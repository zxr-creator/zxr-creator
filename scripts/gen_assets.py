"""Generate the profile SVGs (light + dark). Usage: python3 scripts/gen_assets.py assets"""
import sys
from xml.sax.saxutils import escape as esc

OUT = sys.argv[1]

THEMES = {
    "light": dict(bg="#ffffff", surface="#ffffff", surface2="#fafafa", ink="#0a0a0a", ink2="#4d4d4d", ink3="#8f8f8f",
                  line="#ebebeb", line2="#d9d9d9", accent="#2450e6", soft="#eef2ff", green="#16a34a",
                  t1="#f5f5f5", t2="#ededed", t3="#e3e3e3", dot="rgba(10,10,10,0.09)"),
    "dark": dict(bg="#0d1117", surface="#0d1117", surface2="#161b22", ink="#ededed", ink2="#a8b0ba", ink3="#7d8590",
                 line="#21262d", line2="#30363d", accent="#6f8cff", soft="#121a33", green="#3ccf7a",
                 t1="#161b22", t2="#1c2128", t3="#262c36", dot="rgba(237,237,237,0.07)"),
}
SANS = "Geist, Inter, ui-sans-serif, -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "'Geist Mono', ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace"

BASE_CSS = """
.sans{{font-family:{sans}}} .mono{{font-family:{mono}}}
@keyframes pulse{{0%,100%{{opacity:1}}50%{{opacity:.25}}}}
@keyframes cyc{{0%,30%{{opacity:1}}34%,100%{{opacity:0}}}}
@keyframes draw{{0%{{stroke-dashoffset:1}}55%,100%{{stroke-dashoffset:0}}}}
@keyframes fill{{0%,40%{{opacity:0}}60%,100%{{opacity:1}}}}
@keyframes pop{{0%,52%{{opacity:0}}60%,100%{{opacity:1}}}}
.pulse{{animation:pulse 2.2s ease-in-out infinite}}
.f{{opacity:0;animation:cyc 6s linear infinite}} .f1{{opacity:1}} .f2{{animation-delay:2s}} .f3{{animation-delay:4s}}
.draw{{stroke-dasharray:1;stroke-dashoffset:0;animation:draw 6s ease-out infinite}}
.area{{animation:fill 6s ease-out infinite}} .pop{{animation:pop 6s ease-out infinite}}
@media (prefers-reduced-motion:reduce){{*{{animation:none!important}}}}
"""


def svg_open(w, h, title, c):
    css = BASE_CSS.format(sans=SANS, mono=MONO)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" '
            f'aria-label="{esc(title)}">\n<title>{esc(title)}</title>\n<style>{css}</style>\n'
            f'<defs><pattern id="dots" width="16" height="16" patternUnits="userSpaceOnUse">'
            f'<circle cx="8" cy="8" r="1" fill="{c["dot"]}"/></pattern></defs>\n')


# ------------------------------------------------------------------ hero
def sparse_frames(n=16):
    """Block-sparse causal attention: attention-sink column + diagonal are always read;
    a few heavy-hitter key blocks (vertical stripes) change from step to step."""
    static = {(i, j) for i in range(n) for j in range(i + 1) if j == 0 or j == i}
    heavy = [(4, 10), (6, 12), (3, 9)]
    frames = [{(i, j) for j in cols for i in range(n) if i > j} - static for cols in heavy]
    return static, frames


