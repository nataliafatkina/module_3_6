data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(*args):
    total = 0
    for i in args:
        if isinstance(i, (list, set, tuple)):
            for j in i:
                total += calculate_structure_sum(j)
        elif isinstance(i, dict):
            for k, value in i.items():
                total += calculate_structure_sum(k, value)
        elif isinstance(i, int):
            total += i
        elif isinstance(i, str):
            total += len(i)
    return total


result = calculate_structure_sum(data_structure)
print(result)
