def merge_sort(array):
    # get the length of the array
    length = len(array)
    # base case: if the array has less than 1 element, its already sorted
    if length <= 1: return

    # find the middle index of array to break array into left and right part
    middle = int(length / 2)

    # split the array into two halves
    left_array = array[0:middle]
    right_array = array[middle:]

    # recursively sort both halves
    merge_sort(left_array)
    merge_sort(right_array)

    # merge the sorted halves
    merge(left_array, right_array, array)

    # return the sorted array
    return array
def merge(left_array, right_array, array):
    # calculate sizes of the left and right array
    left_size = int(len(array) / 2)
    right_size = len(array)- left_size

    # initialize integers for traversing the arrays
    # i for main array, l for left array, r for right array
    i,l,r = 0,0,0

    # merge the two arrays until one of them is empty
    while (l <left_size and r<right_size):
        # compare elements from both arrays and merge them in sorted order
        if left_array[l] < right_array[r]:
            array[i] = left_array[l]
            i+=1
            l+=1
        else:
            array[i] = right_array[r]
            i+=1
            r+=1

    # if there are remaining elements in the left array, add them to the list
    while l< left_size:
        array[i] = left_array[l]
        i+=1
        l+=1

    # if there are remaining elements in the right array, add them to the list
    while r<right_size:
        array[i] = right_array[r]
        i += 1
        r += 1

print(merge_sort([8,2,3,5,1,7,6]))