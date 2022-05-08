arr = [2, 4, 1, 6, 8, 9, 0, -1]


def sort_array(array: list):
    new_arr = []
    min_value = array[0]
    min_index = 0
    for i in range(1, len(array)):
        if array[i] < min_value:
            min_value = array[i]
            min_index = i
    print(min_value, min_index)


sort_array(arr)
