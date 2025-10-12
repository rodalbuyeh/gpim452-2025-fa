---
layout: page
title: Feature Store
description: Reference datasets for ZIP code–level enrichment.
nav_order: 8
---

# 🗂️ Feature Store

Use these datasets to enrich records that include ZIP or ZCTA information. Each source includes a download link and notes on usage.

---

## 📍 Geographic Reference

**U.S. Census ZCTA Shapefiles**  
- [Download (TIGER/Line)](https://www.census.gov/programs-surveys/geography/guidance/geo-areas/zctas.html)  
- Polygon boundaries for ZIP Code Tabulation Areas (ZCTAs).  
- Use for spatial joins, mapping, and area aggregation.

**HUD–USPS ZIP Crosswalk**  
- [HUD Crosswalk Files](https://www.huduser.gov/portal/datasets/usps_crosswalk.html)  
- Maps ZIPs to census tracts, counties, CBSAs.  
- Useful when allocating metrics across geographies.


---

## 💰 Demographic and Economic Data

**IRS ZIP-Code Data**  
- [IRS SOI ZIP-Code Statistics](https://catalog.data.gov/dataset/zip-code-data)  
- Income, returns, and filer counts by ZIP.

**Row Zero ZIP Demographics**  
- [Demographics by ZIP](https://rowzero.io/datasets/demographics-by-zip-code)  
- Race, age, and income summaries. Verify recency.

**SimpleMaps ZIP Database**  
- [SimpleMaps US ZIP Codes](https://simplemaps.com/data/us-zips)  
- CSV with location, population, time zone, and county.

---

## 🧭 Notes

- **ZIP vs ZCTA:** USPS ZIPs are routing designations; ZCTAs are Census approximations for area joins.  
- **Boundary overlap:** ZIPs may span multiple counties or states. Use crosswalks for proportional allocation.  
- **Updates:** ZIP codes change annually. Check each data source for current version numbers.  
- **Licensing:** Verify terms before redistribution.

---