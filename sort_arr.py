def arr_sort(arr):
    l = len(arr)
    for i in range(l - 1):
        for j in range(l - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = [int(x) for x in input("Enter numbers separated by space: ").split()]
result = arr_sort(arr)
print("The Sorted Array: ",result)