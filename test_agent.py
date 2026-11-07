import pytest
from app.bob_agent import IBMBobAgent

def test_pii_redaction():
    text_with_phone = "My phone number is +91 9845012345 and email test@gmail.com"
    sanitized = IBMBobAgent.redact_pii(text_with_phone)
    assert "[PROTECTED PHONE NUMBER]" in sanitized
    assert "[PROTECTED EMAIL]" in sanitized
    assert "9845012345" not in sanitized

def test_multilingual_job_match():
    dummy_jobs = [
        {
            "id": "1",
            "title_en": "EV Battery Technician",
            "title_kn": "ಇವಿ ಬ್ಯಾಟರಿ ತಂತ್ರಜ್ಞ",
            "title_hi": "ईवी बैटरी तकनीशियन",
            "category": "Clean Tech & Electric Vehicles",
            "languages": ["Kannada", "English"]
        },
        {
            "id": "2",
            "title_en": "Silk Handloom Retail",
            "title_kn": "ರೇಷ್ಮೆ ಮಾರಾಟ",
            "title_hi": "सिल्क बिक्री",
            "category": "Retail",
            "languages": ["Kannada", "Hindi"]
        }
    ]
    
    matches = IBMBobAgent.match_jobs("ಇವಿ ಬ್ಯಾಟರಿ", dummy_jobs, preferred_lang="kn")
    assert len(matches) > 0
    assert matches[0]["id"] == "1"

def test_skill_gap_analysis():
    target_job = {
        "title_en": "EV Technician",
        "company": "Nandi Mobility",
        "required_skills": ["Basic Electrical Knowledge", "Battery Cell Testing"]
    }
    skills_db = {
        "skills_matrix": {
            "Basic Electrical Knowledge": {
                "level": "Foundational",
                "learning_roadmap": [{"step": 1, "topic": "AC/DC basics", "duration": "3 days", "provider": "ITI"}]
            }
        },
        "local_skilling_centers": [{"name": "Peenya ITI", "location": "Peenya", "specialization": "EV", "tuition": "Free"}]
    }
    
    analysis = IBMBobAgent.analyze_skill_gap(
        user_skills=["Basic Electrical Knowledge"],
        target_job=target_job,
        skills_db=skills_db
    )
    
    assert analysis["current_fit_score"] == 50
    assert "Battery Cell Testing" in analysis["missing_skills"]
    assert len(analysis["bob_custom_curriculum"]) == 1

if __name__ == "__main__":
    test_pii_redaction()
    test_multilingual_job_match()
    test_skill_gap_analysis()
    print("All OpportunityBob Agent tests passed successfully!")
