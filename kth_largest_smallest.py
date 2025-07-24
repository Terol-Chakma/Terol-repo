def kth_largest_smallest(arr, k):
    arr_sorted = sorted(arr)
    kth_smallest = arr_sorted[k-1]          
    kth_largest = arr_sorted[-k]        
    return kth_smallest, kth_largest

n = int(input("Enter the number of element: "))
arr= [ ]
for i in range(n):
    num = int(input())
    arr.append(num)
k = int(input("Enter kth element: "))
small, large = kth_largest_smallest(arr, k)
print(f"{k}th smallest: {small}")
print(f"{k}th largest: {large}")
