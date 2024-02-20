def binary_search(arr,target):
 
    low, high = 0, len(arr) -1

    while low <= high:
        mid = (low + high) //2
        mid_element = arr[mid]

        if mid_element == target:
            return mid
        elif mid_element < target:
            low = mid + 1
        else:
            high = mid - 1

    return - 1

sorted_list = [1,3,5,9,11,13,15,17,19,21,23,25,27,29,31,33]
target_element = 23

result = binary_search(sorted_list,target_element)

if result != -1:
    print(f"Target element {target_element} found at index {result}.")

else:
    (f"Target element {target_element} not found in the list.")