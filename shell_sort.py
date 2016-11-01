from insertion_sort import insertion_sort


def shell_sort(array):
    n = len(array)
    h = 1
    while h < n:
        h = 3 * h + 1
    while h > 0:
        h //= 3
        for k in range(1, h):
            insertion_sort(array[k:h:n])


test = [1, 2, 3, 4, 14, 7, 3, 2, 101, 78]
print(shell_sort(test) == sorted(test))
