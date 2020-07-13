import time, threading

def num_divisors(num):
    i = 1
    count = 0
    while i <= num:
        if num % i == 0:
            count += 1
        i += 1
    return count

def isPrime(num):
    # A prime number has only two divisors, 1 and itself
    if num_divisors(num) == 2:
        return True
    return False

num = int(input("Enter a number:\n"))


t1  = time.time()

if isPrime(num):
    print("{} is Prime".format(num))
else:
    print("{} is not Prime".format(num))
t2 = time.time()
print(t2 - t1)

t3 = time.time()

for i in range(2, num):
    if num % i == 0:
        print("{} is not prime".format(num))
        break
else:
    print("{} is prime".format(num))
t4 = time.time()
print(t4 - t3)
        

