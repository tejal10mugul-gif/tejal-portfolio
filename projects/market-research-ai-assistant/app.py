import json
import os
from datetime import datetime

import streamlit as st

st.set_page_config(page_title="Market Research AI Assistant", page_icon="🔎", layout="wide")
st.title("🔎 Market Research AI Assistant")
st.caption("Portfolio prototype • Claude Platform 101 concepts • Demo data unless an API key is configured")

with st.sidebar:
    st.header("Research brief")
    industry = st.text_input("Industry", "Renewable energy")
    geography = st.text_input("Geography", "India")
    company = st.text_input("Company or focus", "Solar power companies")
    research_goal = st.selectbox(
        "Research goal",
        ["Company profiling", "Competitor benchmarking", "Market overview", "Strategic research questions"]
    )
    st.divider()
    st.caption("API mode uses the Anthropic API if ANTHROPIC_API_KEY is configured. Otherwise, the app shows clearly labeled illustrative demo output.")

def demo_report(industry, geography, company, research_goal):
    return {
        "project": {
            "industry": industry,
            "geography": geography,
            "focus": company,
            "research_goal": research_goal,
            "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M")
        },
        "executive_summary": (
            "DEMO OUTPUT ONLY. This example illustrates the report structure, not verified market findings. "
            "Replace the illustrative entries with sourced research before using this for a business decision."
        ),
        "company_profiles": [
            {
                "company": "Example Solar One (illustrative)",
                "positioning": "Illustrative utility-scale solar developer",
                "offering": "Solar project development and operations",
                "evidence": "Demo placeholder — no source checked",
                "confidence": "Low — illustrative only"
            },
            {
                "company": "Example Green Energy (illustrative)",
                "positioning": "Illustrative distributed energy provider",
                "offering": "Commercial rooftop solar solutions",
                "evidence": "Demo placeholder — no source checked",
                "confidence": "Low — illustrative only"
            }
        ],
        "comparison": [
            {"dimension": "Target customer", "company_a": "Utility / large project (illustrative)", "company_b": "Commercial rooftop (illustrative)"},
            {"dimension": "Business model", "company_a": "Project development (illustrative)", "company_b": "Solutions provider (illustrative)"},
            {"dimension": "Evidence status", "company_a": "Not verified", "company_b": "Not verified"}
        ],
        "research_gaps": [
            "Verify each company’s current offering using official sources.",
            "Collect dated source URLs for market size, capacity, revenue and pricing claims.",
            "Do not infer market share or growth rates without a defensible methodology."
        ],
        "quality_check": {
            "source_links_present": False,
            "claims_verified": False,
            "missing_data_flagged": True,
            "human_review_required": True
        }
    }

def call_claude(industry, geography, company, research_goal):
    import anthropic
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    prompt = f"""
You are assisting with a market research draft. Produce valid JSON only with these keys:
project, executive_summary, company_profiles, comparison, research_gaps, quality_check.
Research brief:
Industry: {industry}
Geography: {geography}
Focus: {company}
Goal: {research_goal}

Important constraints:
- You do not have a web-search tool in this app. Do not claim you performed live research or verified current facts.
- Clearly mark unsupported specifics as needing verification.
- Do not invent source URLs, market statistics, revenue, market share, or pricing.
- Use company_profiles as a list of objects with company, positioning, offering, evidence, confidence.
- Use comparison as a list of objects with dimension, company_a, company_b.
- Use research_gaps as a list of verification tasks.
- quality_check must include source_links_present, claims_verified, missing_data_flagged, human_review_required.
- Explain that this is a research draft requiring source verification.
"""
    response = client.messages.create(
        model=os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-5"),
        max_tokens=1800,
        messages=[{"role": "user", "content": prompt}],
    )
    text_parts = [block.text for block in response.content if getattr(block, "type", None) == "text"]
    raw = "\n".join(text_parts).strip()
    if raw.startswith("```"):
        raw = raw.split("\n", 1)[1].rsplit("```", 1)[0].strip()
    return json.loads(raw)

left, right = st.columns([1, 1])
with left:
    st.subheader("Research workflow")
    st.markdown("1. Define the brief\n2. Generate structured draft\n3. Inspect gaps and evidence status\n4. Review before use")
with right:
    st.subheader("Concepts demonstrated")
    st.markdown("- Structured JSON output\n- Clear tool/API boundary\n- Context: only the current brief is sent\n- Quality rubric and human review\n- Explicit limitations")

run = st.button("Generate research draft", type="primary", use_container_width=True)

if run:
    with st.spinner("Preparing research draft..."):
        try:
            if os.getenv("ANTHROPIC_API_KEY"):
                report = call_claude(industry, geography, company, research_goal)
                mode = "Claude API mode"
            else:
                report = demo_report(industry, geography, company, research_goal)
                mode = "Illustrative demo mode"
            st.session_state["report"] = report
            st.session_state["mode"] = mode
        except Exception as e:
            st.error(f"Could not generate the API draft: {e}")
            st.info("Check your API key, model access, package installation and network connection. No API key? Remove it and run in demo mode.")

if "report" in st.session_state:
    report = st.session_state["report"]
    st.divider()
    st.subheader("Generated output")
    st.info(f"Mode: {st.session_state.get('mode', 'Demo')} — verify all claims and sources before business use.")
    profiles = report.get("company_profiles", [])
    if profiles:
        st.markdown("### Company profiles")
        st.dataframe(profiles, use_container_width=True, hide_index=True)
    comparison = report.get("comparison", [])
    if comparison:
        st.markdown("### Competitor comparison")
        st.dataframe(comparison, use_container_width=True, hide_index=True)
    st.markdown("### Executive summary")
    st.write(report.get("executive_summary", "No summary returned."))
    st.markdown("### Research gaps")
    for gap in report.get("research_gaps", []):
        st.markdown(f"- {gap}")
    st.markdown("### Quality check")
    st.json(report.get("quality_check", {}))
    st.download_button(
        "Download report as JSON",
        data=json.dumps(report, indent=2, ensure_ascii=False),
        file_name="market_research_report.json",
        mime="application/json",
        use_container_width=True
    )
    with st.expander("View complete JSON"):
        st.code(json.dumps(report, indent=2, ensure_ascii=False), language="json")

st.divider()
st.caption("Portfolio project: a prototype for learning and demonstration. Not a substitute for verified research, expert review, or live source collection.")
