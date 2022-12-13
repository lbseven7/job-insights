from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, "r", encoding="utf-8") as read_job:
        data = csv.DictReader(read_job)
        data_list = []
        for row in data:
            data_list.append(row)
    return data_list


def get_unique_job_types(path: str) -> List[str]:
    read_jobs = read(path)
    filter_job = set()
    for job in read_jobs:
        filter_job.add(job["job_type"])
    return filter_job


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    filter_job_types = list()
    for type in jobs:
        if (type["job_type"] == job_type):
            filter_job_types.append(type)
    return filter_job_types
