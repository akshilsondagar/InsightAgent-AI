from pydantic import BaseModel, Field


class ResearchSource(BaseModel):
    """Represents one web research source."""

    title: str
    url: str
    content: str


class CompanyResearch(BaseModel):
    """Represents all research collected for a company."""

    company_name: str = Field(
        min_length=1,
        description="Name of the researched company"
    )

    queries: list[str]

    sources: list[ResearchSource]

    formatted_research: str