#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Alok Kumar'
SITENAME = '@rajalokan'
SITEURL = 'http://localhost:8000'
SITESUBTITLE = AUTHOR
SITETITLE = AUTHOR
PROFILE_IMAGE = 'rajalokan.jpg'

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('email', 'rajalokan@gmail.com'),
          ('twitter', 'https://twitter.com/rajalokan'),
          ('github', 'https://github.com/rajalokan'),
          ('linkedin', 'https://www.linkedin.com/in/alok-kumar-947b838/'),)
          

DEFAULT_PAGINATION = 10

THEME = "pelican-hyde"

DISQUS_SITENAME='rajalokan'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True