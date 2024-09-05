# ДЗ. Дополнительное задание по модулю 3.
# ============================================
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(data_structure):
    summ_ = 0
        # Прописываем условие при помощи цикла 1 summa для список,кортэж,множества
    if isinstance(data_structure, (list, tuple, set)):
        for item in data_structure:
            summ_ += calculate_structure_sum(item)
            # иначе выполняеться цикл 2 add к summa для- key и value
    elif isinstance(data_structure, dict):
        for key, value in data_structure.items():
            summ_ += calculate_structure_sum(key)
            summ_ += calculate_structure_sum(value)
            # иначе выполняеться действие 3 add к summa - целое число и число с плавающей запятой
    elif isinstance(data_structure, (int, float)):
        summ_ += data_structure
        # иначе выполняеться действие 4 add k summa - фу-цию len
    elif isinstance(data_structure, str):
        summ_ += len(data_structure)
        # возврат из функции значения summ_
    return summ_


result = calculate_structure_sum(data_structure)
print(result)
