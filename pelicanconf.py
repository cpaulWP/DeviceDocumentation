#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Wasatch Photonics'
AUTHORS = u'Wasatch Photonics'
SITENAME = u'Devices'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


STATIC_PATHS = ['images', 'files', 'extra/robots.txt',
        'extra/favicon.ico', 'extra/custom.css', 'extra/CNAME']


EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/CNAME': {'path': 'CNAME'},
}

# Blogroll
LINKS = None

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/wasatchphotonic'),
          ('linkedin', 'https://www.linkedin.com/company/wasatch-photonics'),
          ('google-plus', 'https://plus.google.com/113901159584735714933/about'),
          ('github', 'http://github.com/WasatchPhotonics'),
          ('youtube', 'https://www.youtube.com/watch?v=-a69RZVyrZ8'),
          ('facebook', 'https://www.facebook.com/Wasatch-Photonics-155250911204558/'),
         )

# Don't show generated categories in menu (like manuals)
DISPLAY_CATEGORIES_ON_MENU=False

# Show the colorful banner image on all pages
#BANNER = 'images/wasatch_logo_rev_main.png'
BANNER = 'images/banner.png'
BANNER_ALL_PAGES = True
BANNER_SUBTITLE = "Wasatch Photonics"

# don't show any of the right side info
HIDE_SIDEBAR=True

#BOOTSTRAP_THEME="simplex"

HIDE_SITENAME=True

# This documentation is designed to be hosted in a sub domain of a root
# domain.
ROOT_URL="http://wasatchphotonics.com"
