import time
from BubbleSort import bubble_sort
from SelectionSort import selection_sort
from InsertionSort import insertion_sort
from MergeSort import merge_sort
import random


def evaluate_sort(sort='bubble', items=[]):
    print(f"{'*' * 50}")
    print(f'Sort Type: {sort}')
    print(f'Unsorted Items: {items}')
    st = time.perf_counter()
    if sort == "bubble":
        st = time.perf_counter()
        print(f'Sorted Items: {bubble_sort(items)}')
    elif sort == "selection":
        st = time.perf_counter()
        print(f'Sorted Items: {selection_sort(items)}')
    elif sort == 'insertion':
        st = time.perf_counter()
        print(f'Sorted Items: {insertion_sort(items)}')
    elif sort == 'merge':
        st = time.perf_counter()
        print(f'Sorted Items: {merge_sort(items)}')
    et = time.perf_counter()
    print(f'Time Taken: {et - st} seconds')
    print(f"{'*' * 50}")


if __name__ == "__main__":
    items = random.sample(range(1, 20000), 10000)
    random.shuffle(items)
    print(f"Number of Items:{len(items)}")
    print(f'Unsorted List: {items}')
    evaluate_sort(sort='bubble', items=items.copy())
    evaluate_sort(sort='selection', items=items.copy())
    evaluate_sort(sort='insertion', items=items.copy())
    evaluate_sort(sort='merge', items=items.copy())
