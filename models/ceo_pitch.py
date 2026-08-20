from pydantic import BaseModel, Field


class CEOPitch(BaseModel):
    """
    CEO-level strategic pitch.
    """

    executive_summary: str = Field(
        description="Short executive summary"
    )

    key_business_problem: str = Field(
        description="Most important business problem"
    )

    strategic_recommendation: str = Field(
        description="Recommended strategic AI solution"
    )

    expected_business_value: str = Field(
        description="Expected business value"
    )

    implementation_roadmap: list[str] = Field(
        description="Implementation roadmap"
    )

    immediate_next_steps: list[str] = Field(
        description="Immediate next steps"
    )