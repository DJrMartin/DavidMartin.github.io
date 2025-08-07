from datetime import datetime

AUTHOR = "David Martin"
SITEURL = "https://djrmartin.github.io/DavidMartin.github.io/"
SITENAME = "David Martin - PhD"
SITETITLE = "David Martin - PhD"

RELATIVE_URLS = True

BROWSER_COLOR = "#333333"
PYGMENTS_STYLE = "monokai"

ROBOTS = "index, follow"

THEME = "Flex"
PATH = "content"
OUTPUT_PATH = "docs/"
TIMEZONE = "Europe/Paris"

DISABLE_URL_HASH = True

SITELOGO = "images/profile.png"

# PLUGIN_PATHS = ['pelican-plugins']

# PLUGINS = ['i18n_subsites']

# JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

I18N_TEMPLATES_LANG = "en"
DEFAULT_LANG = "en"
OG_LOCALE = "en_US"
LOCALE = "en_US"

DATE_FORMATS = {
    "en": "%B %d, %Y",
}

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

GITHUB_CORNER_URL = "https://github.com/DJrMartin"

SOCIAL = (
    ("github", "https://github.com/DJrMartin"),
    ("linkedin", "https://www.linkedin.com/in/david-martin-3a3784113"),
    ('google', "https://scholar.google.com/citations?user=7lqARwoAAAAJ&hl=fr")
)

MENUITEMS = (
    ("CV", "CV.html"),
    ("PUBLICATIONS", "publications.html"),
    ("TEACHING", "teaching.html")
)

CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike 4.0 International License",
    "version": "4.0",
    "slug": "by-sa",
    "icon": True,
    "language": "en_US",
}

COPYRIGHT_YEAR = datetime.now().year
DEFAULT_PAGINATION = 10

DISQUS_SITENAME = "flex-pelican"
ADD_THIS_ID = "ra-55adbb025d4f7e55"


THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

USE_LESS = True
