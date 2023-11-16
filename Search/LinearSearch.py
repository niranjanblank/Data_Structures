def linear_search(data_list, item_to_search):
    index = 0

    for item in data_list:
        if item == item_to_search:

            return f"Item {item_to_search} found"
        index += 1
    return f"Item {item_to_search} not found"



