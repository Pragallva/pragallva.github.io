# pragallva.github.io

Personal homepage of Pragallva Barpanda: https://pragallva.github.io

Plain HTML, no build step:

- `index.html`: homepage (intro, news, career, publications)
- `projects.html`: projects (animations in `img/projects/`)
- `atlas/`: the Heatwave Box Atlas (`index.html`, `details.html`, `figs/`), with this site's top bar
- `codes.html`: code
- `style.css`: shared styles; `img/`: photo, banner and figures
- `atlas.html`: old address, forwards to `atlas/`

To update, edit the files, commit and push to `master`. GitHub Pages serves the `master` branch directly;
`.nojekyll` tells it not to run Jekyll.

## Updating the atlas

- Small text changes: edit `atlas/index.html` or `atlas/details.html` directly.
- After rebuilding the atlas figures (in the heatwave-box-atlas repository), run `python update_atlas.py`.
  It copies the new atlas into `atlas/` and adds the top bar and introduction again (edit `INTRO` in the
  script to change the introduction). Note: this overwrites any direct edits to `atlas/index.html`.

The previous Jekyll (al-folio) version of the site is in the git history and on the `gh-pages` branch.
