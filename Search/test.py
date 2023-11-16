from LinearSearch import linear_search
import time

if __name__ == "__main__":
    items = [1, 2, 3, 4, 5, 23]
    item_to_find = 57
    print(f"Items:{items}")
    print(f"Item to find: {items}")
    st = time.perf_counter()
    print(linear_search(items, item_to_find))
    et = time.perf_counter()
    print(f'Time Taken: {st-et} seconds')