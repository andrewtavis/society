"""
Generates PDFs and PNGs of cards from .txt files
"""

import os

for fname in os.listdir("../resources/cards/generated"):
    if fname.endswith(".svg"):
        basename = fname[:-4]
        for ext in ["pdf", "png"]:
            os.system(
                (
                    "inkscape ../resources/cards/generated/{} "
                    + "--export-filename=../resources/cards/generated/{}/{}.{}"
                ).format(fname, ext, basename, ext)
            )
