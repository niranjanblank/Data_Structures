import time
class LinearSearch:
    def __init__(self, data):
        self.data_list = data
        pass

    def search(self, item_to_search):
        index = 0
        st = time.perf_counter()
        for item in self.data_list:
            if item == item_to_search:
                et = time.perf_counter()
                return f"Item {item_to_search} found at index {index} in {(et - st)*1000} seconds"
            index += 1
        et = time.perf_counter()
        return f"Item {item_to_search} not found in {(et - st)*1000} seconds"


if __name__ == "__main__":
    items = [1,2,3,4,5,23]
    item_to_find = 23
    linear_search = LinearSearch(items)
    print(f"Items:{items}")
    print(f"Item to find: {items}")
    print(linear_search.search(2))
