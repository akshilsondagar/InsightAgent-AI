from pydantic import BaseModel, Field


class RecommendationScore(BaseModel):
    """Represents a score for an AI recommendation."""

    impact_score: int = Field(
        ge=1,
        le=10,
        description="Expected business impact score"
    )

    feasibility_score: int = Field(
        ge=1,
        le=10,
        description="Technical and operational feasibility score"
    )

    cost_score: int = Field(
        ge=1,
        le=10,
        description="Cost efficiency score"
    )

    total_score: float = Field(
        ge=0,
        le=10,
        description="Overall recommendation score"
    )

    priority: str = Field(
        description="High, Medium, or Low"
    )