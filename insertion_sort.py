# Insertion sort is a good choice when an array is nearly sorted, due to it being adaptive, or when the problem size
# is small, since it has low overhead.
# Because of these reasons, and being stable, it's often used as the recursive base case for smaller subsets in higher
# overhead divide-and-conquer algorithms like quicksort and mergesort.


def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        print("Loop ", i)
        j = i
        while j > 0 and array[j - 1] > array[j]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1


test = [1, 2, 3, 4, 14, 7, 3, 2, 101, 78]
insertion_sort(test)
print(test)
