# alexistsui94.github.io

A personal site by Alexis Tsui, with notes on **ERP implementation, project delivery, AI tools and code**.

The site is **English only**. Articles are written in plain English with sense-group pauses marked (`/` for a short pause, `//` for a longer one), so a piece can be read aloud, shadowed and retold. Nothing on the site is written in Chinese; the few Chinese strings that remain inside the food-label case study are product examples (ingredient names, label wording), not translation lines.

## Structure

- `/` — home, with selected writing
- `/notes/` — all published articles, grouped as **ERP**, **AI** and **Other** (`topic` in each post's front matter)
- `/projects/` — projects only: working tools and case studies
- `/about/` — who, where, education, contact
- `/tech/` — retired, redirects to `/notes/#ai`

Every published article keeps its original URL (`permalink: /:categories/:title/`), so `categories` still decides the URL while `topic` decides the group. Articles that are not about ERP or AI are kept in the repository with `published: false`; removing that line publishes them into the Other group.

## Layout

The visual style follows a plain text-first blog: no cards, no bordered blocks, no rounded corners, no background panels. Hierarchy comes from 1px rules and spacing; text links use a 1px underline; headings use system serif fonts and body text uses system sans-serif fonts. Colors stay warm white and low-saturation moss green.

Built as a lightweight Jekyll site for GitHub Pages, with custom layouts and no theme dependency. All pages share a single stylesheet: `assets/css/site.css`.
