def merge_sort(arr):
    if len(arr)<=1:
        return arr
    

    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]


    #recursion = function calling it self
    left = merge_sort(left)
    right = merge_sort(right)


    return merge(left,right)


def merge(left,right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


my_list = [12,65,48,19,36,45,65,33,48,97,85,53]
print("orginal list: ",my_list)

sorted_list = merge_sort(my_list)

print("sorted list: ",sorted_list)
              
