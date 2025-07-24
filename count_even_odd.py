def count_even_odd(arr):
    even = 0
    odd = 0
    
    for num in arr:
        if num % 2 ==0:
            even += 1
        else: 
            odd +=1
    return even, odd

arr = [int(x) for x in input("Enter numbers separated by space: ").split()]

even, odd = count_even_odd(arr)
print(f"Even numbers: {even}")
print(f"Odd numbers: {odd}")