def hero(c):
    W, H = 1200, 400
    s = [svg_open(W, H, "zxr-creator: efficient AI, ML systems, and recursive self-improvement", c)]
    s.append(f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="18" fill="{c["bg"]}" stroke="{c["line"]}"/>')

    # left column
    s.append(f'<circle class="pulse" cx="64" cy="76" r="4" fill="{c["accent"]}"/>')
    s.append(f'<text class="mono" x="78" y="80.5" font-size="12.5" letter-spacing="2" fill="{c["ink3"]}">'
             f'EFFICIENT AI · ML SYSTEMS · RECURSIVE SELF-IMPROVEMENT</text>')
    s.append(f'<text class="sans" x="58" y="156" font-size="64" font-weight="700" letter-spacing="-2.5" fill="{c["ink"]}">zxr-creator</text>')
    b = f'fill="{c["ink"]}" font-weight="600"'
    a = f'fill="{c["accent"]}" font-weight="600"'
    s.append(f'<text class="sans" font-size="19.5" fill="{c["ink2"]}">'
             f'<tspan x="60" y="204">I make AI cheaper to run: <tspan {b}>efficient models</tspan>, the <tspan {b}>systems</tspan></tspan>'
             f'<tspan x="60" y="233">that serve them on real GPUs, and <tspan {a}>AI agents</tspan> that build</tspan>'
             f'<tspan x="60" y="262">and optimize those systems themselves.</tspan></text>')
    chips = [("efficient model architecture", 60, 230, False), ("ml systems", 300, 100, False),
             ("recursive self-improvement", 410, 214, True)]
    for label, x, w, acc in chips:
        fill, stroke, ink = (c["soft"], c["accent"], c["accent"]) if acc else (c["surface2"], c["line2"], c["ink2"])
        s.append(f'<rect x="{x}" y="286" width="{w}" height="26" rx="13" fill="{fill}" stroke="{stroke}" stroke-opacity="{0.55 if acc else 1}"/>')
        s.append(f'<text class="mono" x="{x + w/2}" y="303.5" font-size="12" text-anchor="middle" fill="{ink}">{label}</text>')
    s.append(f'<text class="mono" x="60" y="352" font-size="12.5" fill="{c["ink3"]}">research intern · CMU InfiniAI Lab  ·  '
             f'Rice University  ·  Pittsburgh, PA</text>')

    # right: window
    X, Y, WW, WH = 688, 38, 472, 324
    s.append(f'<rect x="{X}" y="{Y}" width="{WW}" height="{WH}" rx="14" fill="{c["surface"]}" stroke="{c["line"]}"/>')
    s.append(f'<path d="M{X} {Y+36}V{Y+14}a14 14 0 0 1 14-14H{X+WW-14}a14 14 0 0 1 14 14V{Y+36}z" fill="{c["surface2"]}"/>')
    s.append(f'<line x1="{X}" y1="{Y+36}" x2="{X+WW}" y2="{Y+36}" stroke="{c["line"]}"/>')
    for k in range(3):
        s.append(f'<circle cx="{X+20+16*k}" cy="{Y+18}" r="5" fill="{c["line2"]}"/>')
    s.append(f'<text class="mono" x="{X+72}" y="{Y+22}" font-size="12" fill="{c["ink3"]}">~/research/efficient-ai × rsi</text>')
    s.append(f'<rect x="{X+WW-58}" y="{Y+8}" width="46" height="20" rx="10" fill="none" stroke="{c["green"]}" stroke-opacity="0.45"/>')
    s.append(f'<circle class="pulse" cx="{X+WW-47}" cy="{Y+18}" r="3" fill="{c["green"]}"/>')
    s.append(f'<text class="mono" x="{X+WW-39}" y="{Y+22}" font-size="11" fill="{c["green"]}">live</text>')
    s.append(f'<rect x="{X+1}" y="{Y+37}" width="{WW-2}" height="{WH-38}" rx="0" fill="url(#dots)"/>')
    s.append(f'<line x1="{X+236}" y1="{Y+52}" x2="{X+236}" y2="{Y+WH-14}" stroke="{c["line"]}"/>')

    # pane A: block-sparse attention
    ax, ay, cell, gap, n = X + 22, Y + 76, 10, 2, 16
    s.append(f'<text class="mono" x="{X+18}" y="{Y+60}" font-size="11" fill="{c["ink3"]}">block-sparse attention</text>')
    static, frames = sparse_frames(n)
    for i in range(n):
        for j in range(n):
            x, y = ax + j * (cell + gap), ay + i * (cell + gap)
            if j > i:
                continue
            else:
                acc = (i, j) in static
                s.append(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="2" '
                         f'fill="{c["accent"] if acc else c["t2"]}" fill-opacity="{1 if acc else 1}" '
                         f'stroke="{c["accent"] if acc else c["line2"]}" stroke-opacity="{0.0 if acc else 1}"/>')
    span = n * (cell + gap) - gap
    s.append(f'<path d="M{ax+cell+gap} {ay}H{ax+span}V{ay+span-cell-gap}Z" fill="none" stroke="{c["line2"]}" stroke-dasharray="3 4"/>')
    s.append(f'<text class="mono" x="{ax+span-4}" y="{ay+14}" font-size="9.5" text-anchor="end" fill="{c["ink3"]}">masked</text>')
    total = n * (n + 1) // 2
    for k, fr in enumerate(frames, 1):
        s.append(f'<g class="f f{k}">')
        for (i, j) in sorted(fr):
            x, y = ax + j * (cell + gap), ay + i * (cell + gap)
            s.append(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="2" fill="{c["accent"]}" fill-opacity="0.6"/>')
        s.append(f'<text class="mono" x="{X+18}" y="{Y+292}" font-size="11" fill="{c["ink2"]}">'
                 f'reads {len(static) + len(fr)}/{total} KV blocks ({round(100*(len(static)+len(fr))/total)}%)</text>')
        s.append('</g>')
    s.append(f'<text class="sans" x="{X+18}" y="{Y+310}" font-size="12" font-weight="600" fill="{c["accent"]}">'
             f'compute only what matters</text>')

    # pane B: agent iterations vs reference (schematic curve, real endpoint)
    bx0, bx1, by0, by1 = X + 262, X + 446, Y + 84, Y + 250
    s.append(f'<text class="mono" x="{X+254}" y="{Y+60}" font-size="11" fill="{c["ink3"]}">agent-built server vs vLLM</text>')
    vals = [0.55, 1.05, 1.8, 2.5, 3.3, 4.15, 4.87]
    yv = lambda v: by1 - (v / 5.2) * (by1 - by0)
    xs = [bx0 + k * (bx1 - bx0) / 6 for k in range(7)]
    d = f"M{xs[0]:.1f} {yv(vals[0]):.1f}"
    for k in range(1, 7):
        d += f" H{xs[k]:.1f} V{yv(vals[k]):.1f}"
    area = d + f" V{by1} H{xs[0]:.1f} Z"
    s.append(f'<line x1="{bx0}" y1="{by1}" x2="{bx1}" y2="{by1}" stroke="{c["line2"]}"/>')
    s.append(f'<line x1="{bx0}" y1="{yv(1):.1f}" x2="{bx1}" y2="{yv(1):.1f}" stroke="{c["ink3"]}" stroke-dasharray="4 4"/>')
    s.append(f'<text class="mono" x="{bx1}" y="{yv(1)+14:.1f}" font-size="10" text-anchor="end" fill="{c["ink3"]}">vLLM = 1.0×</text>')
    s.append(f'<path class="area" d="{area}" fill="{c["accent"]}" fill-opacity="0.10"/>')
    s.append(f'<path class="draw" d="{d}" pathLength="1" fill="none" stroke="{c["accent"]}" stroke-width="2.2" stroke-linejoin="round"/>')
    for k in range(7):
        s.append(f'<text class="mono" x="{xs[k]:.1f}" y="{by1+15}" font-size="9.5" text-anchor="middle" fill="{c["ink3"]}">v{k}</text>')
    s.append(f'<g class="pop"><circle cx="{xs[-1]:.1f}" cy="{yv(vals[-1]):.1f}" r="4.5" fill="{c["accent"]}"/>'
             f'<text class="sans" x="{xs[-1]-10:.1f}" y="{yv(vals[-1])+5:.1f}" font-size="15" font-weight="700" text-anchor="end" fill="{c["accent"]}">4.87×</text></g>')
    s.append(f'<text class="mono" x="{X+254}" y="{Y+292}" font-size="11" fill="{c["ink2"]}">each version builds the next</text>')
    s.append(f'<text class="sans" x="{X+254}" y="{Y+310}" font-size="12" font-weight="600" fill="{c["accent"]}">v(n+1) &gt; v(n)</text>')
    s.append('</svg>\n')
    return "\n".join(s)


# ------------------------------------------------------------------ research cards
CARDS = [
    dict(num="01", kicker="efficient model architecture", title="Compute less, by design",
         body=["Model and attention designs that skip work",
               "the model never needed: sparse attention for",
               "long-context and block-diffusion decoding,",
               "and redundancy-aware parallel decoding for",
               "diffusion language models."],
         metric="5.53×", m1="faster sparse attention", m2="at 128K context · RISA", tags="RISA · R²-dLLM · Vortex", icon="mask"),
    dict(num="02", kicker="conventional ml systems", title="Make it fast on real GPUs",
         body=["Classic systems work: serving engines,",
               "sequence parallelism, SLO-aware GPU",
               "scheduling and inference pipelines for LLMs",
               "and diffusion models, built and measured",
               "on real clusters, from H200s to PCIe GPUs."],
         metric="3.46×", m1="serving throughput", m2="vs. full attention · Vortex", tags="Vortex · GenServe · SparSP · QRMark", icon="gpu"),
    dict(num="03", kicker="recursive self-improvement", title="Let agents build the system",
         body=["Agents that do systems work themselves:",
               "build LLM serving engines from scratch,",
               "compress models under a storage budget,",
               "write sparse-attention algorithms. I build",
               "the substrates and benchmarks to measure it."],
         metric="4.87×", m1="vs. the vLLM reference", m2="agent-built server · ServerBench", tags="ServerBench · CompressionBench · Vortex", icon="agent", acc=True),
]


def icon(kind, x, y, c):
    out = []
    if kind == "mask":
        for i in range(4):
            for j in range(i + 1):
                on = j == 0 or j == i or (i, j) == (3, 1)
                out.append(f'<rect x="{x + j*9}" y="{y + i*9}" width="7" height="7" rx="1.5" fill="{c["accent"] if on else c["t3"]}"/>')
    elif kind == "gpu":
        out.append(f'<rect x="{x}" y="{y+6}" width="34" height="22" rx="4" fill="none" stroke="{c["ink3"]}" stroke-width="1.5"/>')
        out.append(f'<rect x="{x+7}" y="{y+12}" width="10" height="10" rx="2" fill="{c["accent"]}"/>')
        for k in range(4):
            out.append(f'<line x1="{x+21+k*3.5}" y1="{y+11}" x2="{x+21+k*3.5}" y2="{y+23}" stroke="{c["ink3"]}" stroke-width="1.2"/>')
        for k in range(4):
            out.append(f'<line x1="{x+5+k*7}" y1="{y+28}" x2="{x+5+k*7}" y2="{y+32}" stroke="{c["ink3"]}" stroke-width="1.5"/>')
    else:  # agent: hexagon with rising bars
        out.append(f'<path d="M{x+8} {y+2}h18l8 15-8 15h-18l-8-15z" fill="none" stroke="{c["accent"]}" stroke-width="1.5" stroke-linejoin="round"/>')
        for k, hgt in enumerate([5, 9, 13]):
            out.append(f'<rect x="{x+10+k*5.5}" y="{y+23-hgt}" width="3.6" height="{hgt}" rx="1" fill="{c["accent"]}"/>')
    return "".join(out)


def research(c):
    W, H = 1200, 344
    s = [svg_open(W, H, "Research areas: efficient model architecture, conventional ML systems, recursive self-improvement", c)]
    # brackets
    def bracket(x0, x1, label):
        mid = (x0 + x1) / 2
        return (f'<path d="M{x0} 40V32H{x1}V40" fill="none" stroke="{c["line2"]}"/>'
                f'<rect x="{mid-len(label)*3.9-10}" y="22" width="{len(label)*7.8+20}" height="20" fill="{c["bg"]}"/>'
                f'<text class="mono" x="{mid}" y="36" font-size="12" letter-spacing="1" text-anchor="middle" fill="{c["ink3"]}">{label}</text>')
    s.append(f'<rect width="{W}" height="{H}" fill="{c["bg"]}" fill-opacity="0"/>')
    s.append(bracket(12, 372, "the model"))
    s.append(bracket(420, 1188, "machine learning systems"))
    cw, gap = 384, 24
    for k, cd in enumerate(CARDS):
        x = k * (cw + gap)
        acc = cd.get("acc")
        s.append(f'<rect x="{x+0.5}" y="52.5" width="{cw-1}" height="{H-56}" rx="14" fill="{c["surface"]}" '
                 f'stroke="{c["accent"] if acc else c["line"]}" stroke-opacity="{0.6 if acc else 1}"/>')
        s.append(f'<text class="mono" x="{x+28}" y="88" font-size="12.5"><tspan fill="{c["accent"]}" font-weight="600">{cd["num"]}</tspan>'
                 f'<tspan fill="{c["ink3"]}" dx="10">{cd["kicker"]}</tspan></text>')
        s.append(icon(cd["icon"], x + cw - 64, 70, c))
        s.append(f'<text class="sans" x="{x+28}" y="126" font-size="22" font-weight="700" letter-spacing="-0.5" fill="{c["ink"]}">{cd["title"]}</text>')
        s.append(f'<text class="sans" font-size="14.5" fill="{c["ink2"]}">' +
                 "".join(f'<tspan x="{x+28}" y="{158 + 21*i}">{esc(line)}</tspan>' for i, line in enumerate(cd["body"])) + '</text>')
        s.append(f'<line x1="{x+28}" y1="266" x2="{x+cw-28}" y2="266" stroke="{c["line"]}"/>')
        s.append(f'<text class="sans" x="{x+28}" y="303" font-size="30" font-weight="700" letter-spacing="-1" fill="{c["accent"]}">{cd["metric"]}</text>')
        s.append(f'<text class="mono" font-size="11.5" fill="{c["ink2"]}"><tspan x="{x+130}" y="290">{esc(cd["m1"])}</tspan>'
                 f'<tspan x="{x+130}" y="306" fill="{c["ink3"]}">{esc(cd["m2"])}</tspan></text>')
        s.append(f'<text class="mono" x="{x+28}" y="{H-16}" font-size="11" fill="{c["ink3"]}">{esc(cd["tags"])}</text>')
    s.append('</svg>\n')
    return "\n".join(s)


for name, c in THEMES.items():
    open(f"{OUT}/hero-{name}.svg", "w", encoding="utf-8").write(hero(c))
    open(f"{OUT}/research-{name}.svg", "w", encoding="utf-8").write(research(c))
print("ok")
