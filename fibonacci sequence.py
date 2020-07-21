def FibRecursion(n):
    if n <= 1:
        return n
    else:
        return (FibRecursion(n - 1) + FibRecursion(n - 2))


numbers = int(input("Enter the numbers? "))  # take input from the user

if numbers <= 0:  # check if the number is valid
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(numbers):
        print(FibRecursion(i))