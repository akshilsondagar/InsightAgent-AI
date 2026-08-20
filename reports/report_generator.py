# from models.analysis import CompanyAnalysis
# from models.challenge import BusinessChallenge
# from models.scored_recommendation import ScoredRecommendation
# from models.ceo_pitch import CEOPitch


# def generate_markdown_report(
#     company_name: str,
#     analysis: CompanyAnalysis,
#     challenges: list[BusinessChallenge],
#     scored_recommendations: list[ScoredRecommendation],
#     pitch: CEOPitch
# ) -> str:
#     """
#     Generate a complete AI Business Strategy Report
#     in Markdown format.
#     """

#     report = []

#     # ============================================================
#     # TITLE
#     # ============================================================

#     report.append(
#         f"# InsightAgent AI Report: {company_name}"
#     )

#     report.append(
#         "AI-Powered Business Research & Strategy Analysis"
#     )

#     report.append("\n---\n")


#     # ============================================================
#     # COMPANY ANALYSIS
#     # ============================================================

#     report.append(
#         "## 🏢 Company Analysis"
#     )

#     report.append(
#         "### Company Overview"
#     )

#     report.append(
#         analysis.company_overview
#     )

#     report.append(
#         "### Business Model Insights"
#     )

#     report.extend(
#         format_markdown_list(
#             analysis.business_model_insights
#         )
#     )

#     report.append(
#         "### Market Trends"
#     )

#     report.extend(
#         format_markdown_list(
#             analysis.market_trends
#         )
#     )

#     report.append(
#         "### Technology Insights"
#     )

#     report.extend(
#         format_markdown_list(
#             analysis.technology_insights
#         )
#     )

#     report.append(
#         "### Key Observations"
#     )

#     report.extend(
#         format_markdown_list(
#             analysis.key_observations
#         )
#     )

#     report.append("\n---\n")


#     # ============================================================
#     # BUSINESS CHALLENGES
#     # ============================================================

#     report.append(
#         "## 🎯 Key Business Challenges"
#     )

#     if not challenges:

#         report.append(
#             "No major business challenges were detected."
#         )

#     else:

#         for index, challenge in enumerate(
#             challenges,
#             start=1
#         ):

#             report.append(
#                 f"### {index}. {challenge.title}"
#             )

#             report.append(
#                 f"**Priority:** {challenge.priority}"
#             )

#             report.append(
#                 f"**Description:** {challenge.description}"
#             )

#             report.append(
#                 f"**Business Impact:** {challenge.impact}"
#             )

#             report.append(
#                 "**Evidence:**"
#             )

#             report.extend(
#                 format_markdown_list(
#                     challenge.evidence
#                 )
#             )

#             report.append("")


#     report.append("\n---\n")


#     # ============================================================
#     # AI RECOMMENDATIONS
#     # ============================================================

#     report.append(
#         "## 💡 Ranked AI Recommendations"
#     )

#     if not scored_recommendations:

#         report.append(
#             "No AI recommendations were generated."
#         )

#     else:

#         for rank, item in enumerate(
#             scored_recommendations,
#             start=1
#         ):

#             recommendation = item.recommendation
#             score = item.score

#             report.append(
#                 f"### 🏆 Rank #{rank}: "
#                 f"{recommendation.title}"
#             )

#             report.append(
#                 f"**Priority:** {score.priority}"
#             )

#             report.append(
#                 f"**Description:** "
#                 f"{recommendation.description}"
#             )

#             report.append(
#                 f"**Problem Addressed:** "
#                 f"{recommendation.problem_addressed}"
#             )

#             report.append(
#                 "#### 📊 Recommendation Score"
#             )

#             report.append(
#                 f"- Impact Score: "
#                 f"{score.impact_score}/10"
#             )

#             report.append(
#                 f"- Feasibility Score: "
#                 f"{score.feasibility_score}/10"
#             )

#             report.append(
#                 f"- Cost Efficiency Score: "
#                 f"{score.cost_score}/10"
#             )

