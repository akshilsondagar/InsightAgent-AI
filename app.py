import json
from datetime import datetime

import streamlit as st

# ============================================================
# PROJECT IMPORTS
# ============================================================

from research.research_pipeline import research_company

from analysis.company_analyzer import analyze_company

from analysis.challenge_detector import detect_challenges

from analysis.recommendation_generator import (
    generate_recommendations
)

from analysis.recommendation_scorer import (
    score_recommendations
)

from analysis.ceo_pitch_generator import (
    generate_ceo_pitch
)

from reports.report_generator import (
    create_report_data,
    generate_json_report,
    generate_pdf_report,
    generate_markdown_report
)


# ============================================================
# STREAMLIT PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="InsightAgent AI",
    page_icon="🤖",
    layout="wide"
)


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def convert_to_dict(data):
    """
    Convert Pydantic models, lists, and dictionaries
    into normal Python dictionaries.
    """

    if data is None:
        return None

    if hasattr(data, "model_dump"):
        return data.model_dump()

    if isinstance(data, list):
        return [
            convert_to_dict(item)
            for item in data
        ]

    if isinstance(data, dict):
        return {
            key: convert_to_dict(value)
            for key, value in data.items()
        }

    return data


# ============================================================
# HEADER
# ============================================================

st.title("🤖 InsightAgent AI")

st.subheader(
    "AI-Powered Company Research and Strategic Intelligence"
)

st.write(
    """
InsightAgent AI researches a company and generates
AI-powered strategic insights.

### What the system does:

- 🔍 Research company information
- 🧠 Analyze the company
- ⚠️ Detect business challenges
- 💡 Generate AI recommendations
- 📊 Score recommendations
- 🎯 Generate a CEO strategy pitch
- 📥 Download the complete report
"""
)

st.divider()


# ============================================================
# USER INPUT
# ============================================================

company_name = st.text_input(
    "Enter Company Name",
    placeholder="Example: Netflix, Tesla, Spotify"
)


analyze_button = st.button(
    "🚀 Analyze Company",
    use_container_width=True
)


# ============================================================
# ANALYSIS PIPELINE
# ============================================================

if analyze_button:

    # --------------------------------------------------------
    # VALIDATE INPUT
    # --------------------------------------------------------

    if not company_name.strip():

        st.warning(
            "⚠️ Please enter a company name."
        )

        st.stop()

    company_name = company_name.strip()

    try:

        # ====================================================
        # START STATUS
        # ====================================================

        with st.status(
            f"🚀 Starting AI analysis for: {company_name}",
            expanded=True
        ) as status:

            # =================================================
            # STEP 1 — WEB RESEARCH
            # =================================================

            st.write(
                "🔍 Step 1/6: Researching company information..."
            )

            research = research_company(
                company_name
            )

            st.write(
                "✅ Company research completed."
            )


            # =================================================
            # STEP 2 — COMPANY ANALYSIS
            # =================================================

            st.write(
                "🧠 Step 2/6: Analyzing company information..."
            )

            analysis = analyze_company(
                research
            )

            st.write(
                "✅ Company analysis completed."
            )


            # =================================================
            # STEP 3 — CHALLENGE DETECTION
            # =================================================

            st.write(
                "⚠️ Step 3/6: Detecting business challenges..."
            )

            challenges = detect_challenges(
                company_name=company_name,
                research=research,
                analysis=analysis
            )

            st.write(
                "✅ Business challenges detected."
            )


            # =================================================
            # STEP 4 — AI RECOMMENDATIONS
            # =================================================

            st.write(
                "💡 Step 4/6: Generating AI recommendations..."
            )

            recommendations = generate_recommendations(
                company_name=company_name,
                challenges=challenges,
                analysis=analysis
            )

            st.write(
                "✅ AI recommendations generated."
            )


            # =================================================
            # STEP 5 — RECOMMENDATION SCORING
            # =================================================

            st.write(
                "📊 Step 5/6: Scoring recommendations..."
            )

            # IMPORTANT:
            # Pass recommendations to score_recommendations()

            scored_recommendations = score_recommendations(
            company_name=company_name,
            recommendations=recommendations
)
            st.write(
                "✅ Recommendations scored."
            )


            # =================================================
            # STEP 6 — CEO PITCH
            # =================================================

            st.write(
                "🎯 Step 6/6: Generating CEO strategy pitch..."
            )

            pitch = generate_ceo_pitch(
                company_name=company_name,
                analysis=analysis,
                challenges=challenges,
                scored_recommendations=scored_recommendations
            )

            st.write(
                "✅ CEO strategy pitch generated."
            )


            # =================================================
            # COMPLETE
            # =================================================

            status.update(
                label="🎉 Analysis completed successfully!",
                state="complete",
                expanded=False
            )


        # ====================================================
        # SAVE RESULTS
        # ====================================================

        st.session_state["company_name"] = (
            company_name
        )

        st.session_state["research"] = (
            research
        )

        st.session_state["analysis"] = (
            analysis
        )

        st.session_state["challenges"] = (
            challenges
        )

        st.session_state["recommendations"] = (
            recommendations
        )

        st.session_state[
            "scored_recommendations"
        ] = scored_recommendations

        st.session_state["pitch"] = (
            pitch
        )


    except Exception as error:

        st.error(
            "❌ Analysis failed."
        )

        st.exception(
            error
        )


