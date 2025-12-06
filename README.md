# Big Data Final Project – Netflix Titles

## Overview
This project uses **Microsoft Fabric** and **Power BI** to analyse the Netflix titles dataset (movies and TV shows).  
It demonstrates data ingestion, cleaning, SQL analysis, and dashboard creation.

## Tools Used
- Microsoft Fabric (Lakehouse, Notebook, SQL endpoint)
- PySpark
- Power BI (dashboard linked to Lakehouse)
- Git & GitHub

## Dataset
- **Source:** Netflix Movies and TV Shows dataset (Kaggle)
- **Main columns:**
  - `Title` – name of the show or movie
  - `Type` – Movie or TV Show
  - `country` – main production country
  - `data_added` – date added to Netflix
  - `release_year` – year of original release
  - `rating` – maturity rating (TV-MA, PG-13, etc.)
  - `duration` / `duration_int` – duration in minutes or number of seasons
  - `listed_in` – genre/category

## Steps

### 1. Ingestion (Fabric Lakehouse)
- Uploaded the raw CSV into a Fabric Lakehouse.
- Created the raw table `netflix_raw`.

### 2. Cleaning (Fabric Notebook with PySpark)
- Converted `release_year` to integer.
- Converted `data_added` to proper date.
- Created `duration_int` from the text `duration` field.
- Removed rows with invalid `Type` values (kept only **Movie** and **TV Show**).
- Saved the cleaned data as `netflix_clean`.

### 3. Analysis (Notebook + SQL)
- Used PySpark to explore:
  - Number of titles by `Type`.
  - Top countries by number of titles.
  - Titles added per year.
- Wrote SQL queries on `netflix_clean` such as:
  - Movies vs TV Shows count.
  - Top 10 countries by number of titles.
  - Number of titles added per year.

### 4. Dashboard (Power BI)
Dashboard is built in Power BI and linked to the cleaned data.  
It includes:
- **Bar chart:** Number of Movies vs TV Shows
- **Bar chart:** Top 10 Countries by Number of Titles
- **Line chart:** Count of Title by data_added

All visuals have clear titles and are part of one main report.

## Files in This Repository
- `Netflix_Dashboard.pbix` – Power BI report / dashboard.
- `fabric_notebook.ipynb` (or `.py`) – Fabric notebook with PySpark cleaning and analysis.
- `queries.sql` – SQL analytical queries on `netflix_clean`.
- `dashboard.png` – Screenshot of the final dashboard (optional).

## How to Run
1. Open `fabric_notebook.ipynb` in Microsoft Fabric (or Jupyter) to see the data preparation steps.
2. Open `Netflix_Dashboard.pbix` in Power BI Desktop to view and interact with the dashboard.
