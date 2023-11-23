def interpolation_search(data_list, item_to_search):
    high = len(data_list) - 1
    low = 0
    while (low <= high) and (item_to_search >= data_list[low]) and (item_to_search <= data_list[high]):
        # Avoid division by zero
        if data_list[high] == data_list[low]:
            if data_list[low] == item_to_search:
                return f"Item {item_to_search} found"
            break

        # Calculate the probe position
        pos = low + ((high - low) * (item_to_search - data_list[low]) // (data_list[high] - data_list[low]))

        # Check if item is at pos
        if data_list[pos] == item_to_search:
            return f"Item {item_to_search} found"
        elif data_list[pos] < item_to_search:
            low = pos + 1
        else:
            high = pos - 1

    return f"Item {item_to_search} not found"

if __name__ == "__main__":
    items = range(1,20)
    item_to_find = 15
    print(f"Number of Items:{len(items)}")
    print(f"Item to find: {item_to_find}")
    print(interpolation_search(items, item_to_find))