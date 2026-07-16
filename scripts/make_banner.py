"""
Komal — self-hosted header banner SVG (no external service dependency)
Generates a locally-rendered banner living inside the repo itself, so it
never depends on a third-party badge/banner API being up.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "banner.svg")
STATIC = bool(os.environ.get("STATIC"))

W, H = 900, 210

BG0, BG1, BG2 = "#0F172A", "#312E81", "#4F46E5"
INK = "#FFFFFF"
SUB = "#C7D2FE"

NAME = "Komal Priya"
TAGLINE_LINES = [
    "Aspiring AI Engineer & ML Enthusiast",
    "Building with Python + Data Structures & Algorithms",
    "Developing Skills in Generative AI + LLMs",
]

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{BG0}"/>
      <stop offset="0.5" stop-color="{BG1}"/>
      <stop offset="1" stop-color="{BG2}"/>
    </linearGradient>
    <clipPath id="clip"><rect width="{W}" height="{H}" rx="14"/></clipPath>
  </defs>

  <g clip-path="url(#clip)">
    <rect width="{W}" height="{H}" fill="url(#bg)"/>

    <path d="M0,{H} L0,{H-70} Q{W*0.25},{H-30} {W*0.5},{H-70} T{W},{H-70} L{W},{H} Z"
          fill="#ffffff" opacity="0.06"/>
    <path d="M0,{H} L0,{H-40} Q{W*0.25},{H-90} {W*0.5},{H-40} T{W},{H-40} L{W},{H} Z"
          fill="#ffffff" opacity="0.05"/>

    <text x="{W/2}" y="72" text-anchor="middle" fill="{INK}"
          font-family="'Segoe UI', ui-sans-serif, system-ui, sans-serif"
          font-size="46" font-weight="700">{NAME}</text>

    <g font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
       font-size="19" fill="{SUB}" text-anchor="middle">
'''

n = len(TAGLINE_LINES)
hold = 1.8
fade = 0.5
cycle = n * hold
for i, line in enumerate(TAGLINE_LINES):
    start = i * hold
    esc = line.replace("&", "&amp;")
    if STATIC or n == 1:
        opacity_attr = '1' if i == 0 else '0'
        svg += f'      <text x="{W/2}" y="120" opacity="{opacity_attr}">{esc}</text>\n'
    else:
        svg += (
            f'      <text x="{W/2}" y="120" opacity="0">{esc}\n'
            f'        <animate attributeName="opacity" '
            f'values="0;0;1;1;0;0" '
            f'keyTimes="0;{start/cycle:.4f};{(start+fade)/cycle:.4f};'
            f'{(start+hold-fade)/cycle:.4f};{(start+hold)/cycle:.4f};1" '
            f'dur="{cycle}s" repeatCount="indefinite"/>\n'
            f'      </text>\n'
        )

svg += '''    </g>
  </g>
  <rect x="0.5" y="0.5" width="''' + str(W-1) + '''" height="''' + str(H-1) + '''" rx="14" fill="none" stroke="#ffffff" stroke-opacity="0.12"/>
</svg>
'''

with open(OUT, "w") as f:
    f.write(svg)
print("wrote", OUT, len(svg), "bytes;", W, "x", H)
