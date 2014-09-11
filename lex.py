#!/usr/bin/env python

import os
import sys

from pygments import highlight
from pygments.lexers import get_lexer_for_filename
from pygments.formatters import HtmlFormatter


def lex(filename):
    with open(filename, "r") as f:
        lexer = get_lexer_for_filename(filename)
        return highlight(f.read(), lexer, HtmlFormatter())


if __name__ == "__main__":
    files = [os.path.join("src", f) for f in os.listdir("src")]
    for filename in files:
        print("Lexing: {}".format(filename))
        html = lex(filename)

        dest = "{}.html".format(filename.replace("src/", ""))
        with open(dest, "w") as f:
            f.write(html)
            print("Written to: {}".format(dest))
