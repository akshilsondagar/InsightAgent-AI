from pydantic import BaseModel, Field

from models.recommendation import AIRecommendation


class ScoredRecommendation(BaseModel):
    """
    AI recommendation with business scoring.
    """

    recommendation: AIRecommendation = Field(
        description="The AI recommendation"
    )

    impact_score: int = Field(
        ge=1,
        le=10,
        description="Expected business impact score"
    )

    feasibility_score: int = Field(
        ge=1,
        le=10,
        description="Implementation feasibility score"
    )

    cost_score: int = Field(
        ge=1,
        le=10,
        description="Cost effectiveness score"
    )

    total_score: float = Field(
        ge=1,
        le=10,
        description="Overall recommendation score"
    )

    priority: str = Field(
        description="Priority: High, Medium, or Low"
    )