from LinearSearch import linear_search
from BinarySearch import binary_search
from InterpolationSearch import interpolation_search
from random import randint, choice

import time


def evaluate_search(search='linear', items=[], item_to_find=None):
    print(f"{'*' * 50}")
    print(f'Search Type: {search}')
    st = time.perf_counter()
    if search == "linear":
        print(linear_search(items, item_to_find))
    elif search == "binary":
        print(binary_search(items, item_to_find))
    elif search == "interpolation":
        print(binary_search(items, item_to_find))
    et = time.perf_counter()
    print(f'Time Taken: {et - st} seconds')
    print(f"{'*' * 50}")


if __name__ == "__main__":
    items = list(range(100000000,0,-1))
    item_to_find = choice(items)
    print(f"Number of Items:{len(items)}")
    print(f"Item to find: {item_to_find}")
    evaluate_search(search = 'linear', items=items, item_to_find=item_to_find)
    evaluate_search(search = 'binary', items=items, item_to_find=item_to_find)
    evaluate_search(search = 'interpolation', items=items, item_to_find=item_to_find)

