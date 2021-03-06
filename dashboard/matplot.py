from django.shortcuts import render

import urllib, base64
import io

from matplotlib import pyplot as plt
from matplotlib.dates import date2num, num2date
from matplotlib import dates as mdates
from matplotlib import ticker
from matplotlib.colors import ListedColormap
from matplotlib.patches import Patch

from scipy.interpolate import interp1d

import pandas as pd
import numpy as np

#'dsfsi'
repo = 'dsfsi'
credit = 'Source: covid19trends.co.za - Data: DSFSI'


def get_matplot():

    # Get sa province rt data
    url = 'https://raw.githubusercontent.com/' + repo + '/covid19za/master/data/calc/calculated_rt_sa_provincial_cumulative.csv'
    states_raw = pd.read_csv(url,
                         parse_dates=['date'], dayfirst=True,
                         squeeze=True, index_col=[0,1])


    # Plot SA
    country = states_raw.filter(like='Total RSA', axis=0)

    fig_country, ax = plt.subplots(figsize=(600/72,400/72))
    ax = plot_rt(country, ax, state_name = '')
    ax.set_title(credit, size=12, weight='light')
    fig_country.suptitle(f'$R_t$ for COVID-19 in South Africa', size=14)

    # Week labels are to close for longer time ranges
    #ax.xaxis.set_major_locator(mdates.WeekdayLocator())
    #ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))

    #fig_country.text(0, 0.95, credit, size=12, weight='light')
    #fig_country.subplots_adjust(top = 0.90)

    uri_country = format_fig(fig_country)

    # Summary of latest results
    latestdate = country.index.get_level_values('date')[-1].strftime('%d %B %Y')
    latestrt = country.groupby(level=0).last().iloc[0]['ML']

    # Plot provinces
    states_filter = states_raw.loc[list(state_key.keys())]
    fig_states = state_plot(states_filter, 'South African provinces', title_y = 0.90, plotscale = 0.85, title_key=state_key)
    uri_states = format_fig(fig_states)

    # Plot districts
    #uri_districts1 = plot_districts('GP', title_y = 0.78, plotscale = 0.58, title_key=district_gp_key)
    #uri_districts2 = plot_districts('WC', title_y = 0.94, plotscale = 0.90, title_key=district_wc_key)

    # TODO create states summary table
    table_states = ''

    return {'country':uri_country,'states':uri_states, 'latestrt':latestrt, 'latestd':latestdate, 'tablesstates':table_states, 'districts1':'', 'districts2':'', 'debug':''}


def state_plot(final_results, title, title_y, plotscale, title_key):
    state_groups = final_results.groupby('state')

    ncols = 3
    nrows = int(np.ceil(len(state_groups) / ncols))

    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(15, nrows*3))

    for i, (state_name, result) in enumerate(state_groups):
        if (title_key != None):
            state_name = title_key[state_name]
        axes.flat[i] = plot_rt(result, axes.flat[i], state_name)

    fig.tight_layout()
    fig.set_facecolor('w')

    fig.suptitle(f'$R_t$ for COVID-19 in ' + title, size=20)
    fig.text(0.35, title_y, credit, size=16, weight='light')
    fig.subplots_adjust(top = plotscale)

    return fig


def plot_districts(state, title_y, plotscale, title_key):
    # Get sa province rt data
    url = 'https://raw.githubusercontent.com/' + repo + '/covid19za/master/data/calc/calculated_rt_' + state.lower() + '_district_cumulative.csv'
    districts_raw = pd.read_csv(url,
                         parse_dates=['date'], dayfirst=True,
                         squeeze=True, index_col=[0,1])
    # Plot provinces
    fig_districts = state_plot(districts_raw, state_key[state] + ' districts', title_y, plotscale, title_key)

    return format_fig(fig_districts)


def format_fig(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)

    return uri


def plot_rt(result, ax, state_name):
    ax.set_title(f"{state_name}")

    # Colors
    ABOVE = [1,0,0]
    MIDDLE = [1,1,1]
    BELOW = [0,0,0]
    cmap = ListedColormap(np.r_[
        np.linspace(BELOW,MIDDLE,25),
        np.linspace(MIDDLE,ABOVE,25)
    ])
    color_mapped = lambda y: np.clip(y, .5, 1.5)-.5

    index = result['ML'].index.get_level_values('date')
    values = result['ML'].values

    # Plot dots and line
    ax.plot(index, values, c='k', zorder=1, alpha=.25)
    ax.scatter(index,
               values,
               s=40,
               lw=.5,
               c=cmap(color_mapped(values)),
               edgecolors='k', zorder=2)

    # Aesthetically, extrapolate credible interval by 1 day either side
    lowfn = interp1d(date2num(index),
                     result['Low_90'].values,
                     bounds_error=False,
                     fill_value='extrapolate')

    highfn = interp1d(date2num(index),
                      result['High_90'].values,
                      bounds_error=False,
                      fill_value='extrapolate')

    extended = pd.date_range(start=pd.Timestamp('2020-03-01'),
                             end=index[-1]+pd.Timedelta(days=1))

    ax.fill_between(extended,
                    lowfn(date2num(extended)),
                    highfn(date2num(extended)),
                    color='k',
                    alpha=.1,
                    lw=0,
                    zorder=3)

    ax.axhline(1.0, c='k', lw=1, label='$R_t=1.0$', alpha=.25);

    # Formatting
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))
    ax.xaxis.set_minor_locator(mdates.DayLocator())

    ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.yaxis.set_major_formatter(ticker.StrMethodFormatter("{x:.1f}"))
    ax.yaxis.tick_right()
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.margins(0)
    ax.grid(which='major', axis='y', c='k', alpha=.1, zorder=-2)
    ax.margins(0)
    ax.set_ylim(0.0, 5.0)
    ax.set_xlim(pd.Timestamp('2020-03-06'), result.index.get_level_values('date')[-1]+pd.Timedelta(days=1))

    #fig.set_facecolor('w')
    return ax

state_key = {
'EC':'Eastern Cape',
'FS':'Free State',
'GP':'Gauteng',
'KZN':'Kwazulu Natal',
'LP':'Limpopo',
'MP':'Mpumalanga',
'NC':'Northern Cape',
'NW':'North-West',
'WC':'Western Cape'
}
