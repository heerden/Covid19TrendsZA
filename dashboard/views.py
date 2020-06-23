from django.shortcuts import render
from .matplot import get_matplot
from .graphly import trend_plots, future_plots 


def home(request):

    content  = trend_plots()

    return render(request, 'home.html', {'content':content})

def export(request):

    return render(request, 'export.html')


def forecast(request):

    content = future_plots()

    return render(request, 'forecast.html', {'content':content})


def matplot(request):

    matplot_fig = get_matplot()

    return render(request, 'matplot.html', matplot_fig)
