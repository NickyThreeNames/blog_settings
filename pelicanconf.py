#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Nick Conti'
SITENAME = u'PolitiNerd'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com'),
		('FiveThirtyEight', 'http://fivethirtyeight.com'),
		('RealPython', 'http://realpython.com'),
		('Yhat', 'https://www.yhat.com'),
		('R-bloggers', 'http://www.r-bloggers.com'),)

#SIDEBAR_DIGEST = 'Programmer and Data Analyst'

# Social widget
SOCIAL = (('GitHub', 'https://github.com/NickyThreeNames'),
          ('LinkedIn', 'https://www.linkedin.com/in/nick-conti-6364475'),
          ('Twitter', 'https://twitter.com/nickythreenames'))

STATIC_PATHS = ['images', 'pdfs', 'notebooks', 'extra/CNAME']

EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    }

THEME = "pelican-themes/pelican-bootstrap3"
PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = ['liquid_tags.img', 'liquid_tags.video', 'liquid_tags.vimeo', 'liquid_tags.include_code', 'tag_cloud', 'i18n_subsites']

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
DISPLAY_TAGS_ON_SIDEBAR = True

DISPLAY_TAGS_INLINE = True

DISPLAY_PAGES_ON_MENU = True

TWITTER_USERNAME = "@NickyThreeNames"

NOTEBOOK_DIR = 'notebooks'
BOOTSTRAP_FLUID = True
BOOTSTRAP_THEME = 'flatly'

AVATAR  = '../images/me.png'
ABOUT_ME = """
I am a data analyst living in Minneapolis.
<br></br>
Though I work in banking now, I had my come-up working in political campaign data, beginning as a field organizer and eventually becoming a Statewide Data Director in Michigan.  I spent a lot of my time <del> fighting</del> working with Excel but became annoyed with its limitations as I focused more on data analysis.  Somewhere along the line, I was introduced to R, then Python, and the rest is history.  It was an instant nerd crush and I have been expanding my data programming skills since.  This blog is my valentine to the possibilities of what can be accomplished with data.
<br></br>
When not dealing with numbers, I can be found running, biking, and enjoying a beer on a patio.
 """


DISQUSURL = 'http://nickythreenames.github.io'
DISQUS_SITENAME = 'politinerd'

#EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')
#MENUITEMS = (('Blog', SITEURL),)
DEFAULT_PAGINATION = 10

CACHE_CONTENT = False
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
