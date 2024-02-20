def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j =i - 1


        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1


        arr[j + 1] = key

if __name__ == "__main__":
    my_array = [59,99,12,96,75,63,24,62,45,98,74,71,25,33]

    print("orginal array: ",my_array) 

    insertion_sort(my_array)

    print("sorted array: ",my_array)