#             report.append(
#                 f"- **Total Score: "
#                 f"{score.total_score}/10**"
#             )

#             report.append(
#                 "#### 🛠️ Implementation Steps"
#             )

#             report.extend(
#                 format_markdown_list(
#                     recommendation.implementation_steps
#                 )
#             )

#             report.append(
#                 "#### ✅ Expected Benefits"
#             )

#             report.extend(
#                 format_markdown_list(
#                     recommendation.expected_benefits
#                 )
#             )

#             report.append(
#                 "#### ⚠️ Potential Risks"
#             )

#             report.extend(
#                 format_markdown_list(
#                     recommendation.risks
#                 )
#             )

#             report.append("")


#     report.append("\n---\n")


#     # ============================================================
#     # EXECUTIVE STRATEGY
#     # ============================================================

#     report.append(
#         "## 👔 Executive Strategy"
#     )

#     report.append(
#         "### Executive Summary"
#     )

#     report.append(
#         pitch.executive_summary
#     )

#     report.append(
#         "### 🎯 Key Business Problem"
#     )

#     report.append(
#         pitch.key_business_problem
#     )

#     report.append(
#         "### 💡 Strategic Recommendation"
#     )

#     report.append(
#         pitch.strategic_recommendation
#     )

#     report.append(
#         "### 💰 Expected Business Value"
#     )

#     report.extend(
#         format_markdown_list(
#             pitch.expected_business_value
#         )
#     )

#     report.append(
#         "### 🗺️ Implementation Roadmap"
#     )

#     for index, step in enumerate(
#         pitch.implementation_roadmap,
#         start=1
#     ):

#         report.append(
#             f"{index}. {step}"
#         )

#     report.append(
#         "### 🚀 Immediate Next Steps"
#     )

#     for index, step in enumerate(
#         pitch.immediate_next_steps,
#         start=1
#     ):

#         report.append(
#             f"{index}. {step}"
#         )


#     # ============================================================
#     # FOOTER
#     # ============================================================

#     report.append("\n---\n")

#     report.append(
#         "Generated by InsightAgent AI"
#     )

#     report.append(
#         "AI-Powered Business Research & Strategy Assistant"
#     )


#     return "\n\n".join(report)


# def format_markdown_list(
#     items: list[str]
# ) -> list[str]:
#     """
#     Convert a Python list into Markdown bullet points.
#     """

#     if not items:

#         return [
#             "- No information available"
#         ]

#     return [
#         f"- {item}"
#         for item in items
#     ]

import json
from io import BytesIO
from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle
)
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak,
    Table,
    TableStyle
)

from models.company import CompanyAnalysis
from models.challenges import BusinessChallenge
from models.scored_recommendation import ScoredRecommendation
from models.ceo_pitch import CEOPitch


# ============================================================
# COMMON HELPER
# ============================================================

