#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Nick Conti'
SITENAME = u'PolitiNerd'
SITEURL = 'http://localhost:8000/'

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
LINKS = (('Pelican', 'http://getpelican.com/'),)

SIDEBAR_DIGEST = 'Programmer and Data Analyst'
# Social widget
SOCIAL = (('GitHub', 'https://github.com/NickyThreeNames'),
          ('LinkedIn', 'https://www.linkedin.com/in/nick-conti-6364475'),
          ('Twitter', 'https://twitter.com/nickythreenames'))

STATIC_PATHS = ['images', 'pdfs']


THEME = "pelican-themes/pelican-blue"
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code', 'liquid_tags.notebook']
DISPLAY_PAGES_ON_MENU = True

TWITTER_USERNAME = '@NickyThreeNames'


#PROFILE_PICTURE = '/images/NickCM.png'
MENUITEMS = (('Blog', SITEURL),)
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
