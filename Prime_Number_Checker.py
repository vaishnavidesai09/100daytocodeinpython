# PRIME NUMBER CHECKER
number = int(input("Enter a number: ")  )
def prime_number(number):
    is_prime = True
    for i in range(2,number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number")
    else:
        print("It's not a prime number")

        
prime_number(number)            