def convert_to_dict(data):
    """
    Convert Pydantic models and nested objects into
    normal Python dictionaries/lists.
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
# COMPLETE REPORT DICTIONARY
# ============================================================

def create_report_data(
    company_name: str,
    research,
    analysis: CompanyAnalysis,
    challenges: list[BusinessChallenge],
    recommendations,
    scored_recommendations: list[ScoredRecommendation],
    pitch: CEOPitch
) -> dict:
    """
    Create the master report dictionary.

    This dictionary is the single source of truth for:
    - JSON
    - PDF
    - Markdown
    """

    return {
        "company_name": company_name,

        "generated_at": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),

        "research": convert_to_dict(
            research
        ),

        "company_analysis": convert_to_dict(
            analysis
        ),

        "business_challenges": convert_to_dict(
            challenges
        ),

        "ai_recommendations": convert_to_dict(
            recommendations
        ),

        "scored_recommendations": convert_to_dict(
            scored_recommendations
        ),

        "ceo_pitch": convert_to_dict(
            pitch
        )
    }


# ============================================================
# JSON REPORT
# ============================================================

def generate_json_report(
    report_data: dict
) -> str:
    """
    Generate machine-readable JSON report.
    """

    return json.dumps(
        report_data,
        indent=4,
        ensure_ascii=False,
        default=str
    )


# ============================================================
# MARKDOWN REPORT
# ============================================================

def generate_markdown_report(
    company_name: str,
    analysis: CompanyAnalysis,
    challenges: list[BusinessChallenge],
    scored_recommendations: list[ScoredRecommendation],
    pitch: CEOPitch
) -> str:
    """
    Generate a complete AI Business Strategy Report
    in Markdown format.
    """

    report = []

    # ========================================================
    # TITLE
    # ========================================================

    report.append(
        f"# InsightAgent AI Report: {company_name}"
    )

    report.append(
        "AI-Powered Business Research & Strategy Analysis"
    )

    report.append("\n---\n")

    # ========================================================
    # COMPANY ANALYSIS
    # ========================================================

    report.append(
        "## 🏢 Company Analysis"
    )

    report.append(
        "### Company Overview"
    )

    report.append(
        analysis.company_overview
    )

    report.append(
        "### Business Model Insights"
    )

    report.extend(
        format_markdown_list(
            analysis.business_model_insights
        )
    )

    report.append(
        "### Market Trends"
    )

    report.extend(
        format_markdown_list(
            analysis.market_trends
        )
    )

    report.append(
        "### Technology Insights"
    )

    report.extend(
        format_markdown_list(
            analysis.technology_insights
        )
    )

    report.append(
        "### Key Observations"
    )

    report.extend(
        format_markdown_list(
            analysis.key_observations
        )
    )

    report.append("\n---\n")

    # ========================================================
    # BUSINESS CHALLENGES
    # ========================================================

    report.append(
        "## 🎯 Key Business Challenges"
    )

    if not challenges:

        report.append(
            "No major business challenges were detected."
        )

    else:

        for index, challenge in enumerate(
            challenges,
            start=1
        ):

            report.append(
                f"### {index}. {challenge.title}"
            )

            report.append(
                f"**Priority:** {challenge.priority}"
            )

            report.append(
                f"**Description:** {challenge.description}"
            )

            report.append(
                f"**Business Impact:** {challenge.impact}"
            )

            report.append(
                "**Evidence:**"
            )

            report.extend(
                format_markdown_list(
                    challenge.evidence
                )
            )

            report.append("")

    report.append("\n---\n")

    # ========================================================
    # AI RECOMMENDATIONS
    # ========================================================

    report.append(
        "## 💡 Ranked AI Recommendations"
    )

    if not scored_recommendations:

        report.append(
            "No AI recommendations were generated."
        )

    else:

        for rank, item in enumerate(
            scored_recommendations,
            start=1
        ):

            recommendation = item.recommendation

            report.append(
                f"### 🏆 Rank #{rank}: "
                f"{recommendation.title}"
            )

            report.append(
                f"**Priority:** {item.priority}"
            )

            report.append(
                f"**Description:** "
                f"{recommendation.description}"
            )

            report.append(
                f"**Problem Addressed:** "
                f"{recommendation.problem_addressed}"
            )

            report.append(
                "#### 📊 Recommendation Score"
            )

            report.append(
                f"- Impact Score: "
                f"{item.impact_score}/10"
            )

            report.append(
                f"- Feasibility Score: "
                f"{item.feasibility_score}/10"
            )

            report.append(
                f"- Cost Efficiency Score: "
                f"{item.cost_score}/10"
            )

            report.append(
                f"- **Total Score: "
                f"{item.total_score}/10**"
            )

            report.append(
                "#### 🛠️ Implementation Steps"
            )

            report.extend(
                format_markdown_list(
                    recommendation.implementation_steps
                )
            )

            report.append(
                "#### ✅ Expected Benefits"
            )

            report.extend(
                format_markdown_list(
                    recommendation.expected_benefits
                )
            )

            report.append(
                "#### ⚠️ Potential Risks"
            )

            report.extend(
                format_markdown_list(
                    recommendation.risks
                )
            )

            report.append("")

    report.append("\n---\n")

    # ========================================================
    # CEO STRATEGY
    # ========================================================

    report.append(
        "## 👔 Executive Strategy"
    )

    report.append(
        "### Executive Summary"
    )

    report.append(
        pitch.executive_summary
    )

    report.append(
        "### 🎯 Key Business Problem"
    )

    report.append(
        pitch.key_business_problem
    )

    report.append(
        "### 💡 Strategic Recommendation"
    )

    report.append(
        pitch.strategic_recommendation
    )

    report.append(
        "### 💰 Expected Business Value"
    )

    report.append(
        pitch.expected_business_value
    )

    report.append(
        "### 🗺️ Implementation Roadmap"
    )

    for index, step in enumerate(
        pitch.implementation_roadmap,
        start=1
    ):

        report.append(
            f"{index}. {step}"
        )

    report.append(
        "### 🚀 Immediate Next Steps"
    )

    for index, step in enumerate(
        pitch.immediate_next_steps,
        start=1
    ):

        report.append(
            f"{index}. {step}"
        )

    # ========================================================
    # FOOTER
    # ========================================================

    report.append("\n---\n")

    report.append(
        "Generated by InsightAgent AI"
    )

    report.append(
        "AI-Powered Business Research & Strategy Assistant"
    )

    return "\n\n".join(report)


# ============================================================
# MARKDOWN LIST HELPER
# ============================================================

def format_markdown_list(
    items: list[str]
) -> list[str]:
    """
    Convert Python list into Markdown bullets.
    """

    if not items:

        return [
            "- No information available"
        ]

    return [
        f"- {item}"
        for item in items
    ]


# ============================================================
# PDF REPORT
# ============================================================

def generate_pdf_report(
    report_data: dict
) -> bytes:
    """
    Generate a professional PDF report.

    Returns:
        PDF bytes
    """

    buffer = BytesIO()

    document = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "ReportTitle",
        parent=styles["Title"],
        alignment=TA_CENTER,
        fontSize=24,
        leading=30,
        spaceAfter=15
    )

    subtitle_style = ParagraphStyle(
        "ReportSubtitle",
        parent=styles["Normal"],
        alignment=TA_CENTER,
        fontSize=11,
        leading=16,
        spaceAfter=20
    )

    heading_style = ParagraphStyle(
        "ReportHeading",
        parent=styles["Heading2"],
        fontSize=16,
        leading=20,
        spaceBefore=12,
        spaceAfter=10
    )

    subheading_style = ParagraphStyle(
        "ReportSubHeading",
        parent=styles["Heading3"],
        fontSize=12,
        leading=16,
        spaceBefore=8,
        spaceAfter=6
    )

    normal_style = ParagraphStyle(
        "ReportNormal",
        parent=styles["BodyText"],
        fontSize=10,
        leading=15,
        spaceAfter=6
    )

    story = []

    company_name = report_data.get(
        "company_name",
        "Company"
    )

    generated_at = report_data.get(
        "generated_at",
        ""
    )

    # ========================================================
    # COVER
    # ========================================================

    story.append(
        Spacer(1, 1.2 * inch)
    )

    story.append(
        Paragraph(
            "InsightAgent AI",
            title_style
        )
    )

    story.append(
        Paragraph(
            "AI-Powered Company Research & Strategic Intelligence",
            subtitle_style
        )
    )

    story.append(
        Spacer(1, 0.3 * inch)
    )

    story.append(
        Paragraph(
            f"<b>Company:</b> {company_name}",
            normal_style
        )
    )

    story.append(
        Paragraph(
            f"<b>Generated:</b> {generated_at}",
            normal_style
        )
    )

    story.append(
        Spacer(1, 1 * inch)
    )

    story.append(
        Paragraph(
            "Confidential Business Strategy Report",
            subtitle_style
        )
    )

    story.append(
        PageBreak()
    )

    # ========================================================
    # COMPANY ANALYSIS
    # ========================================================

    story.append(
        Paragraph(
            "1. Company Analysis",
            heading_style
        )
    )

    analysis = report_data.get(
        "company_analysis",
        {}
    )

    add_pdf_text(
        story,
        "Company Overview",
        analysis.get(
            "company_overview",
            ""
        ),
        subheading_style,
        normal_style
    )

    add_pdf_list(
        story,
        "Business Model Insights",
        analysis.get(
            "business_model_insights",
            []
        ),
        subheading_style,
        normal_style
    )

    add_pdf_list(
        story,
        "Market Trends",
        analysis.get(
            "market_trends",
            []
        ),
        subheading_style,
        normal_style
    )

    add_pdf_list(
        story,
        "Technology Insights",
        analysis.get(
            "technology_insights",
            []
        ),
        subheading_style,
        normal_style
    )

    add_pdf_list(
        story,
        "Key Observations",
        analysis.get(
            "key_observations",
            []
        ),
        subheading_style,
        normal_style
    )

    # ========================================================
    # CHALLENGES
    # ========================================================

    story.append(
        PageBreak()
    )

    story.append(
        Paragraph(
            "2. Key Business Challenges",
            heading_style
        )
    )

    challenges = report_data.get(
        "business_challenges",
        []
    )

    for index, challenge in enumerate(
        challenges,
        start=1
    ):

        story.append(
            Paragraph(
                f"{index}. {challenge.get('title', '')}",
                subheading_style
            )
        )

        story.append(
            Paragraph(
                f"<b>Priority:</b> "
                f"{challenge.get('priority', '')}",
                normal_style
            )
        )

        story.append(
            Paragraph(
                challenge.get(
                    "description",
                    ""
                ),
                normal_style
            )
        )

        story.append(
            Paragraph(
                f"<b>Business Impact:</b> "
                f"{challenge.get('impact', '')}",
                normal_style
            )
        )

        add_pdf_list(
            story,
            "Evidence",
            challenge.get(
                "evidence",
                []
            ),
            subheading_style,
            normal_style
        )

    # ========================================================
    # RECOMMENDATIONS
    # ========================================================

    story.append(
        PageBreak()
    )

    story.append(
        Paragraph(
            "3. Ranked AI Recommendations",
            heading_style
        )
    )

    scored = report_data.get(
        "scored_recommendations",
        []
    )

    for rank, item in enumerate(
        scored,
        start=1
    ):

        recommendation = item.get(
            "recommendation",
            {}
        )

        story.append(
            Paragraph(
                f"🏆 Rank #{rank}: "
                f"{recommendation.get('title', '')}",
                subheading_style
            )
        )

        story.append(
            Paragraph(
                f"<b>Priority:</b> "
                f"{item.get('priority', '')}",
                normal_style
            )
        )

        story.append(
            Paragraph(
                recommendation.get(
                    "description",
                    ""
                ),
                normal_style
            )
        )

        story.append(
            Paragraph(
                f"<b>Problem Addressed:</b> "
                f"{recommendation.get('problem_addressed', '')}",
                normal_style
            )
        )

        # Score table

        score_table = Table(
            [
                [
                    "Impact",
                    "Feasibility",
                    "Cost",
                    "Total",
                    "Priority"
                ],
                [
                    str(
                        item.get(
                            "impact_score",
                            ""
                        )
                    ),
                    str(
                        item.get(
                            "feasibility_score",
                            ""
                        )
                    ),
                    str(
                        item.get(
                            "cost_score",
                            ""
                        )
                    ),
                    str(
                        item.get(
                            "total_score",
                            ""
                        )
                    ),
                    str(
                        item.get(
                            "priority",
                            ""
                        )
                    )
                ]
            ],
            colWidths=[
                0.8 * inch,
                1.0 * inch,
                0.7 * inch,
                0.7 * inch,
                0.9 * inch
            ]
        )

        score_table.setStyle(
            TableStyle(
                [
                    (
                        "BACKGROUND",
                        (0, 0),
                        (-1, 0),
                        colors.lightgrey
                    ),
                    (
                        "GRID",
                        (0, 0),
                        (-1, -1),
                        0.5,
                        colors.grey
                    ),
                    (
                        "ALIGN",
                        (0, 0),
                        (-1, -1),
                        "CENTER"
                    ),
                    (
                        "FONTNAME",
                        (0, 0),
                        (-1, 0),
                        "Helvetica-Bold"
                    ),
                    (
                        "FONTSIZE",
                        (0, 0),
                        (-1, -1),
                        8
                    )
                ]
            )
        )

        story.append(
            score_table
        )

        story.append(
            Spacer(1, 8)
        )

        add_pdf_list(
            story,
            "Implementation Steps",
            recommendation.get(
                "implementation_steps",
                []
            ),
            subheading_style,
            normal_style
        )

        add_pdf_list(
            story,
            "Expected Benefits",
            recommendation.get(
                "expected_benefits",
                []
            ),
            subheading_style,
            normal_style
        )

        add_pdf_list(
            story,
            "Potential Risks",
            recommendation.get(
                "risks",
                []
            ),
            subheading_style,
            normal_style
        )

    # ========================================================
    # CEO STRATEGY
    # ========================================================

    story.append(
        PageBreak()
    )

    story.append(
        Paragraph(
            "4. Executive Strategy",
            heading_style
        )
    )

    pitch = report_data.get(
        "ceo_pitch",
        {}
    )

    add_pdf_text(
        story,
        "Executive Summary",
        pitch.get(
            "executive_summary",
            ""
        ),
        subheading_style,
        normal_style
    )

    add_pdf_text(
        story,
        "Key Business Problem",
        pitch.get(
            "key_business_problem",
            ""
        ),
        subheading_style,
        normal_style
    )

    add_pdf_text(
        story,
        "Strategic Recommendation",
        pitch.get(
            "strategic_recommendation",
            ""
        ),
        subheading_style,
        normal_style
    )

    add_pdf_text(
        story,
        "Expected Business Value",
        pitch.get(
            "expected_business_value",
            ""
        ),
        subheading_style,
        normal_style
    )

    add_pdf_list(
        story,
        "Implementation Roadmap",
        pitch.get(
            "implementation_roadmap",
            []
        ),
        subheading_style,
        normal_style
    )

    add_pdf_list(
        story,
        "Immediate Next Steps",
        pitch.get(
            "immediate_next_steps",
            []
        ),
        subheading_style,
        normal_style
    )

    # ========================================================
    # FOOTER
    # ========================================================

    story.append(
        Spacer(1, 30)
    )

    story.append(
        Paragraph(
            "Generated by InsightAgent AI",
            subtitle_style
        )
    )

    document.build(
        story
    )

    buffer.seek(0)

    return buffer.getvalue()


# ============================================================
# PDF TEXT HELPER
# ============================================================

def add_pdf_text(
    story,
    title,
    text,
    heading_style,
    normal_style
):
    """
    Add a PDF heading and paragraph.
    """

    if not text:
        return

    story.append(
        Paragraph(
            title,
            heading_style
        )
    )

    story.append(
        Paragraph(
            str(text),
            normal_style
        )
    )


# ============================================================
# PDF LIST HELPER
# ============================================================

def add_pdf_list(
    story,
    title,
    items,
    heading_style,
    normal_style
):
    """
    Add a PDF heading and bullet list.
    """

    if not items:
        return

    story.append(
        Paragraph(
            title,
            heading_style
        )
    )

    for item in items:

        story.append(
            Paragraph(
                f"• {str(item)}",
                normal_style
            )
        )