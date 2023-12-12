import time
from BubbleSort import bubble_sort
from SelectionSort import selection_sort
import random

def evaluate_sort(sort='bubble', items=[]):
    print(f"{'*' * 50}")
    print(f'Sort Type: {sort}')
    st = time.perf_counter()
    if sort == "bubble":
        print(f'Sorted Items: {bubble_sort(items)}')
    elif sort == "selection":
        print(f'Sorted Items: {selection_sort(items)}')
    et = time.perf_counter()
    print(f'Time Taken: {et - st} seconds')
    print(f"{'*' * 50}")


if __name__ == "__main__":
    items = random.sample(range(1,100), 20)
    random.shuffle(items)
    print(f"Number of Items:{len(items)}")
    print(f'Unsorted List: {items}')
    evaluate_sort(sort = 'bubble', items=items)
    evaluate_sort(sort='selection', items=items)
