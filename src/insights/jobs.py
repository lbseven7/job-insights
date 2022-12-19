from functools import lru_cache
from typing import List, Dict
import csv


# 1 - Implemente a função read
@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, "r", encoding="utf-8") as read_job:
        data = csv.DictReader(read_job)
        data_list = []
        for row in data:
            data_list.append(row)
    print(data_list)
    return data_list


# 2 - Implemente a função get_unique_job_types
def get_unique_job_types(path: str) -> List[str]:
    read_jobs = read(path)
    filter_job = set()
    for job in read_jobs:
        filter_job.add(job["job_type"])
    return filter_job


# 6 - Implemente a função filter_by_job_type
def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    filter_job_types = list()
    for type in jobs:
        if (type["job_type"] == job_type):
            filter_job_types.append(type)
    return filter_job_types
