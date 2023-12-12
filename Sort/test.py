import time
from BubbleSort import bubble_sort
import random
def evaluate_sort(sort='bubble', items=[]):
    print(f"{'*' * 50}")
    print(f'Sort Type: {sort}')
    st = time.perf_counter()
    if sort == "bubble":
        print(f'Sorted Items: {bubble_sort(items)}')
    et = time.perf_counter()
    print(f'Time Taken: {et - st} seconds')
    print(f"{'*' * 50}")


if __name__ == "__main__":
    items = random.sample(range(1,100),5)
    random.shuffle(items)
    print(f"Number of Items:{len(items)}")
    print(f'Unsorted List: {items}')
    evaluate_sort(sort = 'bubble', items=items)
    print(f'Sorted Items')

