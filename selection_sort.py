# Doesn't seem like a great option, since it's non-adaptive (still requires quadratic time for a mostly sorted list),
# but it has the positive of minimizing the number of swaps. Good for when the cost of swapping items is high.


def selection_sort(array):
    n = len(array)
    for i in range(n):
        current_minimum = i
        for j in range(i + 1, n):
            if array[j] < array[current_minimum]:
                current_minimum = j
        array[i], array[current_minimum] = array[current_minimum], array[i]
    return array


test = [12, 4, 5, 6, 7, 3, 1, 15]
print(selection_sort(test))
