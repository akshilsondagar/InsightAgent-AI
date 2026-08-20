from pydantic import BaseModel, Field


class BusinessChallenge(BaseModel):
    """
    Represents a business challenge identified during analysis.
    """

    title: str = Field(
        description="Short title of the business challenge"
    )

    description: str = Field(
        description="Detailed explanation of the challenge"
    )

    evidence: list[str] = Field(
        description="Evidence supporting this challenge"
    )

    impact: str = Field(
        description="Business impact of this challenge"
    )

    priority: str = Field(
        description="Priority level: High, Medium, or Low"
    )