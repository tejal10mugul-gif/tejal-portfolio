# Oncology Commercial Forecasting Model
## Model methodology, assumptions, controls and interpretation

**Workbook:** [Oncology Forecasting.xlsx](../../proof-of-work/ai-competitive-intelligence-studio/Oncology%20Forecasting.xlsx)  
**Model type:** Patient-based commercial forecast  
**Forecast horizon:** Through 2030, as described in the portfolio  
**Status:** Independent learning and training work sample — not a client deliverable

---

## 1. Executive summary

This workbook is designed to connect an oncology patient population to a commercial sales outlook through a sequence of epidemiology, disease-progression, eligibility, treatment and sales calculations. Its value is the traceability of the calculation chain: a commercial output should be explainable by the patient pool, treatment assumptions and revenue logic that produce it.

The workbook contains five main sheets: `Input`, `Calc.1`, `Calc. 2`, `Cancer Disease Progression` and `Forecasting Sheet`. The documentation below describes their intended analytical roles. Exact formula-level behavior, numeric outputs and source provenance should be confirmed in the workbook before they are quoted externally.

### Questions this model is intended to support

- How does the modeled disease population translate into a potentially treatable patient pool?
- Which diagnosis, progression, eligibility and uptake assumptions control the number of treated patients?
- How are treated patients converted into annual sales?
- Which assumptions should be tested before using the forecast to inform a commercial decision?

---

## 2. Model architecture

| Layer | Workbook sheet(s) | Analytical purpose | Key review question |
|---|---|---|---|
| Assumptions | `Input` | Holds population, epidemiology and commercial inputs | Is each input defined, sourced, dated and unit-labelled? |
| Intermediate calculations | `Calc.1`, `Calc. 2` | Converts the inputs into intermediate rates and patient counts | Can every calculation be traced to a documented input? |
| Disease progression | `Cancer Disease Progression` | Represents the relevant patient population and progression logic | Are stage definitions, timing and patient flows consistent? |
| Commercial forecast | `Forecasting Sheet` | Translates the modeled patient pool into a sales outlook | Are eligible and treated patients linked to price and treatment assumptions correctly? |

**Conceptual flow**

`Population / epidemiology inputs → disease and diagnosis logic → eligible patients → treated patients → annual sales`

This is a conceptual map, not a claim that every step is already implemented as a separate formula in the workbook. Confirm the live cell formulas and dependencies during model review.

---

## 3. Methodology: from population to sales

### Step 1 — Define the population

Establish the geography, indication, patient definition and forecast period. Distinguish incidence (new cases over a period) from prevalence (people living with a disease at a point or over a period). These measures are not interchangeable and should not be added together without a clear cohort method.

**Required documentation:** geography, year, epidemiology measure, unit, source, publication date and any adjustment applied.

### Step 2 — Apply disease and diagnosis logic

Use the model's disease-progression calculations to estimate the relevant patient pool. Define stage or progression categories explicitly and state whether the model follows a new-patient cohort, an existing prevalent pool or a combination.

Patient flows should be mutually exclusive where appropriate. If patients can move between stages over time, the model should avoid counting the same person twice in a single-period total.

### Step 3 — Estimate the eligible population

Apply clinically and commercially relevant filters only where they are supported by the indication and model scope. These may include diagnosis, disease stage, biomarker status, line of therapy, contraindications, access or other eligibility criteria.

The output at this stage is a **modeled eligible population**, not automatically the total addressable market and not a clinical estimate unless the inputs and definitions are validated.

### Step 4 — Estimate treated patients

Convert eligible patients into treated patients using the model's uptake or penetration assumptions. If the workbook includes launch timing, treatment duration, persistence, market share or line-of-therapy assumptions, document how each affects annual treated-patient counts.

A useful conceptual relationship is:

`Treated patients = Eligible patients × treatment penetration`

Use this only where the model's actual formula and patient definitions support it. If treatment duration, patient turnover or cohort carryover is modeled, the calculation may need additional terms.

### Step 5 — Convert treatment into sales

Sales should be traceable to treated patients and the commercial assumptions used in the workbook. Depending on the model design, the conversion may require treatment duration, dosing, price per unit, units per patient, gross-to-net adjustments, market share or other factors.

A simplified conceptual relationship is:

`Sales = Treated patients × revenue per treated patient`

This is not a substitute for checking the workbook's actual formula. Document the currency, price year, gross/net basis, dosing or duration logic and any adjustments before interpreting the result.

### Step 6 — Review the forecast

Review the annual patient and sales trends together. Commercial outputs should be read alongside the assumptions that create them, not as a standalone prediction. Once outputs are verified, useful summary metrics include annual treated patients, annual sales, peak sales and peak year, cumulative sales and scenario differences.

**No numeric peak-sales figure or patient count is published in this documentation** because the outputs and their units, price basis and source assumptions must first be checked directly against the workbook.

