def calculate_structure_sum(data_structure):
    total_sum = 0
    total_length = 0
    def process_element(element):
        nonlocal total_sum, total_length
        if isinstance(element, (int, float)):
            total_sum += element
        elif isinstance(element, str):
            total_length += len(element)
        elif isinstance(element, (list, tuple, set)):
            for item in element:
                process_element(item)
        elif isinstance(element, dict):
            for key, value in element.items():
                process_element(key)
                process_element(value)
    for item in data_structure:
        process_element(item)

    print(f"Сумма всех чисел: {total_sum}")
    print(f"Сумма длин всех строк: {total_length}")


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
