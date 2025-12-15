"""Base platform abstraction for job application sites"""

from abc import ABC, abstractmethod
from typing import Dict, List, Any, Optional
from datetime import datetime
from loguru import logger


class BasePlatform(ABC):
    """Abstract base class for all job platforms"""
    
    def __init__(self, config: Dict[str, Any], credential_manager, qa_engine):
        self.config = config
        self.credential_manager = credential_manager
        self.qa_engine = qa_engine
        self.name = self.__class__.__name__
        self.is_logged_in = False
        self.browser = None
        self.applications_count = 0
        
    @abstractmethod
    async def login(self) -> bool:
        """Login to the platform"""
        pass
    
    @abstractmethod
    async def search_jobs(self, **filters) -> List[Dict[str, Any]]:
        """Search for jobs matching criteria"""
        pass
    
    @abstractmethod
    async def submit_application(self, job: Dict[str, Any], answers: Dict[str, str]) -> bool:
        """Submit job application with answers"""
        pass
    
    @abstractmethod
    async def logout(self) -> bool:
        """Logout from the platform"""
        pass
    
    async def get_job_details(self, job_id: str) -> Optional[Dict[str, Any]]:
        """Get detailed information about a job"""
        logger.info(f"Fetching details for job {job_id}")
        return None
    
    async def detect_application_questions(self, job_posting: str) -> List[str]:
        """Detect questions in application form"""
        if self.qa_engine:
            return await self.qa_engine.detect_questions(job_posting)
        return []
    
    async def generate_answer(self, question: str, job: Dict[str, Any]) -> str:
        """Generate answer for a question"""
        if self.qa_engine:
            return await self.qa_engine.generate_answer(question, job)
        return ""
    
    def log_application(self, job: Dict[str, Any], status: str):
        """Log application attempt"""
        logger.info(f"[{self.name}] Job: {job.get('title')} | Company: {job.get('company')} | Status: {status}")
        self.applications_count += 1
    
    @staticmethod
    def extract_company_name(job: Dict[str, Any]) -> str:
        """Extract company name from job data"""
        return job.get('company', 'Unknown Company')
    
    @staticmethod
    def extract_job_title(job: Dict[str, Any]) -> str:
        """Extract job title from job data"""
        return job.get('title', 'Unknown Title')
    
    @staticmethod
    def extract_location(job: Dict[str, Any]) -> str:
        """Extract location from job data"""
        return job.get('location', 'Remote')
    
    @staticmethod
    def extract_salary(job: Dict[str, Any]) -> Optional[str]:
        """Extract salary information from job data"""
        return job.get('salary')
    
    async def close(self):
        """Clean up resources"""
        if self.browser:
            await self.browser.close()
            logger.info(f"{self.name} browser closed")
