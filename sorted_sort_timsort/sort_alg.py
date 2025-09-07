import timeit
import random

def insertion_sort(lst):
    n = len(lst)
    for i in range(1, n):
        k = lst[i]
        for j in range(i):
            if lst[j] >= lst[i]:
                for m in range(i, j - 1, -1):
                    if m == j:
                        lst[m] = k
                    else:
                        lst[m] = lst[m - 1]
                break

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи,
		# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

def random_data(size):
    return [random.randint(0, size) for _ in range(size)]

for i in range(0, 4):
    insertion_stmt = "insertion_sort(data.copy())"
    merge_stmt = "merge_sort(data.copy())"
    timsort_stmt = "sorted(data.copy())"
    setup_code = "data=random_data({size})"
    if i == 0:
        insertion_timeit = timeit.timeit(insertion_stmt, globals=globals(), setup=setup_code.format(size=1000), number=1)
        merge_timeit = timeit.timeit(merge_stmt, globals=globals(), setup=setup_code.format(size=1000), number=1)
        sorted_timeit = timeit.timeit(timsort_stmt, globals=globals(), setup=setup_code.format(size=1000), number=1)
        print(f"Insertion sort : {insertion_timeit:.6f} сек Розмір 1000")
        print(f"Merge sort: {merge_timeit:.6f} сек Розмір 1000")
        print(f"Sorted sort: {sorted_timeit:.6f} сек Розмір 1000")
    if i == 1:
        insertion_timeit = timeit.timeit(insertion_stmt, globals=globals(), setup=setup_code.format(size=10000), number=1)
        merge_timeit = timeit.timeit(merge_stmt, globals=globals(), setup=setup_code.format(size=10000), number=1)
        sorted_timeit = timeit.timeit(timsort_stmt, globals=globals(), setup=setup_code.format(size=10000), number=1)
        print(f"Insertion sort : {insertion_timeit:.6f} сек Розмір 10000")
        print(f"Merge sort: {merge_timeit:.6f} сек Розмір 10000")
        print(f"Sorted sort: {sorted_timeit:.6f} сек Розмір 10000")
    if i == 2:
        insertion_timeit = timeit.timeit(insertion_stmt, globals=globals(), setup=setup_code.format(size=100000), number=1)
        merge_timeit = timeit.timeit(merge_stmt, globals=globals(), setup=setup_code.format(size=100000), number=1)
        sorted_timeit = timeit.timeit(timsort_stmt, globals=globals(), setup=setup_code.format(size=100000), number=1)
        print(f"Insertion sort : {insertion_timeit:.6f} сек Розмір 100000")
        print(f"Merge sort: {merge_timeit:.6f} сек Розмір 100000")
        print(f"Sorted sort: {sorted_timeit:.6f} сек Розмір 100000")
    if i == 3:
        insertion_timeit = timeit.timeit(insertion_stmt, globals=globals(), setup=setup_code.format(size=1000000), number=1)
        merge_timeit = timeit.timeit(merge_stmt, globals=globals(), setup=setup_code.format(size=1000000), number=1)
        sorted_timeit = timeit.timeit(timsort_stmt, globals=globals(), setup=setup_code.format(size=1000000), number=1)
        print(f"Insertion sort : {insertion_timeit:.6f} сек Розмір 1000000")
        print(f"Merge sort: {merge_timeit:.6f} сек Розмір 1000000")
        print(f"Sorted sort: {sorted_timeit:.6f} сек Розмір 1000000")
