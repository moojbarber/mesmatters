# shopfloormatters.com

Source for the Shopfloor Matters website: a small static site built with Python and deployed to GitHub Pages.

## Writing a new article
1. Add `content/posts/<slug>.md` with front matter:
   ```yaml
   ---
   title: "Your headline"
   short: "Short label for nav and cards"
   description: "120-155 character meta description"
   published: 2026-10-20
   category: education   # education | advice | thought-leadership
   art: hexgrid          # see MOTIFS in scripts/art.py
   ---
   ```
2. Run `python scripts/art.py` and `python scripts/og.py` to create its illustration and share card.
3. Push to `main`. The site rebuilds and deploys automatically.

Use `::block <name>` on its own line to drop in an on-brand diagram from `content/blocks/`.

## Scripts
- `scripts/build.py` builds the site into `dist/` (`--base /mesmatters` for the github.io preview).
- `scripts/art.py` generates article illustrations (`public/images/art`).
- `scripts/og.py` renders 1200×630 social share cards (`public/images/og`).
- `scripts/scrape_wix.py` and `scripts/convert_legacy.py` were the one-off import from Wix.

## URLs
Articles keep their original Wix addresses (`/post/<slug>`), so existing links and Google rankings carry over. Old Wix category URLs redirect to the new pages.

## Tools, templates and audience pages

- `content/tools.yaml` lists every tool and template on `/tools/`. Tool data lives in `content/tools/<id>.yaml`; markup in `templates/tools/`; behaviour in `public/js/tools.js`. Answers stay in the visitor's browser (localStorage).
- `content/audiences.yaml` holds the industry and role pages at `/for/<id>`. `content/speaking.yaml` holds `/speaking`.
- The Excel templates in `public/downloads/` are generated: `python scripts/templates_xlsx.py`, then recalculate each file with LibreOffice so the cached values are filled in.

Repository variables (Settings → Secrets and variables → Actions → Variables):

| Variable | What it does | Empty means |
| --- | --- | --- |
| `KIT_FORM_ID` | Newsletter form, template email gates, "email me my result" | Sign-ups hidden; template downloads shown directly |
| `ASK_FORM_ENDPOINT` | Where Ask Matt questions are posted (e.g. Formspree or Tally) | The question is copied and LinkedIn opens |

Kit needs custom fields named `role`, `resource`, `readiness_level`, `readiness_score`, `readiness_weakest` and `readiness_process`, `readiness_data`, `readiness_systems`, `readiness_people`, `readiness_analytics` for the gates and readiness report to carry their data. An automation keyed on `resource` sends the right download link.
