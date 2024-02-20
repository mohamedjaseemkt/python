def linear_search(arr,target):
    """
    perform linear search to find the target element in the list.

    parameters:
    - arr: the list to be searched.
    - target: the element to be searched for.

    returns:
    - if the taget is found, ruturns the index of the first occurrence.
    - if the target is not found, returns -1. 

    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i # target found at index i
    return -1 # target not found in the list

my_list = [3,5,4,99,8,6,4,7,1,81,33,55]
target_element = 7

result = linear_search(my_list,target_element)

if result != -1:
    print(f"Target element {target_element} found at index {result}.")
else:
    print(f"Target element {target_element} not fount the list.")