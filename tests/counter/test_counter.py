from src.pre_built.counter import count_ocurrences

# def count_ocurrences(path: str, word: str) -> int:
#     file = open(path, "r")
#     read_data = file.read()
#     word_count = read_data.lower().count(word.lower())
#     return word_count


# 10 - Implemente um teste para a função count_ocurrences
def test_counter():
    assert count_ocurrences('data/jobs.csv', 'Python') == 1639
    assert (count_ocurrences('data/jobs.csv', 'JavaScript')) == 122
    # assert (count_ocurrences('data/jobs.csv', 'lbarbosa')) == 0
