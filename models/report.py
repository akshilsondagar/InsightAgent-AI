from pydantic import BaseModel, Field

from models.research import CompanyResearch
from models.challenge import BusinessChallenge
from models.recommendation import AIRecommendation
from models.scoring import RecommendationScore


class ScoredRecommendation(BaseModel):
    """Connects an AI recommendation with its score."""

    recommendation: AIRecommendation

    score: RecommendationScore


class CompanyReport(BaseModel):
    """Represents the complete InsightAgent AI report."""

    company_name: str = Field(
        min_length=1
    )

    research: CompanyResearch

    challenges: list[BusinessChallenge] = Field(
        default_factory=list
    )

    recommendations: list[ScoredRecommendation] = Field(
        default_factory=list
    )

    executive_summary: str = ""

    ceo_pitch: str = ""