#this is a test


def is_prime(number:int) -> bool:

    #if less than 1
    if number <=1:
        return False
    #if less than 3
    if number <=3:
        return True
    #if divisible by 2 or 3 not prime
    if number % 2 == 0 or number % 3 == 0:
        return False
    #prime test loop
    i = 5
    while i * i <=number:
        if number % i == 0 or number % ( i + 2) == 0:
            return False
        i += 6
    return True
    return 
#print(is_prime(3))
#print(is_prime(50))