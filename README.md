# mesmatters.com

Source for the MES Matters website: a small static site built with Python and deployed to GitHub Pages.

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
