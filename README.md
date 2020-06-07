# Covid19 Trends ZA Dashboard Project

## Introduction

This is a Covid-19 analytics dashboard for South Africa. The focus is on the Effective Reproduction Number (Rt).

This project was inspired by analytics on USA data, [Rt.live](https://rt.live). The South African model was refined by the [Data Science for Social Impact research group](https://github.com/dsfsi/covid19za/blob/master/notebooks/Realtime%20R0.ipynb) (DFSI).

The dashboard is build with Django. The analytics engine currently runs on the [DFSI](https://github.com/dsfsi/covid19za) repo.

## Contributing

1. Fork the repo
1. Open a new issue
1. Make changes and commit code
1. Submit a pull request

### TODOs

1. Improve front-end layout
1. Change all plots to Plotly
1. Consider using a cron job to store the latest Rt data with PostgreSQL DB
1. Consider running the analytics engine directly in this project (low priority)

## Installing

1. `$ brew install postgresql`
1. `$ pip install -r requirements.txt`
1. `$ python manage.py collectstatic --noinput `
1. `$ python manage.py runserver`
