"""
MetricsThinking™: Universal Project Evaluation Engine & Forensic Auditor.
"""

__version__ = "1.0.0"

from .collector import ProjectCollector, ProjectEvidence
from .engine import run_audit
from .evaluator import CriteriaEvaluator
from .models import (
    AuditCriterion,
    CanonicalModuleEvaluation,
    MaturityBand,
    ModuleStatus,
    ProjectAuditReport,
    RemediationItem,
)
from .renderer import ReportRenderer
from .scorer import AuditScorer

__all__ = [
    "ModuleStatus",
    "MaturityBand",
    "AuditCriterion",
    "CanonicalModuleEvaluation",
    "RemediationItem",
    "ProjectAuditReport",
    "ProjectCollector",
    "ProjectEvidence",
    "CriteriaEvaluator",
    "AuditScorer",
    "ReportRenderer",
    "run_audit",
]
