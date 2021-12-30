"""
Generates PDFs and PNGs of cards from .svg files
"""

import os
from sys import platform

if platform == "darwin":  # OSX
    inkscape_prompt = "/Applications/Inkscape.app/Contents/MacOS/inkscape"
else:
    inkscape_prompt = "inkscape"

for fname in os.listdir("../components/cards/svg"):
    basename = fname[:-4]
    for ext in ["pdf", "png"]:
        os.system(
            (
                "{} ../components/cards/svg/{} "
                + "--export-filename=../components/cards/{}/{}.{}"
            ).format(inkscape_prompt, fname, ext, basename, ext)
        )
