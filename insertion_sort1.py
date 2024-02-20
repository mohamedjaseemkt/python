def insertion_sort(arr):
    for i in range (1,len(arr)):
        key = arr[i]
        j =  i - 1

        while j >= 0 and key < arr[j]:
              arr[j + 1] = arr[j]
              j -= 1

        arr[j + 1] = key


if __name__=="__main__":
    my_array = [32,63,85,47,14,12,36]

print("orginal list: ",my_array)

insertion_sort(my_array)

print("sorted list: ",my_array)


