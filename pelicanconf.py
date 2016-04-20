#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

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
LINKS = (('Pelican', 'http://getpelican.com/'),)


# Social widget
SOCIAL = (('GitHub', 'https://github.com/NickyThreeNames'),
          ('LinkedIn', 'https://www.linkedin.com/in/nick-conti-6364475'),)

STATIC_PATHS = ['images', ]

THEME = "pelican-themes/blue-penguin"


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
