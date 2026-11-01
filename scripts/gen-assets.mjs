// Regenerates assets/hero.svg: `node scripts/gen-assets.mjs`
import { writeFileSync, mkdirSync } from "node:fs";
import { fileURLToPath } from "node:url";

const OUT = process.argv[2] ?? fileURLToPath(new URL("../assets", import.meta.url));
mkdirSync(OUT, { recursive: true });

// ---------- hero: pixel wordmark ----------
const G = {
  E: ["11111", "10000", "10000", "11110", "10000", "10000", "11111"],
  N: ["10001", "11001", "10101", "10011", "10001", "10001", "10001"],
  D: ["11110", "10001", "10001", "10001", "10001", "10001", "11110"],
  O: ["01110", "10001", "10001", "10001", "10001", "10001", "01110"],
  K: ["10001", "10010", "10100", "11000", "10100", "10010", "10001"],
  L: ["10000", "10000", "10000", "10000", "10000", "10000", "11111"],
  P: ["11110", "10001", "10001", "11110", "10000", "10000", "10000"],
};
const WORD = "ENDOKELP";
const CELL = 15, SIZE = 13, LETTER_GAP = 2;
const cols = WORD.length * 5 + (WORD.length - 1) * LETTER_GAP;
const W = 888;
const x0 = Math.round((W - (cols * CELL - (CELL - SIZE))) / 2);
const y0 = 34, H = y0 * 2 + 7 * CELL - (CELL - SIZE);

const lerp = (a, b, t) => Math.round(a + (b - a) * t);
const rowColor = (r) => {
  const t = r / 6, a = [167, 139, 250], b = [124, 58, 237];
  return `rgb(${lerp(a[0], b[0], t)},${lerp(a[1], b[1], t)},${lerp(a[2], b[2], t)})`;
};

const cells = [];
let col = 0;
for (const ch of WORD) {
  G[ch].forEach((line, r) => {
    [...line].forEach((bit, c) => {
      if (bit === "1") cells.push({ x: x0 + (col + c) * CELL, y: y0 + r * CELL, r, k: col + c });
    });
  });
  col += 5 + LETTER_GAP;
}

const rect = (c, extra = "") => `<rect x="${c.x}" y="${c.y}" width="${SIZE}" height="${SIZE}" rx="2.5" ${extra}/>`;
const shadow = cells.map((c) => rect({ ...c, x: c.x + 4, y: c.y + 4 })).join("");
const base = cells
  .map((c) => rect(c, `class="c" fill="${rowColor(c.r)}" style="animation-delay:${c.k * 22 + c.r * 30}ms"`))
  .join("");
const shine = cells.map((c) => rect(c, `fill="url(#sh)"`)).join("");

writeFileSync(
  `${OUT}/hero.svg`,
  `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" role="img" aria-labelledby="t">
<title id="t">ENDOKELP</title>
<style>
.c{animation:pop .55s cubic-bezier(.2,.8,.2,1) backwards;transform-box:fill-box;transform-origin:center}
@keyframes pop{from{opacity:0;transform:scale(.3)}}
@media (prefers-reduced-motion:reduce){.c{animation:none}.shine{display:none}}
</style>
<defs>
<linearGradient id="sh" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="160" y2="-60">
<stop offset="0" stop-color="#fff" stop-opacity="0"/>
<stop offset=".5" stop-color="#fff" stop-opacity=".55"/>
<stop offset="1" stop-color="#fff" stop-opacity="0"/>
<animateTransform attributeName="gradientTransform" type="translate" values="-260 0;1100 0;1100 0" keyTimes="0;.3;1" dur="10s" begin="2.2s" repeatCount="indefinite"/>
</linearGradient>
</defs>
<g fill="#4c1d95" opacity=".28">${shadow}</g>
<g>${base}</g>
<g class="shine">${shine}</g>
</svg>
`
);
