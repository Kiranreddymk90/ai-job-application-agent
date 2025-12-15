"""Core module for job application agent"""

from .base_platform import BasePlatform
from .profile_analyzer import ProfileAnalyzer
from .job_matcher import JobMatcher
from .application_tracker import ApplicationTracker

__all__ = [
    "BasePlatform",
    "ProfileAnalyzer",
    "JobMatcher",
    "ApplicationTracker",
]
