limit = 1000

def is_prime(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

sum = 0
count = 0
for i in range(2, int(limit+1)):
    if is_prime(i):
        sum = sum + i
        count += 1
print(sum)