from pydantic import BaseModel, Field


class AIRecommendation(BaseModel):
    """Represents an AI solution recommendation."""

    title: str = Field(
        min_length=3,
        description="Name of the AI solution"
    )

    description: str = Field(
        min_length=10,
        description="Explanation of the recommendation"
    )

    problem_addressed: str = Field(
        description="Business problem addressed by the solution"
    )

    implementation_steps: list[str] = Field(
        default_factory=list,
        description="Steps required to implement the solution"
    )

    expected_benefits: list[str] = Field(
        default_factory=list,
        description="Expected business benefits"
    )

    risks: list[str] = Field(
        default_factory=list,
        description="Potential implementation risks"
    )