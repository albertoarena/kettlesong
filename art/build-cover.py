#!/usr/bin/env python3
"""Build the README cover (art/cover-light.svg, art/cover-dark.svg) from art/*.txt.

Run from the repo root after you change the banner or one of the cover figures:
    python3 art/build-cover.py

The cover shows a real reply: the prompt, the banner in a diff block (green),
an italic themed line, and four figures in the order of one session.
The colors are the GitHub diff colors for each theme. Each cover has a solid
background, so it stays readable on a page of the other theme.
"""
import html

WIDTH = 960
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, 'DejaVu Sans Mono', monospace"
THEMES = {
    "light": {"bg": "#ffffff", "row": "#dafbe1", "green": "#1a7f37", "fg": "#1f2328", "muted": "#59636e"},
    "dark": {"bg": "#0d1117", "row": "#12261e", "green": "#3fb950", "fg": "#d1d7e0", "muted": "#9198a1"},
}
PROMPT = "&gt; Hi"
THEMED_LINE = "Good to see you, master; the lamps are lit and the path is clear."
FIGURES = [
    ("elf-bow", "a bug is found"),
    ("dwarf-axe", "the tests pass"),
    ("wizard", "a refactor plan"),
    ("hobbit-tea", "the task is done"),
]
TITLE = (
    "Kettlesong: a green text banner, an italic greeting, and four text figures "
    "for a bug, passing tests, a refactor and a finished task."
)


def piece(name):
    return open(f"art/{name}.txt").read().rstrip("\n").split("\n")


def block(lines, x, y, size, line_height, fill, extra=""):
    out = [f'<text x="{x}" y="{y}" font-family="{MONO}" font-size="{size}" fill="{fill}" xml:space="preserve" {extra}>']
    for i, line in enumerate(lines):
        out.append(f'<tspan x="{x}" y="{y + i * line_height}">{html.escape(line)}</tspan>')
    out.append("</text>")
    return "\n".join(out)


def build(theme):
    c = THEMES[theme]
    s = []

    # Banner: one diff row for each line, with "+" in the gutter.
    y = 40
    size, line_height = 18, 23
    banner = piece("banner")
    cols = 3 + max(len(line) for line in banner)
    row_width = cols * size * 0.6 + 28
    bx = (WIDTH - row_width) / 2
    by = y + 22

    # Prompt, aligned with the banner text.
    s.append(f'<text x="{bx + 14:.1f}" y="{y}" font-family="{MONO}" font-size="15" fill="{c["muted"]}" xml:space="preserve">{PROMPT}</text>')

    for i in range(len(banner)):
        s.append(f'<rect x="{bx:.1f}" y="{by + i * line_height}" width="{row_width:.1f}" height="{line_height}" fill="{c["row"]}"/>')
    tx, ty = bx + 14, by + line_height * 0.74
    s.append(block(["+" for _ in banner], tx, ty, size, line_height, c["green"]))
    s.append(block(["   " + line for line in banner], tx, ty, size, line_height, c["green"], 'font-weight="600"'))

    # Themed line.
    y = by + len(banner) * line_height + 40
    s.append(f'<text x="{WIDTH / 2}" y="{y}" text-anchor="middle" font-family="{MONO}" font-size="15" font-style="italic" fill="{c["fg"]}">{THEMED_LINE}</text>')

    # Figures, bottom-aligned in four equal slots, with a plain label under each.
    y += 30
    size, line_height = 14, 17
    margin = 50
    slot = (WIDTH - 2 * margin) / 4
    fy = y + 26
    for i, (name, label) in enumerate(FIGURES):
        lines = piece(name)
        cols = max(len(line) for line in lines)
        fx = margin + i * slot + (slot - cols * size * 0.6) / 2
        top = fy + (8 - len(lines)) * line_height
        s.append(block(lines, round(fx, 1), top, size, line_height, c["fg"], 'font-weight="500"'))
        s.append(f'<text x="{margin + i * slot + slot / 2:.1f}" y="{fy + 8 * line_height + 14}" text-anchor="middle" font-family="{MONO}" font-size="13" fill="{c["muted"]}">{label}</text>')

    height = int(fy + 8 * line_height + 18 + 30)
    head = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {height}" width="{WIDTH}" height="{height}" role="img" aria-labelledby="t">'
        f'<title id="t">{TITLE}</title>'
        f'<rect width="{WIDTH}" height="{height}" rx="12" fill="{c["bg"]}"/>'
    )
    return head + "\n" + "\n".join(s) + "\n</svg>\n"


for theme in THEMES:
    with open(f"art/cover-{theme}.svg", "w") as f:
        f.write(build(theme))
print(f"Built the cover in {len(THEMES)} themes.")
