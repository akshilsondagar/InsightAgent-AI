import json


# ============================================================
# COMPANY ANALYSIS PROMPT
# ============================================================

def build_company_analysis_prompt(research):
    """
    Build prompt for company analysis.
    """

    if hasattr(research, "model_dump"):
        research = research.model_dump()

    research_text = json.dumps(
        research,
        indent=2,
        default=str
    )

    return f"""
You are an expert business intelligence analyst.

Analyze the following company research.

COMPANY RESEARCH:
{research_text}

Return ONLY valid JSON.

Use EXACTLY this structure:

{{
    "company_overview": "string",
    "business_model_insights": [
        "string"
    ],
    "market_trends": [
        "string"
    ],
    "technology_insights": [
        "string"
    ],
    "key_observations": [
        "string"
    ]
}}

Rules:
- Return only JSON.
- Do not use Markdown.
- Do not use code blocks.
- Do not add extra keys.
- All list items must be strings.
- Keep insights concise and relevant.
"""


# ============================================================
# CHALLENGE DETECTION PROMPT
# ============================================================

def build_challenge_detection_prompt(
    company_name,
    research,
    analysis
):
    """
    Build prompt for detecting business challenges.
    """

    if hasattr(research, "model_dump"):
        research = research.model_dump()

    if hasattr(analysis, "model_dump"):
        analysis = analysis.model_dump()

    research_text = json.dumps(
        research,
        indent=2,
        default=str
    )

    analysis_text = json.dumps(
        analysis,
        indent=2,
        default=str
    )

    return f"""
You are a business strategy and AI transformation expert.

Analyze the company and identify important business
challenges or strategic opportunities.

COMPANY:
{company_name}

RESEARCH:
{research_text}

COMPANY ANALYSIS:
{analysis_text}

Return ONLY valid JSON.

Use EXACTLY this structure:

{{
    "challenges": [
        {{
            "title": "Challenge title",
            "description": "Clear explanation of the challenge",
            "evidence": [
                "Evidence or observation"
            ],
            "impact": "Business impact",
            "priority": "High"
        }}
    ]
}}

Rules:
- Identify 3 to 5 meaningful challenges.
- priority must be High, Medium, or Low.
- evidence must always be a list of strings.
- Return only JSON.
- Do not use Markdown.
"""


# ============================================================
# RECOMMENDATION GENERATION PROMPT
# ============================================================

def build_recommendation_prompt(
    company_name,
    challenges,
    analysis
):
    """
    Build prompt for generating AI recommendations.
    """

    if hasattr(challenges, "model_dump"):
        challenges = challenges.model_dump()

    if hasattr(analysis, "model_dump"):
        analysis = analysis.model_dump()

    challenges_text = json.dumps(
        challenges,
        indent=2,
        default=str
    )

    analysis_text = json.dumps(
        analysis,
        indent=2,
        default=str
    )

    return f"""
You are an AI strategy consultant.

Generate practical AI-powered recommendations for
the following company.

COMPANY:
{company_name}

BUSINESS CHALLENGES:
{challenges_text}

COMPANY ANALYSIS:
{analysis_text}

Return ONLY valid JSON.

Use EXACTLY this structure:

{{
    "recommendations": [
        {{
            "title": "Recommendation title",
            "description": "Clear explanation",
            "problem_addressed": "Challenge being solved",
            "implementation_steps": [
                "Step 1",
                "Step 2",
                "Step 3"
            ],
            "expected_benefits": [
                "Benefit 1",
                "Benefit 2"
            ],
            "risks": [
                "Risk 1"
            ]
        }}
    ]
}}

Rules:
- Generate one useful recommendation for each major challenge.
- Recommendations should be realistic.
- Focus on AI, automation, analytics, or intelligent systems.
- Return only JSON.
- Do not use Markdown.
"""


# ============================================================
# RECOMMENDATION SCORING PROMPT
# ============================================================

def build_scoring_prompt(
    company_name,
    recommendations
):
    """
    Build prompt for scoring recommendations.
    """

    recommendations_text = json.dumps(
        recommendations,
        indent=2,
        default=str
    )

    return f"""
You are an expert business strategy consultant.

Score the following recommendations for the company.

COMPANY:
{company_name}

RECOMMENDATIONS:
{recommendations_text}

Evaluate each recommendation using:

1. Business Impact
2. Implementation Feasibility
3. Cost Effectiveness

Each score must be an integer from 1 to 10.

Calculate:

total_score =
(impact_score + feasibility_score + cost_score) / 3

Priority rules:

8.0 to 10.0 = High
5.0 to 7.9 = Medium
1.0 to 4.9 = Low

Return ONLY valid JSON.

Use EXACTLY this structure:

{{
    "scored_recommendations": [
        {{
            "recommendation": {{
                "title": "Recommendation title",
                "description": "Description",
                "problem_addressed": "Problem",
                "implementation_steps": [
                    "Step 1"
                ],
                "expected_benefits": [
                    "Benefit 1"
                ],
                "risks": [
                    "Risk 1"
                ]
            }},
            "impact_score": 9,
            "feasibility_score": 8,
            "cost_score": 7,
            "total_score": 8.0,
            "priority": "High"
        }}
    ]
}}

Rules:
- Score every recommendation.
- Return only JSON.
- priority must be High, Medium, or Low.
- Do not add extra text.
"""


# ============================================================
# CEO PITCH PROMPT
# ============================================================

def build_ceo_pitch_prompt(
    company_name,
    analysis,
    challenges,
    scored_recommendations
):
    """
    Build prompt for generating a CEO-level strategic pitch.
    """

    if hasattr(analysis, "model_dump"):
        analysis = analysis.model_dump()

    if hasattr(challenges, "model_dump"):
        challenges = challenges.model_dump()

    if hasattr(scored_recommendations, "model_dump"):
        scored_recommendations = (
            scored_recommendations.model_dump()
        )

    analysis_text = json.dumps(
        analysis,
        indent=2,
        default=str
    )

    challenges_text = json.dumps(
        challenges,
        indent=2,
        default=str
    )

    recommendations_text = json.dumps(
        scored_recommendations,
        indent=2,
        default=str
    )

    return f"""
You are a senior business strategy consultant
preparing a CEO-level AI transformation proposal.

COMPANY:
{company_name}

COMPANY ANALYSIS:
{analysis_text}

BUSINESS CHALLENGES:
{challenges_text}

SCORED AI RECOMMENDATIONS:
{recommendations_text}

Create a concise and convincing CEO strategy pitch.

Return ONLY valid JSON.

IMPORTANT:
The JSON MUST contain exactly these fields:

{{
    "executive_summary": "Short executive summary",
    "key_business_problem": "Most important business problem",
    "strategic_recommendation": "Recommended strategic AI solution",
    "expected_business_value": "Expected business value",
    "implementation_roadmap": [
        "Phase 1: ...",
        "Phase 2: ...",
        "Phase 3: ..."
    ],
    "immediate_next_steps": [
        "Step 1",
        "Step 2",
        "Step 3"
    ]
}}

STRICT RULES:

1. executive_summary MUST be a string.
2. key_business_problem MUST be a string.
3. strategic_recommendation MUST be a string.
4. expected_business_value MUST be a string.
5. implementation_roadmap MUST be a list of strings.
6. immediate_next_steps MUST be a list of strings.
7. Do not return dictionaries for string fields.
8. Do not return Markdown.
9. Do not use ```json.
10. Do not add explanations.
11. Return ONLY valid JSON.
"""