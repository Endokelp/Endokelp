"""32x32 kelp pup. Round body, big eyes, tiny feet — Jeff / Doraemon energy, not a copy."""

SIZE = 32
TRANSPARENT = "."

PALETTE = {
    "s": (38, 98, 96),      # teal shadow
    "b": (72, 176, 164),    # body
    "h": (255, 232, 196),   # belly
    "w": (252, 252, 250),   # eye white
    "e": (24, 22, 28),      # pupil / smile
    "f": (92, 56, 42),      # feet
}


def _put(g: list[list[str]], x: int, y: int, c: str) -> None:
    if 0 <= x < SIZE and 0 <= y < SIZE:
        g[y][x] = c


def _disk(g: list[list[str]], cx: float, cy: float, rx: float, ry: float, c: str) -> None:
    for y in range(SIZE):
        for x in range(SIZE):
            if ((x + 0.5 - cx) / rx) ** 2 + ((y + 0.5 - cy) / ry) ** 2 <= 1:
                g[y][x] = c


def _paint_base() -> list[str]:
    g = [[TRANSPARENT] * SIZE for _ in range(SIZE)]
    # body sits low so the fin reads above the head
    _disk(g, 16, 17, 10, 10, "s")
    _disk(g, 16, 17, 9, 9, "b")
    _disk(g, 16, 21, 6.5, 4.2, "h")
    # Jeff-ish fin
    for x, y, c in (
        (16, 1, "s"),
        (15, 2, "s"), (16, 2, "b"), (17, 2, "s"),
        (15, 3, "s"), (16, 3, "b"), (17, 3, "b"), (18, 3, "s"),
        (16, 4, "b"), (17, 4, "b"), (18, 4, "s"),
        (16, 5, "b"), (17, 5, "s"),
        (16, 6, "b"),
    ):
        _put(g, x, y, c)
    # eyes
    _disk(g, 11.2, 15.2, 3.4, 3.6, "w")
    _disk(g, 20.8, 15.2, 3.4, 3.6, "w")
    for x, y in ((12, 15), (13, 15), (12, 16), (20, 15), (19, 15), (20, 16)):
        _put(g, x, y, "e")
    # smile on the face, not the belly
    _put(g, 15, 20, "s")
    _put(g, 16, 21, "s")
    _put(g, 17, 20, "s")
    # stub arms
    _put(g, 6, 19, "b")
    _put(g, 5, 20, "s")
    _put(g, 6, 20, "b")
    _put(g, 26, 19, "b")
    _put(g, 27, 20, "s")
    _put(g, 26, 20, "b")
    # feet
    for x in range(9, 13):
        _put(g, x, 27, "f")
        _put(g, x, 28, "f")
    _put(g, 8, 28, "f")
    for x in range(20, 24):
        _put(g, x, 27, "f")
        _put(g, x, 28, "f")
    _put(g, 24, 28, "f")
    return ["".join(row) for row in g]


def _shift_vertical(grid: list[str], dy: int) -> list[str]:
    empty = TRANSPARENT * SIZE
    if dy < 0:
        return grid[-dy:] + [empty] * (-dy)
    if dy > 0:
        return [empty] * dy + grid[:-dy]
    return list(grid)


def _blink(grid: list[str]) -> list[str]:
    out = []
    for row in grid:
        if "e" in row and "w" in row:
            out.append(row.replace("e", "s").replace("w", "s"))
        else:
            out.append(row)
    return out


def _sit(grid: list[str]) -> list[str]:
    dropped = _shift_vertical(grid, 2)
    feet = list(dropped)
    for i, row in enumerate(feet):
        if "f" not in row:
            continue
        chars = list(row)
        left = chars.index("f")
        right = SIZE - 1 - chars[::-1].index("f")
        if left > 0:
            chars[left - 1] = "f"
        if right < SIZE - 1:
            chars[right + 1] = "f"
        feet[i] = "".join(chars)
    return feet


def _outline(grid: list[str]) -> list[str]:
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
    base = _paint_base()
    if mood == "hungry":
        sit = _sit(base)
        return [sit, _blink(sit)]
    if mood == "ghost":
        g = _outline(base)
        return [g, _shift_vertical(g, -1)]
    up = _shift_vertical(base, -1)
    return [base, up, _blink(base), _shift_vertical(base, 1)]
