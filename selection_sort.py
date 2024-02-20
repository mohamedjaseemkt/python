def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        main_index = i


        for j in range(i+1,n):
            if arr [j] < arr[main_index]:
                main_index = j

        arr[i],arr[main_index] = arr[main_index],arr[i]

my_list = [32,52,69,74,46,25,14,11]
selection_sort(my_list)
print("sorted list: ",my_list)