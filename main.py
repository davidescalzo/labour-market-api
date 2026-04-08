from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class AnalyzeRequest(BaseModel):
    query: str
    location: Optional[str] = "Italia"
    posted_within_days: Optional[int] = 30
    keywords: Optional[List[str]] = []
    limit: Optional[int] = 100

@app.get("/")
def home():
    return {"message": "Labour Market API attiva"}

@app.post("/api/jobs/analyze")
def analyze_jobs(req: AnalyzeRequest):
    return {
        "search_summary": {
            "query": req.query,
            "location": req.location,
            "analyzed_jobs": 2
        },
        "top_roles": [
            {"role": "Data Analyst", "count": 12},
            {"role": "Cybersecurity Specialist", "count": 7}
        ],
        "top_skills": [
            {"skill": "Power BI", "count": 8},
            {"skill": "SQL", "count": 6}
        ],
        "seniority_distribution": [
            {"seniority": "junior", "count": 9},
            {"seniority": "senior", "count": 5}
        ],
        "location_distribution": [
            {"location": "Bari", "count": 6},
            {"location": "Lecce", "count": 4}
        ],
        "contract_distribution": [
            {"contract_type": "full_time", "count": 10},
            {"contract_type": "internship", "count": 2}
        ],
        "keyword_frequency": [
            {"keyword": "Power BI", "count": 8},
            {"keyword": "SAP", "count": 3}
        ]
    }
