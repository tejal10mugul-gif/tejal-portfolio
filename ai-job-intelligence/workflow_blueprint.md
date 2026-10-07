# Workflow Blueprint

## Stage 1 — Discover
Collect recent, permitted job information from:
- Official company career pages
- Job boards
- Public professional-network hiring posts
- Other permitted public sources

## Stage 2 — Normalize
Create one consistent record:
company | title | location | experience | source | source_url | application_url | posted_date

## Stage 3 — Clean
- Remove duplicate URLs
- Normalize company names
- Flag missing application routes
- Remove obvious promotional/non-hiring records

## Stage 4 — Match
Use the role-match prompt to assess:
role, skills, experience, consulting relevance, location, source quality and recency.

## Stage 5 — Score
Run `code/opportunity_scoring.js`.

## Stage 6 — Review
Store the shortlist in a spreadsheet and manually verify:
- role is still open
- company/source is legitimate
- requirements are understood
- application route works

## Stage 7 — Analyze
Power BI can be used to track:
- openings by function
- companies hiring
- location mix
- match-score distribution
- applications vs interviews
- source effectiveness

The system supports decision-making; it does not automatically apply for jobs.
