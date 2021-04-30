import urllib.parse


filename = "README.md"


def headlevel(line):
    if line.startswith("#"):
        new_line = line.lstrip("#")
        return len(line) - len(new_line)
    else:
        return 0


def head2contents(line, level):
    new_line = line.lstrip("#").lstrip(" ")
    tag = (level - 2) * "\t" + "* "
    title = new_line.replace("\n", "")
    link = "#" + new_line.replace(" ", "-").replace("\n", "").replace(".", "")

    return f"{tag}[{title}]({link})"


def run():
    with open(filename, "r") as f:
        lines = f.readlines()

    contents = ""
    for line in lines:
        level = headlevel(line)
        if level:
            contents += head2contents(line, level) + "\n"

    with open("contents-en.md", "w+") as f:
        f.write(contents)


run()
