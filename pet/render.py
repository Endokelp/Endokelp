"""Integer-scale the sprite onto an LCD tank and write an animated GIF."""
from pathlib import Path

from PIL import Image

from sprite import PALETTE, SIZE, TRANSPARENT, frames_for

CANVAS_W = 80
CANVAS_H = 56
LCD = (42, 36, 28)
BEZEL = (42, 36, 28)
SCREEN = (18, 42, 36)
SAND = (58, 72, 40)
PEBBLE = (44, 52, 32)
KELP_DARK = (16, 78, 52)
KELP_LIT = (42, 138, 74)
BUBBLE = (150, 196, 160)

# ponytail: stalks as (x, top_y). Sway is 1px. Upgrade: more plants if the tank feels empty.
_STALKS = ((9, 16), (15, 12), (21, 20), (58, 14), (66, 18), (71, 22))
_PEBBLES = ((8, 48), (12, 49), (18, 48), (28, 49), (50, 48), (62, 49), (70, 48))


def _paint_tank(sway: int = 0) -> Image.Image:
    im = Image.new("RGB", (CANVAS_W, CANVAS_H), BEZEL)
    for y in range(4, CANVAS_H - 4):
        for x in range(4, CANVAS_W - 4):
            inside = 6 <= x < CANVAS_W - 6 and 6 <= y < CANVAS_H - 6
            im.putpixel((x, y), SCREEN if inside else LCD)
    floor_y = CANVAS_H - 10
    for y in range(floor_y, CANVAS_H - 6):
        for x in range(6, CANVAS_W - 6):
            im.putpixel((x, y), SAND)
    for sx, top in _STALKS:
        for y in range(top, floor_y):
            dx = sway if (y // 4) % 2 == 0 else 0
            x = sx + dx
            if 6 <= x < CANVAS_W - 7:
                im.putpixel((x, y), KELP_DARK)
                im.putpixel((x + 1, y), KELP_LIT)
            if y % 5 == 2 and 8 <= x < CANVAS_W - 10:
                side = -1 if ((y // 5) + sx) % 2 else 1
                im.putpixel((x + side * 2, y), KELP_LIT)
                im.putpixel((x + side * 3, y), KELP_DARK)
                if 6 <= y - 1:
                    im.putpixel((x + side * 3, y - 1), KELP_LIT)
    for px, py in _PEBBLES:
        im.putpixel((px, py), PEBBLE)
    for bx, by in ((24, 14 + sway), (40, 18 - sway), (54, 12 + sway)):
        if 6 <= by < floor_y:
            im.putpixel((bx, by), BUBBLE)
            if by > 6:
                im.putpixel((bx, by - 1), BUBBLE)
    return im


def _blit_sprite(tank: Image.Image, grid: list[str]) -> Image.Image:
    frame = tank.copy()
    ox = (CANVAS_W - SIZE) // 2
    oy = CANVAS_H - SIZE - 6
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == TRANSPARENT:
                continue
            frame.putpixel((ox + x, oy + y), PALETTE[cell])
    return frame


def write_gif(path: Path, mood: str, scale: int = 4) -> Path:
    if scale < 1 or scale != int(scale):
        raise ValueError("scale must be a positive integer")
    grids = frames_for(mood)
    duration = {"idle": 380, "hungry": 520, "ghost": 640}[mood]
    images = []
    for i, grid in enumerate(grids):
        native = _blit_sprite(_paint_tank(i % 2), grid)
        images.append(native.resize((CANVAS_W * scale, CANVAS_H * scale), Image.Resampling.NEAREST))
    path = Path(path)
    images[0].save(
        path,
        save_all=True,
        append_images=images[1:],
        duration=duration,
        loop=0,
        disposal=2,
    )
    return path


if __name__ == "__main__":
    root = Path(__file__).resolve().parent.parent
    write_gif(root / "pet.gif", "idle", scale=4)
