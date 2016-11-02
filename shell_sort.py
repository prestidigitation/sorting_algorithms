from insertion_sort import insertion_sort


def shell_sort(array):
    n = len(array)
    gap = len(array) // 2
    while gap > 0:
        for i in range(gap, n):
            val = array[i]
            j = i
            while j >= gap and array[j - gap] > val:
                array[j] = array[j - gap]
                j -= gap
            array[j] = val
        gap //= 2


test = [1, 2, 3, 4, 14, 7, 3, 2, 101, 78]

print(test)
shell_sort(test)
print(test == sorted(test))
