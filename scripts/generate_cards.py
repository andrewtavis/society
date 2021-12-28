"""
Generates SVGs of cards from .txt files
"""

for kind in ["event", "action"]:
    with open("../components/cards/{}_cards.txt".format(kind), "r") as txt:
        title = None
        print(txt)
        for idx, line in enumerate(txt):
            line = line[:-1]
            if idx % 3 == 0:
                if title:
                    with open("../templates/{}_cards.svg".format(kind), "r") as svg:
                        with open(
                            "../components/cards/svg/{}_{}.svg".format(kind, idx // 3),
                            "w",
                        ) as out:
                            for l in svg:
                                l = l.replace("{{title}}", title).replace(
                                    "{{content}}", content
                                )
                                out.write(l)
                title = line
            elif idx % 3 == 1:
                content = line[1:]