---

## 4. Assumption register

The `Input` sheet should be accompanied by an assumption register with one row per input.

| Field | What to record |
|---|---|
| Assumption name | Clear, unambiguous label |
| Definition | What the variable measures and what it excludes |
| Value and unit | Include %, patients, years, currency or other unit |
| Year / geography | Period and market to which the value applies |
| Source and publication date | Direct citation or source URL, plus access/publication date |
| Type | External fact, derived value or illustrative assumption |
| Rationale | Why the value is appropriate for this model |
| Low / base / high | Plausible scenario values, where relevant |
| Owner / review status | Who checked the input and whether it is validated |

If a value is illustrative, label it as such. Do not present an unsourced workbook input as an industry fact. Clinical evidence, regulatory facts and commercial assumptions should be separated rather than blended into one confidence level.

---

## 5. Scenario and sensitivity framework

A decision-ready forecast should test uncertainty instead of relying on a single point estimate. The following are recommended scenario definitions; they should be implemented only after the base-case inputs and formulas have been verified.

| Driver | Downside case | Base case | Upside case |
|---|---|---|---|
| Diagnosed / eligible population | Lower conversion | Documented central assumption | Higher conversion supported by rationale |
| Launch timing / access | Delay or slower access | Expected timing | Faster access where defensible |
| Uptake / penetration | Slower ramp | Central uptake curve | Faster ramp with rationale |
| Treatment duration / persistence | Shorter duration | Central assumption | Longer duration if evidence supports it |
| Realized price | Lower net price | Documented price basis | Higher realized price only if justified |

Run one-way sensitivity tests on the most material drivers first, then consider combined scenarios. Report the change versus base case in both absolute terms and percentage terms. Avoid implying that scenario outputs are probabilities unless a probability framework has been built.

---

## 6. Model validation and quality controls

Before using the forecast in an interview, portfolio discussion or business decision, perform and record these checks.

### Input and formula checks
- Confirm units, time periods, geographies and definitions are consistent across sheets.
- Trace key outputs back through all linked cells to the original assumptions.
- Identify hard-coded overrides, broken references, hidden adjustments and formula inconsistencies.
- Confirm whether the model uses incidence, prevalence, cohorts or a combination.

### Patient-flow checks
- Patient counts are non-negative and rates/proportions fall within their defined bounds.
- Stage totals and transitions reconcile to the stated patient-flow logic.
- No patient group is double-counted across stages, lines of therapy or annual periods.
- Eligible patients do not exceed the relevant upstream population without a documented reason.
- Treated patients reconcile to eligible patients and the modeled penetration definition.

### Commercial checks
- Price, currency, price year, dosing, treatment duration and gross/net basis are explicit.
- Annual sales reconcile to treated patients and the workbook's actual revenue formula.
- Launch timing and ramp assumptions are consistent with the forecast years.
- Units are consistent throughout; patient counts must not be multiplied by a price measure with incompatible units.

### Output checks
- Review annual patient and sales trends for unexpected jumps or discontinuities.
- Confirm peak sales, peak year and cumulative sales from workbook outputs before publishing them.
- Keep a dated record of model version, key assumptions and validation status.

---

## 7. Interpretation for commercial strategy

The model can help structure commercial questions, but the answer depends on the quality of the assumptions and implementation.

- **Opportunity sizing:** The most useful population is the clearly defined eligible pool, not total disease prevalence alone.
- **Forecast drivers:** Separate population conversion from uptake and revenue-per-patient effects to see what actually moves the sales curve.
- **Launch planning:** Explicit launch timing and a documented uptake curve are more interpretable than an unexplained growth rate.
- **Evidence priorities:** Sensitivity analysis can identify which assumptions need better epidemiology, clinical, access or pricing evidence.
- **Governance:** A traceable assumption register and formula audit make the forecast easier to review, update and explain.

### Recommended output dashboard

Once the workbook is validated, summarize:
1. Eligible patients by year.
2. Treated patients by year.
3. Annual sales and cumulative sales.
4. Peak sales and peak year.
5. Downside / base / upside comparison.
6. Sensitivity ranking of the key assumptions.
7. Data-source coverage and validation status.

---

## 8. Limitations and appropriate use

This page documents the intended model logic and a review framework; it does **not** certify that every listed control or scenario is already implemented in the workbook. Exact formulas, values, sources and scenario outputs need to be verified against the file.

This is an independently prepared commercial and pharma forecasting learning/training work sample, not a client deliverable. It is not medical advice and should not be used for clinical, investment or real-world commercial decisions without appropriate source validation and independent review.

**Workbook:** [Open Oncology Forecasting.xlsx](../../proof-of-work/ai-competitive-intelligence-studio/Oncology%20Forecasting.xlsx)  
**Case study:** [Return to Oncology Forecasting case study](index.html)
