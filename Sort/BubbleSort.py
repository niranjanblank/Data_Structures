def bubble_sort(item):
    # outer loop for multiple passes through the list
    for i in range(len(item)):
        # inner loop to perform pairwise comparisons and swaps
        for j in range(len(item)-1):
            # compare adjacent items
            if item[j] > item[j+1]:
                # swap the two items if they are in the wrong order
                temp = item[j]
                item[j] = item[j+1]
                item[j+1] = temp
    return item

