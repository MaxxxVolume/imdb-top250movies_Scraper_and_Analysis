# IMDb Top 250 Analysis

I wanted to know if the "Top 250" movies are actually good or just hyped, so I wrote a script to find out.

This repo contains a custom scraper (because the CSVs online were outdated) and a full analysis of the data.

## ⚡ TL;DR (What I found)

- **Recency Bias is crazy:** Most "best" movies are from the last 20 years.
- **Length wins:** Longer movies don't get better ratings, but they get way more votes.
- **Hidden Gems:** The highest-rated movies with low vote counts are almost all international (non-Hollywood).

## 📂 The Files

- `IMDb_Scraper.ipynb` -> The script. Scrapes live data, cleans it, and handles the "2h 45m" string conversion.
- `imdb_analysis.ipynb` -> The findings. Charts for trends, ratings, and runtimes.
- Cleaned data ready for the next step (ML).

## 🌌 The Path

- [x] Scraper
- [x] Analysis
- [x] ML Model (Random Forest) 
