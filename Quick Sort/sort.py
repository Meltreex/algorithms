students_list = [
    {"name": "Alice", "class": "A", "grade": 88},
    {"name": "Bob", "class": "B", "grade": 77},
    {"name": "Charlie", "class": "B", "grade": 85},
    {"name": "David", "class": "B", "grade": 91},
    {"name": "Eva", "class": "C", "grade": 21},
    {"name": "Frank", "class": "A", "grade": 48},
    {"name": "Grace", "class": "C", "grade": 52},
    {"name": "Hannah", "class": "C", "grade": 33},
    {"name": "Ian", "class": "A", "grade": 79},
    {"name": "Jane", "class": "A", "grade": 21}
]

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        left_subarray = [i for i in array[1:] if i["grade"] <= pivot["grade"]]
        right_subarray = [j for j in array[1:] if j["grade"] > pivot["grade"]]

    return quicksort(left_subarray) + [pivot] + quicksort(right_subarray)

print(quicksort(students_list))