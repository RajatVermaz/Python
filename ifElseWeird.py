# Task
# Given an integer, n, perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird

if __name__ == "__main__": #  is used to execute some code only if the file was run directly, and not imported.
    n=int(input("Enter a number: ")) 
    if n%2 == 0 and 2<=n<=5: # If n is even and in the inclusive range of 2 to 5, print Not Weird
        print("Not Weird")  
    elif n%2 == 0 and 6<=n<=20: # If n is even and in the inclusive range of 6 to 20, print Weird
        print("Weird")
    elif n%2 == 0 and n>20: # If n is even and greater than 20, print Not Weird
        print("Not Weird")
    else:   # If n is odd, print Weird
        print("Weird")