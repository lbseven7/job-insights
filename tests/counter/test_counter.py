# from src.pre_built.counter import count_ocurrences
from src.pre_built.counter import count_ocurrences


# def count_ocurrences(path: str, word: str) -> int:
#     file = open(path, "r")
#     read_data = file.read()
#     word_count = read_data.lower().count(word.lower())
#     return word_count


# 10 - Implemente um teste para a função count_ocurrences
def test_counter():
    python = count_ocurrences('data/jobs.csv', 'Python')
    javascript = count_ocurrences('data/jobs.csv', 'JavaScript')
    return python, javascript
