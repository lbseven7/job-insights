from typing import List, Dict
from src.insights.jobs import read


# 3 - Implemente a função get_unique_industries
def get_unique_industries(path: str) -> List[str]:
    read_jobs = read(path)
    filter_industry = set()
    for industry in read_jobs:
        if (industry["industry"] != ""):
            filter_industry.add(industry["industry"])
    return filter_industry


# 7 - Implemente a função filter_by_industry
def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    filter_industry = list()
    for job_industry in jobs:
        if (job_industry["industry"] == industry):
            filter_industry.append(job_industry)
    return filter_industry
