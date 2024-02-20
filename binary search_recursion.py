def binary_search_recursive(arr,targrt,low,high):
    if low <= high:
        mid = (low + high) //2
        mid_element = arr[mid]

        if mid_element == targrt:
            return mid
        elif mid_element < targrt:
            return binary_search_recursive(arr, targrt, mid + 1, high)
        else: 
            return binary_search_recursive(arr,targrt,low,mid - 1)
    else:
        return -1
    
sorted_list =[9,11,13,15,17,19,21,23,25,27,29,31,33]
target_element = 31

result = binary_search_recursive(sorted_list, target_element, 0, len(sorted_list) -1)

if result != -1:
    print(f"Target element {target_element} found at index {result}.")

else:
    print(f"Target element {target_element} not found in the list.")
