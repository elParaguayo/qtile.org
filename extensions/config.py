# Copyright (c) 2022 elParaguayo
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import textwrap

import requests

from jinja2 import nodes
from jinja2.ext import Extension

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

from utils.qtile import TAG

QTILE_METADATA = "https://api.github.com/repos/qtile/qtile/releases/latest"


class DefaultConfig(Extension):
    """
    Basic extension to download default_config.py from latest release
    and highlight text using pygments.
    """

    tags = {"default_config"}

    def parse(self, parser):
        lineno = next(parser.stream).lineno
        call = self.call_method("_render", lineno=lineno)
        return nodes.Output([nodes.MarkSafe(call)]).set_lineno(lineno)

    def _render(self):
        lines = requests.get(
            f"https://raw.githubusercontent.com/qtile/qtile/{TAG}/libqtile/resources/default_config.py"
        ).text
        lines = [line for line in lines.split("\n") if not line.startswith("#")]
        lines.insert(0, f"# Default config file - {TAG}")
        lines = textwrap.dedent("\n".join(lines))
        return highlight(lines, PythonLexer(), HtmlFormatter())
