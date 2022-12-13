from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str, encoding="utf-8") -> List[Dict]:
    with open(path, "r") as read_job:
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
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
