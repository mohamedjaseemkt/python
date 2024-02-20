def quick_sort(arr):
    if len(arr) <=1:
        return arr
    
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less)+[pivot]+quick_sort(greater)
    
my_list = [12,36,9,4,38,52,87,7,99]
print("orginal list: ",my_list)

sorted_list = quick_sort(my_list)
print("sorted list: ",sorted_list)