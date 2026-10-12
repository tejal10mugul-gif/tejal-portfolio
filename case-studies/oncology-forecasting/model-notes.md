# Oncology Sales Forecasting Model — Documentation

**Workbook:** `Oncology Forecasting.xlsx`  
**Sheets:** `Input`, `Calc.1`, `Calc. 2`, `Cancer Disease Progression`, `Forecasting Sheet`  
**Horizon described in portfolio:** Through 2030  
**Status:** Independent learning/training work sample; not a client deliverable

## Objective
Create a transparent, patient-based commercial forecast that connects epidemiology and disease progression to eligible patients, treated patients and projected product sales.

## Model flow
1. **Input:** Store clinical, population and commercial assumptions with units, source, publication date, and rationale.
2. **Calc.1 / Calc. 2:** Transform input assumptions into intermediate patient counts and rates.
3. **Cancer Disease Progression:** Model the relevant disease population and progression logic. Document stage definitions and avoid double-counting.
4. **Forecasting Sheet:** Convert the eligible/treated patient pool into forecast sales using the model's commercial assumptions.

## Business interpretation
- The forecast should be interpreted as a linked chain of assumptions, not as a standalone sales prediction.
- The addressable patient population must be defined after diagnosis and eligibility constraints, not inferred from total prevalence alone.
- Treatment penetration, launch timing, duration/persistence and price can materially alter the sales curve.
- The model becomes more decision-useful when peak sales, peak year, treated patients, cumulative sales and sensitivity results are shown together.

## Validation required before external use
- Add source, source date, unit and rationale for each epidemiology and commercial assumption.
- Verify formulas and cross-sheet references; identify any hard-coded overrides.
- Document treatment line, eligible population definition, launch date and forecast cut-off.
- Define price basis (gross/net), currency, dosing, duration and any adjustment factors that are included.
- Add downside/base/upside scenarios and one-way sensitivity analysis.
- Check patient counts are non-negative; proportions are within valid ranges; patient stages reconcile; and sales outputs reconcile to patients × price/duration logic.
- Verify numeric outputs from the workbook before quoting peak sales, peak year or patient counts in public-facing materials.

## Suggested scenario design
- **Downside:** slower diagnosis/access, lower eligible share or uptake, launch delay, lower realized price.
- **Base:** central documented assumptions.
- **Upside:** stronger diagnosis/access or uptake, where supported by clinical and commercial rationale.

## Portfolio disclosure
This is a learning/training work sample. It is not a client deliverable and should not be used for real-world medical, investment or commercial decisions without independent validation.
