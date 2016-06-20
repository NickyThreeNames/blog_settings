Title: Portfolio
Date: 2016-4-16 9:51
Category: Blog
Tags: portfolio,
Slug: portfolio
Author: Nick Conti
Summary: Portfolio


### Overview

Curious about a project I've written about in the past?  I will be updating the descriptions here and including links.  My goal is to have a post for all of the listed projects once they are completed.

### Election Results Mapping

There's got to be a better way to display election data on maps, right?  There is a post on the blog (and another is on the way) that goes more in depth.  Additionally, you can take a look at this github [repo](https://github.com/NickyThreeNames/ElectionStatsandMap).  As part of this effort, I have been trying to move away from static pictures and create more interactivity.

Interactive version available [here](http://bl.ocks.org/NickyThreeNames/e3228a8ea478b78c802bb12ac94e3d8c)

![mnmap]({filename}/images/shresults.PNG)


### Election Statistics

While working on campaigns, I spent many hours pouring over targeting spreadsheets.  These re-create a lot of the stastics used in precinct/district targeting such as DPI, Dem Base, Turnout, etc.  The notebooks used to create the post are available [here](https://github.com/NickyThreeNames/ElectionStatsandMap), and it contains a lot of additional analysis that I will post about soon.

Interactive version available [here](http://bl.ocks.org/NickyThreeNames/553327998df38ddf56cc46c6d38713d8)

![mninteractive]({filename}/images/leafletInteractive3.PNG)

### Flask and D3 Powered Web App

While working on some of the above projects, I became more interested on how to host some basic applications online.   I found this [tutorial](https://realpython.com/blog/python/web-development-with-flask-fetching-data-with-requests/#deploying) at [Real Python](https://realpython.com/) and decided to give it a try.  The app creates a bubble chart with D3.js based on stock prices and volume.  This was great tutorial, but I had some trouble deploying the app until I switched to Heroku for hosting.  Live version is [here](http://stocksncm.herokuapp.com/) and  Github repo is [here](https://github.com/NickyThreeNames/stocksD3).

![stockviz]({filename}/images/StockViz1.PNG)

### Targeting Dashboard

Despite spending years of my life trying to make sense of gargantuan spreadsheets full of district statistics, I always thought there had to be a better way to target competitive districts.  Then I stumbled into [Crossfilter](http://square.github.io/crossfilter/) and [dc.js](https://dc-js.github.io/dc.js/) and was really impressed.  I had tried some basic projects but was really inspired to work off of an example I saw [here](https://austinlyons.github.io/dcjs-leaflet-untappd/#).  This [repo](https://github.com/NickyThreeNames/targetingDashboard) has my ongoing work to get an interactive targeting dashboard up and running with data from 2014.

