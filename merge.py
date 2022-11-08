def merge_sort(unsorted_array):
    if len(unsorted_array) > 1:
        mid = len(unsorted_array) // 2
        left = unsorted_array[:mid]
        right = unsorted_array[mid:]

        merge_sort(left)
        merge_sort(right)
        print(unsorted_array)

        i = j = k = 0
    
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                unsorted_array[k] = left[i]
                i += 1
            else:
                unsorted_array[k] = right[j]
                j += 1
            k += 1
        # print(unsorted_array)

        while i < len(left):
            unsorted_array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            unsorted_array[k] = right[j]
            j += 1
            k += 1

def print_list(array1):
    for i in range(len(array1)):
        print(array1[i], end=" ")
    print()

if __name__== '__main__':
    from random import randint
    array = [randint(1, 1000) for _ in range(10)]
    print("Given array is", end="\n")
    print_list(array)
    merge_sort(array)
    # print("Sorted array is: ", end="\n")
    # print_list(array)