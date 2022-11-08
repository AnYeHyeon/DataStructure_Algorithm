def insertionSort(arr):

    for i in range(1, len(arr)):
        print(arr)
        key = arr[i]
        
        j = i-1

        print(key)
        print(i)
        print(j)

        while j >= 0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
        print(arr)    
        arr[j+1] = key
        print(arr)
        print("------------")

arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print("Sorted array is:")
for i in range(len(arr)):
    print("%d" %arr[i])