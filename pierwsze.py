while True:
    num = int(input("Enter a positive number to see if it's a prime number: "))
    if num > 1:
        break
    elif num == 1:
        print("1 is technically not a prime number.")
    else:
        print("Number cannot be negative- try again.")

for num1 in range(2,num):
    div = num%num1
    count = 0
    if div == 0:
        print(num1,"is a divisor of",num,"... stopping.")
        print(num,"is not a prime number.")
        break
    else:
        count += 1
        print(num1,"is NOT a divisor of",num,"... continuing")

if count == 1:
    print(num,"is a prime number!")