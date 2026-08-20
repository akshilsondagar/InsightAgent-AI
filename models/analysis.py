from pydantic import BaseModel, Field


class CompanyAnalysis(BaseModel):
    """Represents AI-generated company analysis."""

    company_overview: str = Field(
        min_length=10,
        description="Brief overview of the company"
    )

    business_model_insights: list[str] = Field(
        default_factory=list,
        description="Key insights about the business model"
    )

    market_trends: list[str] = Field(
        default_factory=list,
        description="Relevant market or industry trends"
    )

    technology_insights: list[str] = Field(
        default_factory=list,
        description="Technology, digital, or AI insights"
    )

    key_observations: list[str] = Field(
        default_factory=list,
        description="Important observations from the research"
    )