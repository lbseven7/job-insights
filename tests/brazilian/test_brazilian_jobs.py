from src.pre_built.brazilian_jobs import read_brazilian_file


# 11 - Implemente um teste para a função read_brazilian_file
def test_brazilian_jobs():
    brazilian_job = read_brazilian_file(
        'tests/mocks/brazilians_jobs.csv')
    for job in brazilian_job:
        job["titulo"] = job.pop("title")
        job["salario"] = job.pop("salary")
        job["tipo"] = job.pop("type")
    return brazilian_job

# [{'title': 'Maquinista', 'salary': '2000', 'type': 'trainee'}]
