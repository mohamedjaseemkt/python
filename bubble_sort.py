def bubble_sort(arr):
    n = len(arr)

    for i in range(n): 
        #i= to perform loop according to the length of given list and travers through all element
        for j in range(0,n-i-1):
            # j = associated with the index of the list and to compare and swap values of the indexes 
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

my_list = [26,11,48,67,15,45,55,77,93,49,33,99,19,84,23,86,63]
print("orginal list:",my_list)

bubble_sort(my_list)

print("sorted list: ",my_list)
