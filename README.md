# Astrovastu Rashi Predictions — Shri V M Joshi

A bilingual (Kannada + English) astrology website that displays monthly Rashi (zodiac) predictions for all 12 signs.

## Overview

This is a static, two-page website built for **Shri V M Joshi**, a Vastu consultant and astrologer. It allows users to select their Rashi and read detailed monthly predictions in both Kannada and English.

This website is a monthly astrology prediction platform designed primarily for Kannada-speaking users who follow traditional Vedic astrology. Visitors can select one of the 12 Rashis (zodiac signs) from the home page and instantly read a detailed forecast for the current month covering key areas of life — career, finances, family, health, personal growth, and spiritual remedies — all presented in both Kannada and English. The site is built around the guidance of Shri V M Joshi, a Vastu expert and astrologer, whose profile anchors the home page. Beyond reading predictions, users are encouraged to book a personal consultation through a promotional popup, making the site both an informational resource and a lead generation tool for Shri Joshi's practice.

## Pages

| File | Purpose |
|---|---|
| `index.html` | Home page — hero section with astrologer profile and a 12-Rashi selection grid |
| `rashi.html` | Prediction detail page — dynamically loads content for the selected Rashi from `data.json` via URL query param (`?rashi=mesha`) |

## Data

All prediction content lives in `data.json`. Each Rashi entry contains the following sections, with `_en` (English) and `_kn` (Kannada) variants:

- `month` — current prediction month
- `intro` — overview for the month
- `career` — career & professional life
- `finance` — financial outlook
- `family` — family & relationships
- `health` — health guidance
- `growth` — overall growth summary
- `remedy` — spiritual remedies (mantras, rituals)
- `conclusion` — lucky color, number, and day

## Assets

```
assets/
  css/style.css      — All styles (cosmic navy theme, gold accents, Kannada font)
  img/
    sachin3.jpg      — Astrologer portrait
    rashis/          — Icon images for each of the 12 Rashis
```

## Rashis Covered

Mesha, Vrishabha, Mithuna, Karka, Simha, Kanya, Tula, Vrischika, Dhanu, Makara, Kumbha, Meena

## Tech Stack

- Plain HTML, CSS, vanilla JavaScript (no frameworks or build tools)
- Google Tag Manager (GTM-NNVPDXCS)
- Meta Pixel (ID: 1952801472042069) for Facebook tracking
- Google Fonts — Anek Kannada (Kannada text), English headings

## How It Works

1. User lands on `index.html` and clicks a Rashi card.
2. Browser navigates to `rashi.html?rashi=<name>`.
3. JavaScript reads the query param, fetches `data.json`, and renders the prediction sections.
4. A consultation booking popup is shown to encourage users to book a session with Shri V M Joshi.

## Running Locally

No build step required. Open `index.html` directly in a browser, or serve with any static file server:

```bash
npx serve .
```
