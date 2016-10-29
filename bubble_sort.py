# Overall the worst of the sorting algorithms. Best case is O(n) if array is already sorted (have to include "sorted"
# Boolean). Average and worst case are both O(n^2). Best use case would be smaller arrays that are nearly pre-sorted.
# Insertion sort is preferred over bubble sort for sorting smaller arrays.


def bubble_sort(a):
    n = len(a)
    for i in range(n):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


# Can optimize bubble sort by keeping track of whether any changes were made to the array during a given run.
# This keeps the algorithm from iterating through all possible comparisons if the array is already sorted.
def bubble_sort_optimized(a):
    n = len(a)
    for i in range(n):
        flag = False
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                flag = True
                a[j], a[j + 1] = a[j + 1], a[j]
        if flag is not True:
            break


test = [12, 4, 5, 6, 7, 3, 1, 15]
test = bubble_sort(test)
print(test)

test2 = [12, 4, 5, 6, 7, 3, 1, 15]
print(test2)

print(sorted([1, 2, 3, 4, 6, 5, 7, 8, 9, 10, 11, 13, 12, 14, 15, 16, 17, 18, 20, 19]) \
      == bubble_sort_optimized([1, 2, 3, 4, 6, 5, 7, 8, 9, 10, 11, 13, 12, 14, 15, 16, 17, 18, 20, 19]))
