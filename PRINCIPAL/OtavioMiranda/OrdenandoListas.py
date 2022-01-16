data1 = [3, 1, 4, 5, 7, 2]
print(data1, "Lista Original")
data1_sorted = sorted(data1)
data1.sort(
    reverse=True
)  # Ordenar uma lista existente sem criar uma nova lista não é uma boa prática
print(data1_sorted, "sorted ()")
print(data1, "sort(reverse=True)")

data2 = [
    {"name": "Product A", "id": 29, "dt1": "2022/01/03"},
    {"name": "Product C", "id": 25, "dt1": "2022/02/"},
    {"name": "Product B", "id": 21, "dt1": "2022/03/"},
    {"name": "Product D", "id": 23, "dt1": "2022/02/"},
    {"name": "Product F", "id": 22, "dt1": "2022/20/"},
    {"name": "Product E", "id": 20, "dt1": "1995/12/22"},
]
