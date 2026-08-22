"""Integer-scale the sprite onto an LCD tank and write an animated GIF."""
from pathlib import Path

from PIL import Image

from sprite import PALETTE, SIZE, TRANSPARENT, frames_for

# Native handheld. Integer scale only.
CANVAS_W = 80
CANVAS_H = 56
LCD = (28, 46, 28)
BEZEL = (42, 36, 28)
SCREEN = (22, 38, 24)


def _paint_tank() -> Image.Image:
    im = Image.new("RGB", (CANVAS_W, CANVAS_H), BEZEL)
    for y in range(4, CANVAS_H - 4):
        for x in range(4, CANVAS_W - 4):
            im.putpixel((x, y), SCREEN if 6 <= x < CANVAS_W - 6 and 6 <= y < CANVAS_H - 6 else LCD)
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
    tank = _paint_tank()
    duration = {"idle": 380, "hungry": 520, "ghost": 640}[mood]
    images = []
    for grid in grids:
        native = _blit_sprite(tank, grid)
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
