// Regenerates assets/hero.svg and assets/method-map.svg: `node scripts/gen-assets.mjs`
// To add a project to the map, append a row to RES or BLD (and keep each column at 4 and 5 rows, or adjust TOP/STEP).
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

// ---------- method map ----------
const RES = [
  ["#5fb3ff", "DRINKING WATER", "TTHM warning rules", "7,149 water systems tested"],
  ["#2dd4bf", "CIRCADIAN HEALTH", "Hypnos", "RL model of the body clock"],
  ["#f472b6", "MULTI-AGENT AI", "Partner rotation study", "Pre-registered, inconclusive"],
  ["#a3e635", "CS EDUCATION", "CSAwesome2", "AI-assisted AP CS exercises"],
];
const BLD = [
  ["#6fe3a0", "TEEN LABOR LAW", "Off the Clock", "Shift to statute to dollars"],
  ["#f4d03f", "BIRD-SAFE GLASS", "Gap check", "Phone photo to millimetre map"],
  ["#ff7b72", "DRONE DETECTION", "Listening Post", "Acoustic alert in a phone"],
  ["#ffa94d", "LEARNING ACCESS", "Vaidra", "Free multilingual courses"],
  ["#818cf8", "BROWSER AUTOMATION", "Endoplexity", "Agents on your own login"],
];

const MW = 888, NW = 244, NH = 70, TOP = 50, STEP = 82;
const MH = TOP + 4 * STEP + NH + 26;
const LX = 28, RX = MW - 28 - NW;
const rightYs = BLD.map((_, i) => TOP + i * STEP);
const lastY = rightYs[4];
const leftYs = RES.map((_, i) => Math.round(TOP + (i * (lastY - TOP)) / 3));
const hubY = Math.round((TOP + NH / 2 + lastY + NH / 2) / 2), hubX = MW / 2;

const nodes = [
  ...RES.map((n, i) => ({ n, x: LX, y: leftYs[i], left: true })),
  ...BLD.map((n, i) => ({ n, x: RX, y: rightYs[i], left: false })),
];

let lines = "", pulses = "", boxes = "";
nodes.forEach(({ n: [color, dom, name, ev], x, y, left }, i) => {
  const yc = y + NH / 2;
  const ex = left ? x + NW : x;
  const d = left
    ? `M${hubX},${hubY} C${hubX - 72},${hubY} ${ex + 78},${yc} ${ex},${yc}`
    : `M${hubX},${hubY} C${hubX + 72},${hubY} ${ex - 78},${yc} ${ex},${yc}`;
  lines += `<path class="ln" d="${d}" stroke="${color}" stroke-opacity=".5"/>`;
  pulses += `<g class="pl" fill="${color}" opacity="0"><circle r="7" opacity=".25"/><circle r="3.2"/>` +
    `<animateMotion dur="3.4s" begin="${(i * 0.38).toFixed(2)}s" repeatCount="indefinite" path="${d}" calcMode="spline" keyTimes="0;1" keySplines=".4 0 .2 1"/>` +
    `<animate attributeName="opacity" values="0;1;1;0" keyTimes="0;.12;.85;1" dur="3.4s" begin="${(i * 0.38).toFixed(2)}s" repeatCount="indefinite"/></g>`;
  boxes += `<rect x="${x}" y="${y}" width="${NW}" height="${NH}" rx="12" fill="#15122f" stroke="${color}" stroke-opacity=".5"/>` +
    `<rect x="${x + 1}" y="${y + 14}" width="3.5" height="${NH - 28}" rx="1.75" fill="${color}"/>` +
    `<text x="${x + 20}" y="${y + 22}" class="d" fill="${color}">${dom}</text>` +
    `<text x="${x + 20}" y="${y + 43}" class="n">${name}</text>` +
    `<text x="${x + 20}" y="${y + 60}" class="e">${ev}</text>`;
});

writeFileSync(
  `${OUT}/method-map.svg`,
  `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${MW} ${MH}" width="${MW}" height="${MH}" role="img" aria-labelledby="t">
<title id="t">One method applied to nine projects</title>
<style>
text{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
.h{font-size:11px;font-weight:600;letter-spacing:1.6px;fill:#9a96c8}
.d{font-size:10.5px;font-weight:600;letter-spacing:1.3px}
.n{font-size:17px;font-weight:700;fill:#f4f2ff}
.e{font-size:12px;fill:#b4b0d8}
.ln{fill:none;stroke-width:1.5;stroke-dasharray:2 7;stroke-linecap:round;animation:flow 1.2s linear infinite}
@keyframes flow{to{stroke-dashoffset:-18}}
@media (prefers-reduced-motion:reduce){.ln{animation:none}.pl{display:none}}
</style>
<rect x=".5" y=".5" width="${MW - 1}" height="${MH - 1}" rx="18" fill="#0c0a1d" stroke="#2b2657"/>
<text x="${LX}" y="32" class="h">RESEARCH</text>
<text x="${MW - LX}" y="32" class="h" text-anchor="end">BUILDS</text>
${lines}
${pulses}
<circle cx="${hubX}" cy="${hubY}" r="66" fill="#1b1647" stroke="#8b5cf6" stroke-width="2"/>
<text x="${hubX}" y="${hubY - 16}" text-anchor="middle" font-size="9.5" font-weight="600" letter-spacing="1.6" fill="#a78bfa">ONE METHOD</text>
<text x="${hubX}" y="${hubY + 6}" text-anchor="middle" font-size="20" font-weight="700" fill="#fff">Systems</text>
<text x="${hubX}" y="${hubY + 26}" text-anchor="middle" font-size="13" fill="#cfcaf7">thinking + AI</text>
${boxes}
</svg>
`
);
