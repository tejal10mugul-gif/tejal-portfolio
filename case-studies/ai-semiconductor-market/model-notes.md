# AI Semiconductor Market — Model Documentation

**Owner:** Tejal Mugul  
**Artifact:** `AI Semiconductor Market.xlsx`  
**Scope:** United States; annual model from 2020–2031  
**Status:** Independent portfolio work sample; not externally validated

## Purpose
Estimate an annual top-line market series and allocate it across technology, deployment, product, services and end-user segments using explicit year-by-year share assumptions.

## Workbook structure
The workbook contains one sheet, `Sizing`.

- **Top-line series (row 7):** 2020 starts at 4,435 and rises by 2,217 each year to 28,822 in 2031.
- **Year-on-year growth (row 8):** calculated as current-year value divided by prior-year value, minus one.
- **Segment calculations (rows 10–13, 15–17, 19–21, 23–26, 28–30):** segment value equals the annual top-line estimate multiplied by the corresponding year-specific share.
- **Share assumptions (columns S:AD):** annual segment-share inputs. Residual categories are calculated as 100% minus the other category shares.
- **CAGR cells (column P):** use Excel `RATE` calculations over the selected four-year interval (2027–2031).

## Key model observations
1. Top-line values increase by a constant 2,217 workbook units per year. This is a linear absolute-growth construction.
2. The implied YoY growth rate declines from approximately 50.0% in 2021 to 8.3% in 2031.
3. The 2027–2031 top-line CAGR calculated from the model values is approximately 9.63%.
4. Modelled 2031 shares versus 2020: Machine Learning 26.2% vs 25.0%; Deep Learning 17.3% vs 16.0%; NLP 28.6% vs 31.0%; Computer Vision is the residual.
5. Hybrid deployment remains the largest assumed deployment category (about 53.9% in 2031); services remain the largest product category (about 56.3%); Integrated Device Manufacturers remain the largest end-user category (about 61.4%).

## Important caveats
- The workbook does **not** state a unit/currency for the top-line figures. Do not label them as USD, USD millions or market revenue until confirmed.
- Source URLs, publication dates, methodology and actual-versus-forecast cut-off are not documented in the workbook. These are required before presenting the numbers as external market facts.
- Segment shares are model assumptions. They should be traced to sources or explicitly retained as scenarios.
- The constant annual increment should be compared with at least one compound-growth forecast and a downside/upside range.
- Validate that segment shares sum to 100% for each year and that segment values reconcile to the total.

## Recommended validation checklist
- [ ] Define the market boundary and value chain.
- [ ] Add source, source date, unit and notes for every key input.
- [ ] Separate historical observations from forecast years.
- [ ] Add conservative/base/upside scenarios.
- [ ] Reconcile every segment to the total and check share totals.
- [ ] Add charts for top-line trend and segment mix.
- [ ] Record model version and last updated date.

## Decision-use conclusion
The current file is useful as a transparent segmentation and forecasting scaffold. It is not yet suitable for a client-facing market-size claim until unit, data provenance and assumptions are validated.
