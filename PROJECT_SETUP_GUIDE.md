# AI Job Application Agent - Complete Setup Guide

## Project Overview
Dynamic AI-powered job application automation agent with multi-platform support for job sites like Naukri, LinkedIn, Indeed, Remotive, FlexJobs, and more.

## Key Features
- ✅ Multi-platform support (Naukri, LinkedIn, Indeed, Remotive, FlexJobs, etc.)
- ✅ Automated login with credential encryption
- ✅ Dynamic question detection and answer generation
- ✅ Intelligent answer reusability
- ✅ Secure credential storage
- ✅ MFA support (manual)
- ✅ Application tracking and logging
- ✅ AI-powered recruiter question answering

## Quick Start

### 1. Installation
```bash
git clone https://github.com/Kiranreddymk90/ai-job-application-agent.git
cd ai-job-application-agent

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Setup spaCy model
python -m spacy download en_core_web_lg
```

### 2. Configuration
```bash
# Copy example environment file
cp .env.example .env

# Edit .env with your credentials
nano .env
```

### 3. Set Encryption Key
```bash
python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
# Copy the key and paste in .env as ENCRYPTION_KEY
```

## Remaining Files to Create

The following sections provide all the remaining files you need to add to your GitHub repository:

### Core Modules
- `src/core/base_platform.py` - Abstract base class for platforms
- `src/core/profile_analyzer.py` - Resume/profile analysis using NLP
- `src/core/job_matcher.py` - Job recommendation engine
- `src/core/application_tracker.py` - Track applications

### Authentication & Credentials
- `src/auth/credential_manager.py` - Encrypted credential storage
- `src/auth/session_manager.py` - Session/cookie management
- `src/auth/mfa_handler.py` - MFA handling
- `src/auth/account_manager.py` - Multi-account management

### Platform Implementations
- `src/platforms/naukri.py`
- `src/platforms/linkedin.py`
- `src/platforms/indeed.py`
- `src/platforms/remotive.py`
- `src/platforms/flexjobs.py`
- `src/platforms/we_work_remotely.py`
- `src/platforms/remote_co.py`
- `src/platforms/arc_dev.py`

### QA & Answer Generation
- `src/qa_engine/question_detector.py`
- `src/qa_engine/answer_generator.py`
- `src/qa_engine/answer_repository.py`
- `src/qa_engine/profile_context_builder.py`

### Database
- `src/database/models.py` - SQLAlchemy models
- `src/database/connection.py` - DB connection
- `src/database/migrations.py` - Schema migrations

### Configuration Files
- `config/platforms.yaml` - Platform configurations
- `config/profiles.yaml` - User profiles
- `config/recruiter_questions.json` - Question templates
- `config/answer_templates.json` - Answer templates

## Remote Job Sites Covered

1. **Naukri.com** - India's largest job portal
2. **LinkedIn** - Global professional network
3. **Indeed.com** - 200K+ .NET backend remote jobs
4. **We Work Remotely** - Vetted remote-only jobs
5. **Remotive** - 75K+ remote opportunities
6. **FlexJobs** - Hand-curated remote positions
7. **Remote.co** - Community-focused remote board
8. **Arc.dev** - Specialized .NET backend roles
9. **Himalayas.app** - Personalized recommendations
10. **Wellfound** - Startup remote positions

## Architecture Benefits

### Dynamic Question Answering
```python
# System detects:
- "Why are you interested?"
- "Why switch jobs?"
- "Salary expectations?"
- "Relocation willing?"
- Custom role-specific questions

# Generates answers based on:
- User profile (skills, experience, goals)
- Job posting details
- Company information
- Context and history
```

### Secure Credential Management
```python
# Features:
- Fernet encryption for stored credentials
- Per-platform credential isolation
- Automatic session tracking
- Failed login recovery
- Account creation tracking
```

### Answer Reusability
```python
# Knowledge Base:
- Stores successful answers
- Tracks answer effectiveness
- Semantic similarity matching
- Confidence scoring
- Auto-population for similar questions
```

## Next Steps

1. **Clone and Setup**: Follow installation steps above
2. **Create Files**: Add remaining files from documentation
3. **Configure**: Set up .env with your credentials
4. **Test**: Run individual modules first
5. **Customize**: Adapt answer templates for your profile
6. **Deploy**: Set up as cron job or scheduler

## File Download Instructions

All project files are available in the GitHub repository. You can:

1. Clone the entire repository
2. Download as ZIP from GitHub
3. Copy individual files as needed

## Support & Documentation

Refer to the comprehensive documentation for:
- Platform-specific setup
- API configuration
- MFA troubleshooting
- Performance optimization

## License
MIT License - See LICENSE file

## Author
Your Name (Kiranreddymk90)

---

**Last Updated**: December 15, 2025
**Project Version**: 2.0.0