# ============================================================
# DISPLAY RESULTS
# ============================================================

if "analysis" in st.session_state:

    st.divider()

    st.success(
        f"🎉 Analysis completed for "
        f"{st.session_state['company_name']}"
    )



    # ========================================================
    # CREATE TABS
    # ========================================================

    (
        tab_overview,
        tab_analysis,
        tab_challenges,
        tab_recommendations,
        tab_ceo,
        tab_download
    ) = st.tabs(
        [
            "🏢 Overview",
            "🧠 Analysis",
            "⚠️ Challenges",
            "💡 Recommendations",
            "🎯 CEO Pitch",
            "📥 Download Report"
        ]
    )

    # ========================================================
    # TAB 1 — COMPANY OVERVIEW
    # ========================================================

    with tab_overview:

        st.header("🏢 Company Research")

        research = st.session_state["research"]

        st.subheader(
            st.session_state["company_name"]
        )

        st.json(
            convert_to_dict(research)
        )

    # ========================================================
    # TAB 2 — COMPANY ANALYSIS
    # ========================================================

    with tab_analysis:

        st.header("🧠 AI Company Analysis")

        analysis = st.session_state["analysis"]

        st.subheader("Company Overview")
        st.write(analysis.company_overview)

        st.subheader("Business Model Insights")
        for item in analysis.business_model_insights:
            st.write(f"• {item}")

        st.subheader("Market Trends")
        for item in analysis.market_trends:
            st.write(f"• {item}")

        st.subheader("Technology Insights")
        for item in analysis.technology_insights:
            st.write(f"• {item}")

        st.subheader("Key Observations")
        for item in analysis.key_observations:
            st.write(f"• {item}")

    # ========================================================
    # TAB 3 — BUSINESS CHALLENGES
    # ========================================================

    with tab_challenges:

        st.header("⚠️ Business Challenges")

        challenges = st.session_state["challenges"]

        if not challenges:
            st.info("No business challenges were detected.")
        else:
            for index, challenge in enumerate(challenges, start=1):

                with st.expander(
                    f"{index}. {challenge.title} — "
                    f"Priority: {challenge.priority}"
                ):

                    st.write("### Description")
                    st.write(challenge.description)

                    st.write("### Business Impact")
                    st.write(challenge.impact)

                    st.write("### Evidence")

                    for evidence in challenge.evidence:
                        st.write(f"• {evidence}")

    # ========================================================
    # TAB 4 — AI RECOMMENDATIONS
    # ========================================================

    with tab_recommendations:

        st.header("💡 AI Recommendations")

        scored_recommendations = st.session_state[
            "scored_recommendations"
        ]

        if not scored_recommendations:

            st.info("No recommendations were generated.")

        else:

            for index, item in enumerate(
                scored_recommendations,
                start=1
            ):

                if hasattr(item, "recommendation"):
                    recommendation = item.recommendation
                else:
                    recommendation = item

                with st.expander(
                    f"{index}. {recommendation.title}"
                ):

                    st.write("### Description")
                    st.write(recommendation.description)

                    if hasattr(
                        recommendation,
                        "problem_addressed"
                    ):
                        st.write("### Problem Addressed")
                        st.write(
                            recommendation.problem_addressed
                        )

                    if hasattr(
                        recommendation,
                        "implementation_steps"
                    ):
                        st.write("### Implementation Steps")

                        for step in recommendation.implementation_steps:
                            st.write(f"• {step}")

                    if hasattr(
                        recommendation,
                        "expected_benefits"
                    ):
                        st.write("### Expected Benefits")

                        for benefit in recommendation.expected_benefits:
                            st.write(f"• {benefit}")

                    if hasattr(recommendation, "risks"):
                        st.write("### Potential Risks")

                        for risk in recommendation.risks:
                            st.write(f"• {risk}")

                    if hasattr(item, "impact_score"):

                        st.divider()
                        st.subheader("Recommendation Score")

                        col1, col2, col3, col4 = st.columns(4)

                        col1.metric(
                            "Impact",
                            item.impact_score
                        )

                        col2.metric(
                            "Feasibility",
                            item.feasibility_score
                        )

                        col3.metric(
                            "Cost",
                            item.cost_score
                        )

                        col4.metric(
                            "Total Score",
                            item.total_score
                        )

                        if hasattr(item, "priority"):
                            st.write(
                                f"### Priority: {item.priority}"
                            )

    # ========================================================
    # TAB 5 — CEO PITCH
    # ========================================================

    with tab_ceo:

        st.header("🎯 CEO Strategy Pitch")

        pitch = st.session_state["pitch"]

        st.subheader("Executive Summary")
        st.write(pitch.executive_summary)

        st.subheader("Key Business Problem")
        st.write(pitch.key_business_problem)

        st.subheader("Strategic Recommendation")
        st.write(pitch.strategic_recommendation)

        st.subheader("Expected Business Value")
        st.write(pitch.expected_business_value)

        st.subheader("Implementation Roadmap")

        for step in pitch.implementation_roadmap:
            st.write(f"• {step}")

        st.subheader("Immediate Next Steps")

        for step in pitch.immediate_next_steps:
            st.write(f"• {step}")

    # ========================================================
    # TAB 6 — DOWNLOAD REPORT
    # ========================================================

    with tab_download:

        st.header("📥 Download Complete Report")

        # Create ONE master report dictionary.
        # JSON, PDF and Markdown are all generated from this data.
        report = create_report_data(
            company_name=st.session_state["company_name"],
            research=st.session_state["research"],
            analysis=st.session_state["analysis"],
            challenges=st.session_state["challenges"],
            recommendations=st.session_state["recommendations"],
            scored_recommendations=st.session_state[
                "scored_recommendations"
            ],
            pitch=st.session_state["pitch"]
        )

        # ====================================================
        # JSON REPORT
        # ====================================================

        st.subheader("📄 JSON Report")

        try:

            report_json = generate_json_report(
                report
            )

            st.download_button(
                label="📥 Download JSON Report",
                data=report_json,
                file_name=(
                    f"{st.session_state['company_name']}"
                    "_InsightAgent_Report.json"
                ),
                mime="application/json",
                use_container_width=True
            )

        except Exception as error:

            st.error(
                "❌ JSON report generation failed."
            )

            st.exception(error)

        # ====================================================
        # PDF REPORT
        # ====================================================

        st.subheader("📕 PDF Report")

        try:

            report_pdf = generate_pdf_report(
                report
            )

            st.download_button(
                label="📥 Download PDF Report",
                data=report_pdf,
                file_name=(
                    f"{st.session_state['company_name']}"
                    "_InsightAgent_Report.pdf"
                ),
                mime="application/pdf",
                use_container_width=True
            )

        except Exception as error:

            st.error(
                "❌ PDF report generation failed."
            )

            st.exception(error)

        # ====================================================
        # MARKDOWN REPORT
        # ====================================================

        st.subheader("📝 Markdown Report")

        try:

            report_markdown = generate_markdown_report(
                company_name=st.session_state["company_name"],
                analysis=st.session_state["analysis"],
                challenges=st.session_state["challenges"],
                scored_recommendations=st.session_state[
                    "scored_recommendations"
                ],
                pitch=st.session_state["pitch"]
            )

            st.download_button(
                label="📥 Download Markdown Report",
                data=report_markdown,
                file_name=(
                    f"{st.session_state['company_name']}"
                    "_InsightAgent_Report.md"
                ),
                mime="text/markdown",
                use_container_width=True
            )

        except Exception as error:

            st.error(
                "❌ Markdown report generation failed."
            )

            st.exception(error)

        st.success(
            "✅ JSON, PDF and Markdown reports are ready."
        )
