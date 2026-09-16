# MSc Artificial Intelligence e-Portfolio

e-Portfolio for the MSc Artificial Intelligence programme at the University of
Essex Online.

**Live site:** <https://aabouraya.github.io/msc-ai-portfolio/>

Built with Jekyll and published by GitHub Pages from the `master` branch — there
is no build pipeline to maintain; pushing to `master` publishes.

## Layout

```
_config.yml                  site config, top nav
_data/modules.yml            module metadata: status, learning outcomes, skills
_layouts/                    default, page, module
_includes/module-cards.html  module card grid, used on Home and Modules
assets/css/style.css         the whole theme (light + dark)
assets/img/<module>/         diagrams and screenshots
index.md  modules/  skills.md  about.md
modules/<module>/            one page per portfolio section
artefacts/<module>/          source code and raw artefacts (not rendered)
```

## Adding content

**A new artefact** — write it up on the relevant module section page, then add a
row to the *Artefact index* table on that module's Overview page stating which
learning outcomes it evidences. The mapping is an assessment requirement, not
decoration.

**A new module** — add an entry to `_data/modules.yml` (slug, title, status,
term, summary, outcomes, skills), then create `modules/<slug>/index.md`. It
appears in the card grids automatically. Copy the seven pages from
`modules/intelligent-agents/` once the module starts.

**A new section page in a module** — set `module: <slug>` and a `nav_order` in the
front matter; the module sub-navigation picks it up and orders by `nav_order`
(`0` is the Overview page).

Module status is one of `in-progress`, `completed` or `not-started`, and drives
the badge shown on the cards.

## Local preview

```sh
bundle install
bundle exec jekyll serve   # http://127.0.0.1:4000/msc-ai-portfolio/
```

Links use the `relative_url` filter throughout so that the `baseurl`
(`/msc-ai-portfolio`) is applied consistently in both local and published builds.
