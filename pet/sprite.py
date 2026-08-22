"""32x32 kelp pet. Chibi: big uneven pneumatocyst head, unmatched blades, holdfast feet."""

SIZE = 32
TRANSPARENT = "."

# 5 colors. Olive LCD, not indigo. Hue-shifted shadow (cool) and highlight (warm).
PALETTE = {
    "s": (45, 74, 56),    # shadow kelp
    "b": (90, 143, 74),   # body
    "h": (201, 212, 163), # pneumatocyst highlight
    "f": (107, 74, 50),   # holdfast
    "e": (20, 24, 16),    # eye
}

# ponytail: one base grid; frames are shifts / blinks / outlines of this.
_BASE = """\
................................
................................
........hhhhhhhhh...............
......hhhbbbbbbbhhh.............
.....hhbbbbbbbbbbbhh............
....hbbbbbbbbbbbbbbbh...........
....hbbbbbbbbbbbbbbbh...........
....hb.e......bbbbbbh...........
....hbbbbbbb....e.bbh...........
....hbbbbbbbbbbbbbbbh...........
.....hhbbbbbbbbbbbbhh...........
......hhhbbbbbbbbhhh............
........hhhhhhhhhh..............
...........bbbbbb...............
...........bbbbbb...............
..sssb.....bbbbbb.....bss.......
.sbbbb.....bbbbbb.....bbbs......
.sbbbbb....bbbbbb....bbbbs......
..sbbbb....bbbbbb....bbbs.......
...sss.....bbbbbb.....ss........
...........bb..bb...............
...........bb..bb...............
..........bbb..bbb..............
.........bbbb..bbbb.............
.......fff........ffff..........
......ffff........fffff.........
......fff..........fff..........
.......ff..........ff...........
................................
................................
................................
................................"""


def _rows(text: str) -> list[str]:
    rows = text.strip("\n").split("\n")
    if len(rows) != SIZE or any(len(r) != SIZE for r in rows):
        raise ValueError("sprite must be 32x32")
    return rows


def _shift_vertical(grid: list[str], dy: int) -> list[str]:
    empty = TRANSPARENT * SIZE
    if dy < 0:
        return grid[-dy:] + [empty] * (-dy)
    if dy > 0:
        return [empty] * dy + grid[:-dy]
    return list(grid)


def _blink(grid: list[str]) -> list[str]:
    return [row.replace("e", "s") for row in grid]


def _sit(grid: list[str]) -> list[str]:
    """Hungry: drop the head two pixels, widen the feet."""
    dropped = _shift_vertical(grid, 2)
    feet = list(dropped)
    # holdfast spreads one pixel outward on the sit rows
    for i in range(24, 28):
        row = list(feet[i])
        if "f" in row:
            left = row.index("f")
            right = SIZE - 1 - row[::-1].index("f")
            if left > 0:
                row[left - 1] = "f"
            if right < SIZE - 1:
                row[right + 1] = "f"
        feet[i] = "".join(row)
    return feet


def _outline(grid: list[str]) -> list[str]:
    """Ghost: keep only edge pixels, recode as shadow."""
    filled = {(x, y) for y, row in enumerate(grid) for x, c in enumerate(row) if c != TRANSPARENT}
    out = []
    for y, row in enumerate(grid):
        chars = []
        for x, c in enumerate(row):
            if c == TRANSPARENT:
                chars.append(TRANSPARENT)
                continue
            neighbors = ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1))
            if any(n not in filled for n in neighbors):
                chars.append("s")
            else:
                chars.append(TRANSPARENT)
        out.append("".join(chars))
    return out


def frames_for(mood: str) -> list[list[str]]:
    base = _rows(_BASE)
    if mood == "hungry":
        sit = _sit(base)
        return [sit, _blink(sit)]
    if mood == "ghost":
        g = _outline(base)
        return [g, _shift_vertical(g, -1)]
    # idle: 4-frame breathe + blink (pixel-art-sprites idle count)
    up = _shift_vertical(base, -1)
    return [base, up, _blink(base), _shift_vertical(base, 1)]
