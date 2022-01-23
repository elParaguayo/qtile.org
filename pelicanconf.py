import sys

sys.path.append(".")

from jinja2 import nodes
from jinja2.ext import Extension

import utils.qtile as QTILE  # noqa: F401
from extensions.config import DefaultConfig
from utils.screenshots import INLINE_SCREENSHOTS, SCREENSHOTS

class DummyExtension(Extension):
    # a set of names that trigger the extension.
    tags = {"static"}

    # def __init__(self, environment):
    #     super().__init__(environment)

    #     # add the defaults to the environment
    #     environment.extend(fragment_cache_prefix="", fragment_cache=None)

    def parse(self, parser):
        # the first token is the token that started the tag.  In our case
        # we only listen to ``'cache'`` so this will be a name token with
        # `cache` as value.  We get the line number so that we can give
        # that line number to the nodes we create by hand.
        lineno = next(parser.stream).lineno

        # now we parse a single expression that is used as cache key.
        args = [parser.parse_expression()]

        call = self.call_method("_render", args=args, lineno=lineno)
        return nodes.Output([nodes.MarkSafe(call)]).set_lineno(lineno)

        # return nodes.CallBlock(
        #     self.call_method("_render", args), [], [], None
        # ).set_lineno(lineno)

    def _render(self, args):
        """Helper callback."""
        # key = self.environment.fragment_cache_prefix + name

        # # try to load the block from the cache
        # # if there is no fragment in the cache, render it and store
        # # it in the cache.
        # rv = self.environment.fragment_cache.get(key)
        # if rv is not None:
        #     return rv
        # rv = caller()
        # self.environment.fragment_cache.add(key, rv, timeout)
        # return rv
        return f"/theme/{args}"


AUTHOR = "Team Qtile"
SITENAME = "qtile.org"
SITEURL = ""

PATH = "content"

TIMEZONE = "Europe/London"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = False

THEME = "themes/qtile-theme"
WEBASSETS = True

JINJA_ENVIRONMENT = {"extensions": [DummyExtension, DefaultConfig]}

STATIC_PATHS = ["public"]

WEBASSETS_BUNDLES = (
    (
        "qtile_js",
        (
            "../../../public/bower_components/jquery/dist/jquery.min.js",
            "../../../public/bower_components/bootstrap/js/modal.js",
            "../../../public/bower_components/bootstrap/js/collapse.js",
            "../../../public/bower_components/bootstrap/js/tooltip.js",
            "../../../public/bower_components/imagesloaded/imagesloaded.pkgd.min.js",
            "../../../public/bower_components/masonry/dist/masonry.pkgd.min.js",
            "js/microtemplating.js",
            "js/qtile.index.js",
            "js/qtile.screenshots.js",
            "js/qtile.videos.js",
            "js/qtile.toggle.js",
        ),
        {"filters": "rjsmin", "output": "js/qtile.min.js"},
    ),
    (
        "qtile_css",
        (
            "../../../public/bower_components/fontawesome/less/font-awesome.less",
            "../../../public/bower_components/bootstrap/less/bootstrap.less",
            "less/qtile.less",
            "css/pygments.css",
            # "css/qtile.css",
            "https://fonts.googleapis.com/css?family=Open+Sans:400italic,700italic,400,700",
            "https://fonts.googleapis.com/css?family=Varela+Round",
        ),
        {"filters": "less,cssutils", "output": "css/qtile.min.css"},
    )
)
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
LESS_BIN = "/home/anto/node_modules/less/bin/lessc"

