def find_largest_smallest():
    num = []
    
    for i in range(10):
        n = int(input(f"Enter number {i+1}: "))
        num.append(n)
    
    largest = num[0]
    smallest = num[0]
    
    for n in num[1:]:
        if n > largest:
            largest = n
        if n < smallest:
            smallest = n

    print("The entered numbers are:", num)
    print("The largest number is:", largest)
    print("The smallest number is:", smallest)

find_largest_smallest()
