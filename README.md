# alexistsui94.github.io

A personal site by Alexis Tsui, with notes on **ERP implementation, project delivery, AI tools and code**.

The site is **English-first**. Articles are written in plain English with sense-group pauses marked (`/` for a short pause, `//` for a longer one), and a Chinese reference line beneath each English passage. Readers can hide the Chinese lines for listen → shadow → retell practice.

The pause marks belong to English only. Chinese reference lines are written as ordinary Chinese prose — no sense-group splitting, and no attempt to mirror the English clause boundaries with commas or semicolons. Project pages carry no pause marks in either language; they are meant to be read, not shadowed.

## Structure

- `/` — home, with selected writing
- `/notes/` — all published articles, newest first
- `/tech/` — AI & Code
- `/projects/` — ERP & Delivery, plus the food-label AI case study
- `/about/` — background and how the articles are written

Only two topic sections remain. Articles that are not about ERP, AI or code are kept in the repository with `published: false`, so nothing is deleted and they can be restored by removing that line. Every published article keeps its original URL (`permalink: /:categories/:title/`).

## Layout

The visual style follows a plain text-first blog: no cards, no bordered blocks, no rounded corners, no background panels. Hierarchy comes from 1px rules and spacing; text links use a 1px underline; headings use system serif fonts and body text uses system sans-serif fonts. Colors stay warm white and low-saturation moss green.

Built as a lightweight Jekyll site for GitHub Pages, with custom layouts and no theme dependency. All pages share a single stylesheet: `assets/css/site.css`.
