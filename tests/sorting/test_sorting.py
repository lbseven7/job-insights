from src.pre_built.sorting import sort_by


# 12 - Implemente um teste para a função sort_by
def test_sort_by_criteria():
    # Arrange
    jobs = [
        {'date_posted': '2022-11-15', 'max_salary': 30000, 'min_salary': 1500},
        {'date_posted': '2022-11-14', 'max_salary': 18000, 'min_salary': 8000},
        {'date_posted': '2022-11-13', 'max_salary': 12000, 'min_salary': 5000},
    ]
    jobs_min_salary = [
        {'date_posted': '2022-11-15', 'max_salary': 30000, 'min_salary': 1500},
        {'date_posted': '2022-11-13', 'max_salary': 12000, 'min_salary': 5000},
        {'date_posted': '2022-11-14', 'max_salary': 18000, 'min_salary': 8000},
    ]
    jobs_max_salary = [
        {'date_posted': '2022-11-15', 'max_salary': 30000, 'min_salary': 1500},
        {'date_posted': '2022-11-14', 'max_salary': 18000, 'min_salary': 8000},
        {'date_posted': '2022-11-13', 'max_salary': 12000, 'min_salary': 5000},
    ]
    jobs_date_posted = [
        {'date_posted': '2022-11-15', 'max_salary': 30000, 'min_salary': 1500},
        {'date_posted': '2022-11-14', 'max_salary': 18000, 'min_salary': 8000},
        {'date_posted': '2022-11-13', 'max_salary': 12000, 'min_salary': 5000},
    ]

    # Act / Assert
    sort_by(jobs, 'min_salary')
    assert jobs == jobs_min_salary

    sort_by(jobs, 'max_salary')
    assert jobs == jobs_max_salary

    sort_by(jobs, 'date_posted')
    assert jobs == jobs_date_posted
