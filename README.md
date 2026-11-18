# The World in One Day — 17 November 2026

[![make.fun](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/rayataufik/news-image-17-nov-2026/rank.svg)](https://make.fun/bounty/news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/rayataufik/news-image-17-nov-2026/reward.svg)](https://make.fun/bounty/news-image-20261117)

A one-image summary of the world's news on Tuesday, 17 November 2026, made for the [make.fun](https://make.fun/?ref=vnhxm4py) bounty "Sum up 17 November's world news in one image".

The image is a newspaper front page: a dark masthead names the day in full — TUESDAY, 17 NOVEMBER 2026 — and six stories fill a 2×3 grid, one per region or beat. U.S. strikes on Iran after the Hormuz tanker attacks, Ukraine's hit on the Kerch Bridge, a cascade of outages across banks, flights, Apple and the NSA, NVIDIA's board refusing Jensen Huang's return, Trump's Asia trip for the Xi–Putin summit, and the U.S. losing its measles elimination status — plus a footer noting Robert Pattinson as the next James Bond. Every story is as reported by Reuters, AP, NPR and CNN on the day.

## Files

- `entry.png` — the finished image, 1024×1024 PNG.
- `design.html` — the page the image was rendered from (system fonts only, no external assets), kept so the layout can be inspected and re-rendered.
- `main.py` — the entry program: it copies `entry.png` to the output directory.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

That writes `out/entry.png`, byte-identical to the `entry.png` in this repo. The program needs no network and reads nothing but the image beside it, so running it twice always produces the same bytes.
