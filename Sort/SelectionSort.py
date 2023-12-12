def selection_sort(items):
    # Iterate over each element in the list
    for i in range(len(items)):
        # Assume the current element is the minimum in the remaining unsorted array
        min_index = i

        # Iterate over the unsorted portion of the array
        for j in range(i + 1, len(items)):
            # Compare current element with every other element
            if items[j] < items[min_index]:
                # Update the index of the minimum element if a smaller element is found
                min_index = j

        # Swap the current element with the smallest found element in the unsorted portion
        items[i], items[min_index] = items[min_index], items[i]

    # Return the sorted list
    return items
