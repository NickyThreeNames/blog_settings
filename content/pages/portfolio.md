Title: Portfolio
Date: 2016-4-16 9:51
Category: Blog
Tags: portfolio,
Slug: portfolio
Author: Nick Conti
Summary: Portfolio


### Overview

This is a spot to highlight ongoing and completed projects in data analysis.  If I have written a post about the project, I will update the description here to include a link.  My goal is to have a post for all of the listed projects once they are completed.

### Election Results Mapping

Basically working to find better ways to display election data on maps.  There are two posts, available here and here that go more in depth.  Additionally, you can take a look at this github [repo](https://github.com/NickyThreeNames/ElectionStatsandMap).  As part of this I have been trying to move away from just static pictures and create more interactivity.

![mnmap]({filename}/images/shresults.PNG)

Live version available [here](http://bl.ocks.org/NickyThreeNames/e3228a8ea478b78c802bb12ac94e3d8c)

### Election Statistics

While working on campaigns, I spent many hours pouring over targeting spreadsheets.  These are attempts at re-creating a lot of the stastics used in precinct/district targeting such as DPI, Dem Base, Turnout, etc.  See this post for more information.  The notebooks used to create the post is available [here](https://github.com/NickyThreeNames/ElectionStatsandMap), and contains a lot of additional analysis that I plan to write up into a post soon.

### Flask and D3 Powered Web App

While working on some of the above projects, I became more interested on how to host some basic applications online.   I found this [tutorial](https://realpython.com/blog/python/web-development-with-flask-fetching-data-with-requests/#deploying) at [Real Python](https://realpython.com/) and decided to give it a try.  The app creates a bubble chart with D3.js.  This has been a great tutorial, but I had some trouble deploying the app until I switched to Heroku for hosting.  Live version is [here](http://stocksncm.herokuapp.com/) and  Github repo is [here](https://github.com/NickyThreeNames/stocksD3).

### Targeting Dashboard

Despite spending years of my life trying to make sense of gargantuan spreadsheets full of district statistics, I always thought there had to be a better way to target competitive districts.  Then I stumbled into [Crossfilter](http://square.github.io/crossfilter/) and [dc.js](https://dc-js.github.io/dc.js/) and was really impressed .  I had tried some basic projects but was really inspired to work off of an example I saw [here](https://austinlyons.github.io/dcjs-leaflet-untappd/#).  This [repo](https://github.com/NickyThreeNames/targetingDashboard) has my ongoing work to get an interactive targeting dashboard up and running with data from 2014.

