def binary_search(arr, target):
    low_index = 0
    high_index = len(arr) - 1

    while low_index <= high_index:

        mid_index = (low_index + high_index) // 2
        if target == arr[mid_index]:
            return mid_index
        elif target > arr[mid_index]:
            low_index = mid_index + 1
        else:
            high_index = mid_index - 1
    return None


print(binary_search([1, 2, 3, 4, 5], 6))
