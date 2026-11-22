"""Copy the Heatwave Box Atlas into this website (folder atlas/) and add the site's top bar to it.

Run after rebuilding the atlas (build_dashboard_robinson.py in the atlas repository):

    python update_atlas.py

It copies index.html, details.html and figs/ from the atlas build folder below into atlas/, then adds the top bar,
the introduction and the "coming soon" note. Edit INTRO below to change that text.
"""
import os, re, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.expanduser("~/Work/2025-2026/summer_heat_wave_MPI/Manuscript/Heatwave_atlas/"
                         "Heatwave_Box_Atlas_recreate/2026-11-18/github_pages/heatwave-box-atlas")
DST = os.path.join(HERE, "atlas")

INTRO = """
    <p class="site-intro">An interactive atlas of blocking-driven summer heatwaves in 18 Northern Hemisphere regions, from
      the MPI Grand Ensemble (MPI-ESM1.2-LR, 5 members, historical 1850–2014 and SSP3-7.0 2015–2100, June–August).
      Pick a region on the map to see how often heatwaves occur, what drives them at the surface, and how they are
      projected to change in a warmer world.</p>
    <p class="site-intro"><span class="site-soon">Coming soon:</span> the accompanying paper will be posted here.
      &nbsp;<a href="https://github.com/Pragallva/heatwave-box-atlas" target="_blank" rel="noopener">Code on GitHub →</a></p>
"""

ITEMS = [("../index.html", "Homepage"), ("../index.html#news", "News"), ("../index.html#career", "Career"),
         ("../index.html#publications", "Publications"), ("../projects.html", "Projects"),
         ("index.html", "Heatwave Atlas"), ("../codes.html", "Code")]

HEAD = """<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400&display=swap">
<style>
/* Top bar of pragallva.github.io (same look as the other pages). */
body { margin: 0; }
.site-nav { position: sticky; top: 0; z-index: 50; background: var(--panel); border-bottom: 1px solid var(--rule);
  font-family: Roboto, "Helvetica Neue", Arial, sans-serif; font-weight: 300; }
.site-nav .in { max-width: 880px; margin: 0 auto; padding: 0 16px; min-height: 56px; display: flex; align-items: center;
  justify-content: space-between; gap: 12px; flex-wrap: wrap; }
.site-nav a { color: var(--ink); text-decoration: none; }
.site-nav a:hover, .site-nav a.on { color: #b509ac; }
:root[data-theme="dark"] .site-nav a:hover, :root[data-theme="dark"] .site-nav a.on { color: #2698ba; }
.site-nav .brand { font-size: 1.5rem; white-space: nowrap; }
.site-nav ul { display: flex; align-items: center; flex-wrap: wrap; gap: 4px 13px; margin: 0; padding: 0; list-style: none; }
.site-nav ul a { font-size: 0.98rem; white-space: nowrap; }
.site-nav button { background: none; border: 0; padding: 4px; cursor: pointer; color: var(--ink); display: inline-flex; }
.site-nav svg { width: 18px; height: 18px; fill: currentColor; }
@media (max-width: 900px) { .site-nav .in { justify-content: center; padding: 8px 16px; }
  .site-nav .brand { width: 100%; text-align: center; } .site-nav ul { justify-content: center; } }
.site-intro { max-width: 900px; margin: 6px 0 0; font-size: 16px; }
.site-soon { color: #b509ac; }
</style>
<script>
  try { var t = localStorage.getItem("theme"); if (t) document.documentElement.dataset.theme = t; } catch (e) {}
</script>
</head>"""

def nav():
    on = ' class="on"'
    li = "".join(f'      <li><a{on if label == "Heatwave Atlas" else ""} href="{href}">{label}</a></li>\n'
                 for href, label in ITEMS)
    return f"""<body>
<div class="site-nav"><div class="in">
    <a class="brand" href="../index.html">Pragallva Barpanda</a>
    <ul>
{li}      <li><button id="site-theme" aria-label="Switch light/dark mode" title="Switch light/dark mode">
        <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>
      </button></li>
    </ul>
</div></div>"""

TOGGLE = """<script>
  document.getElementById("site-theme").addEventListener("click", function () {
    var root = document.documentElement;
    var dark = root.dataset.theme ? root.dataset.theme === "dark" : window.matchMedia("(prefers-color-scheme: dark)").matches;
    root.dataset.theme = dark ? "light" : "dark";
    try { localStorage.setItem("theme", root.dataset.theme); } catch (e) {}
  });
</script>
</body>"""

def patch(name, intro=False):
    s = open(os.path.join(SRC, name)).read()
    s = s.replace("</head>", HEAD, 1).replace("<body>", nav(), 1).replace("</body>", TOGGLE, 1)
    s = s.replace("<title>Heatwave Box Atlas", "<title>Heatwave Atlas · Pragallva Barpanda", 1)
    if intro:
        s = re.sub(r'(<a class="more" href="details.html">[^<]*</a>)', lambda m: m.group(1) + INTRO, s, count=1)
    open(os.path.join(DST, name), "w").write(s)

os.makedirs(DST, exist_ok=True)
patch("index.html", intro=True)
patch("details.html")
shutil.rmtree(os.path.join(DST, "figs"), ignore_errors=True)
shutil.copytree(os.path.join(SRC, "figs"), os.path.join(DST, "figs"))
print("Atlas copied to", DST)
