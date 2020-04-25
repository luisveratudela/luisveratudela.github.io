#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = ''
SITENAME = 'Personal Notes'
SITESUBTITLE = 'Luis Vera-Tudela'
SITEURL = ''

PATH = 'content'

DEFAULT_DATE = 'fs'

DEFAULT_DATE_FORMAT = '%d %b %Y'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/luis_veratudela'),
          ('github', 'https://github.com/luisveratudela'),
          ('linkedin', 'https://www.linkedin.com/in/luisveratudela/'),
          ('instagram', 'https://www.instagram.com/luisveratudela/'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['assets', 'posts', 'images', 'downloads']

EXTRA_PATH_METADATA = {
    'assets/robots.txt': {'path': 'robots.txt'},
    'assets/favicon.ico': {'path': 'favicon.ico'},
    'assets/CNAME': {'path': 'CNAME'}
}

THEME = 'attila'

PLUGIN_PATHS = ['pelican-plugins']
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PLUGINS = ['i18n_subsites', 'pelican-ipynb.markup']
I18N_TEMPLATES_LANG = 'en'

MARKUP = ('md', 'ipynb')
IGNORE_FILES = [".ipynb_checkpoints"]

# set header background, if posts have no cover image
HEADER_COVER = 'images/typewritter.jpg'
HEADER_COLOR = 'black'

# to customize color scheme
COLOR_SCHEME_CSS = 'monokai.css'
