from typing import Union, List, Dict
from src.insights.jobs import read


# 4 - Implemente a função get_max_salary
def get_max_salary(path: str) -> int:
    read_jobs = read(path)
    salaries = list()
    for salary in read_jobs:
        if (salary["max_salary"].isdigit()):
            salaries.append(int(salary["max_salary"]))
    return max(salaries)


# 5 - Implemente a função get_min_salary
def get_min_salary(path: str) -> int:
    read_jobs = read(path)
    salaries_min = list()
    for salary in read_jobs:
        if (salary["min_salary"].isdigit()):
            salaries_min.append(int(salary["min_salary"]))
    return min(salaries_min)


# 8 - Implemente a função matches_salary_range
def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    # alguma das chaves min_salary ou max_salary estão ausentes no dicionário;
    if ('min_salary' not in job or 'max_salary' not in job):
        raise ValueError('min_salary or max_salary does not exist')
    # alguma das chaves min_salary ou max_salary tem valores não-numéricos;
    if (not str(job['min_salary']).isdigit()
            or not str(job['max_salary']).isdigit()):
        raise ValueError('min_salary or max_salary are not integer values')
    # o valor de min_salary é maior que o valor de max_salary;
    if (int(job['min_salary']) > int(job['max_salary'])):
        raise ValueError('min_salary cannot be higher than the max_salary')
    # o parâmetro salary tem valores não numéricos;
    if (not isinstance(salary, int) and not isinstance(salary, str) or
            (isinstance(salary, str) and not salary.isdigit())):
        raise ValueError('salary is not a integer value')
    # A função deve retornar True se estiver dentro da ou False se não estiver.
    return int(job['min_salary']) <= int(salary) <= int(job['max_salary'])


# 9 - Implemente a função filter_by_salary_range
def filter_by_salary_range(
        jobs: List[dict], salary: Union[str, int]) -> List[Dict]:
    filter_salaries = []
    for job in jobs:
        try:
            if (matches_salary_range(job, salary) is True):
                filter_salaries.append(job)
        except ValueError as exec:
            print(exec)
    return filter_salaries

# jobs = [
#             {"max_salary": 0, "min_salary": 10},
#             {"max_salary": 10, "min_salary": 100},
#             {"max_salary": 10000, "min_salary": 200},
#             {"max_salary": 15000, "min_salary": 0},
#             {"max_salary": 1500, "min_salary": 0},
#             {"max_salary": -1, "min_salary": 10},
#     ]

# filter_salary.append(job)
