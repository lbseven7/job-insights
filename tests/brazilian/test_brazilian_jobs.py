from src.pre_built.brazilian_jobs import read_brazilian_file


# 11 - Implemente um teste para a função read_brazilian_file
def test_brazilian_jobs():
    csv = read_brazilian_file('tests/mocks/brazilians_jobs.csv')
    assert 'title' in csv[1] and 'salary' in csv[1] and 'type' in csv[1]
    assert 'titulo' not in csv[1]
    assert 'salario' not in csv[1]
    assert 'tipo' not in csv[1]
    # O dicionário:
    # {"titulo": "Maquinista", "salario": "2000", "tipo": "trainee"}
    # Deve ser traduzido para:
    # {"title": "Maquinista", "salary": "2000", "type": "trainee"}
    print('AQUI RESULTADO ===>', csv[0])
    # {'title': 'Maquinista', 'salary': '2000', 'type': 'trainee'}
