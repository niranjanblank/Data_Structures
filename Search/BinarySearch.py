def binary_search(data_list, item_to_search):
    data_list = sorted(data_list)
    lower_index = 0
    high_index = len(data_list) - 1
    i = 0
    while lower_index <= high_index:
        # Correct the calculation of middle_index
        middle_index = lower_index + (high_index - lower_index) // 2

        if item_to_search > data_list[middle_index]:
            lower_index = middle_index + 1
        elif item_to_search < data_list[middle_index]:
            high_index = middle_index - 1
        else:
            return f"Item {item_to_search} found"
        i += 1

    return f"Item {item_to_search}"
