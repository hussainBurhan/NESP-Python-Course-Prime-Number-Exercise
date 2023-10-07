# Taking integer type input from user
num = int(input("Enter a number to find out is it a prime number or not : "))

# Checking if the input number is greater than 1
if num > 1:
    # Loop to iterate through numbers from 2 to (num - 1)
    for i in range(2, num):
        # If num is divisible by i, it's not a prime number
        if num % i == 0:
            print(f"{num} is not a prime number")
            print(f"{i} times, {num//i} is {num}")
            break
    else:
        # If no factors were found, num is a prime number
        print(f"{num} is a prime number")
        
else:
    # If num is less than or equal to 1, it's not a prime number
    print(f"{num} is not a prime number")
