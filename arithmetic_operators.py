# The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:

# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.

if __name__ == "__main__":
    a = int(input("Enter a number: "))
    b = int(input("Enter second number: "))

    print(f'Sum of {a} and {b} is: {a+b}')
    print(f"Difference of {a} and {b} is: {a-b}")
    print(f"Product of {a} and {b} is: {a*b}")