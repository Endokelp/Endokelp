"""RED: pet mood, sprite grid, and GIF contract."""
import unittest
from pathlib import Path

from mood import mood_from_idle_days
from render import write_gif
from sprite import PALETTE, SIZE, TRANSPARENT, frames_for


class MoodTests(unittest.TestCase):
    def test_committed_today_is_idle(self):
        self.assertEqual(mood_from_idle_days(0), "idle")

    def test_quiet_day_is_hungry(self):
        self.assertEqual(mood_from_idle_days(1), "hungry")

    def test_four_quiet_days_is_ghost(self):
        self.assertEqual(mood_from_idle_days(4), "ghost")


class SpriteTests(unittest.TestCase):
    def test_idle_frames_are_32_square(self):
        frames = frames_for("idle")
        self.assertGreaterEqual(len(frames), 2)
        for grid in frames:
            self.assertEqual(len(grid), SIZE)
            self.assertTrue(all(len(row) == SIZE for row in grid))

    def test_pixels_stay_in_palette(self):
        allowed = set(PALETTE) | {TRANSPARENT}
        for mood in ("idle", "hungry", "ghost"):
            for grid in frames_for(mood):
                used = {cell for row in grid for cell in row}
                self.assertTrue(used <= allowed, used - allowed)

    def test_silhouette_has_enough_body(self):
        grid = frames_for("idle")[0]
        filled = sum(cell != TRANSPARENT for row in grid for cell in row)
        self.assertGreater(filled, 40)

    def test_idle_has_eye_whites(self):
        used = {cell for row in frames_for("idle")[0] for cell in row}
        self.assertIn("w", used)


class GifTests(unittest.TestCase):
    def test_tank_has_kelp(self):
        from render import KELP_LIT, _paint_tank

        tank = _paint_tank(0)
        pixels = {tank.getpixel((x, y)) for y in range(tank.height) for x in range(tank.width)}
        self.assertIn(KELP_LIT, pixels)

    def test_idle_gif_is_animated(self):
        out = Path(__file__).resolve().parent.parent / "pet.gif"
        write_gif(out, "idle", scale=4)
        data = out.read_bytes()
        self.assertTrue(data.startswith(b"GIF89a"))
        self.assertIn(b"\x21\xf9", data)  # graphic control = animation


if __name__ == "__main__":
    unittest.main()
