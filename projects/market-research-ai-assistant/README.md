# Market Research AI Assistant

A portfolio prototype demonstrating selected Claude Platform 101 concepts in a market research workflow.

## What it does
- Accepts a research brief: industry, geography, company/focus, and research goal.
- Produces structured company-profile and competitor-comparison output.
- Flags research gaps and evidence limitations.
- Exports a JSON report.
- Supports optional Claude API mode when an API key is configured.

## Important limitation
This prototype does **not** perform live web research or verify facts. Demo mode uses explicitly illustrative example companies. Claude API mode generates a draft based on the brief but has no web-search tool connected. Verify claims using credible sources before using the output in a real project.

## Run locally
1. Install Python 3.10 or newer.
2. Open a terminal in this folder.
3. (Recommended) Create and activate a virtual environment.
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Start in demo mode:
   ```bash
   streamlit run app.py
   ```
6. Optional Claude API mode: set `ANTHROPIC_API_KEY` in your environment before starting. Never commit your API key. You may set `ANTHROPIC_MODEL` if your account uses a different supported model name.

## Concepts demonstrated
- Prompting and clear task instructions
- Structured JSON output
- Context limited to the current brief
- Basic quality checks and human review
- Explicit tool/API boundaries and limitations

## Not yet implemented
- Live web search or source retrieval
- Executable research-tool loop
- MCP integrations
- Persistent memory
- Managed agent sessions, sandboxes, streaming events, or independent graders

These are possible future improvements and should not be described as implemented until built and tested.

## Project status
**Prototype / learning project.** Output requires source verification and human review.
