from enum import StrEnum

from pydantic import BaseModel, Field


class Verdict(StrEnum):
    SHIP_IT = "Ship It"
    NOT_BAD = "Not Bad"
    SKETCHY = "Sketchy"
    BUST = "Bust"


class CategoryScore(BaseModel):
    category: str
    score: float = Field(ge=0, le=100)
    summary: str
    findings: list[str] = []


class AnalysisResult(BaseModel):
    verdict: Verdict
    overall_score: float = Field(ge=0, le=100)
    categories: list[CategoryScore] = []
    plain_english_summary: str
    fix_before_deploy: list[str] = []
