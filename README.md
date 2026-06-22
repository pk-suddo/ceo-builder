# CEO Builder

A single-file progress tracker for CEOs learning technical architecture — built to run locally with zero setup and persist progress across all browsers on your machine.

## What it tracks

- **CEO Role** — Sales, Unit Economics, Leadership, Vision tasks scheduled day-by-day across 4 weeks
- **Tech Architecture** — Architecture, n8n, AI/ML, Codebase, Scaling knowledge tasks
- **Learning notes** — capture insights per task, shown inline on cards and in the sidebar
- **Dashboard** — overall progress rings, pillar breakdowns, weekly progress bars, streak counter

## Features

- Day tabs (Mon–Fri + Ongoing) to focus on what's scheduled today
- Pillar accordions with per-pillar colors and progress rings
- Task cards in grid layout with status cycling (Not Started → In Progress → Done)
- Learning modal — lightweight note capture per task
- Today's Focus view — cross-track view of today's tasks
- Dark / light mode toggle
- Export / Import JSON for backups
- Cross-browser auto-save via local file server

## Run locally

```bash
python3 server.py
```

Then open **http://localhost:4200/tracker.html** in any browser.

Progress is saved to `state.json` on disk — open the same URL in Chrome, Safari, or Firefox and they all stay in sync automatically.

## Stack

- Vanilla HTML + CSS + JavaScript (no build step)
- Tailwind CSS via CDN
- Chart.js for trend charts
- canvas-confetti for completion celebrations
- Python `http.server` extended with a `/api/state` REST endpoint for persistence

## Files

| File | Description |
|------|-------------|
| `tracker.html` | The entire app — open this in a browser |
| `server.py` | Local server with state persistence API |
| `state.json` | Your saved progress (gitignored, auto-created) |
