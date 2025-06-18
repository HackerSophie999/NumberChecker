# a divisor is something a number can be divided by
# 12 has the divisors; 1, 2, 3, 4, 6

# a prime number only has one divisor, 1

# an abundant number is one where 
# the sum of its divisors is greater than the number

# a perfect number is one where
# the sum of its divisors is equal to the number


num = int(input("what is your number: "))

divisors = []
total = 0

for i in range(1,num):
    if num % i == 0:
        divisors.append(str(i))
        total = total + i
        divisors.append("+")

del divisors[-1]
    
print(" ".join(divisors), "=", total)

if total == num:
    print("It is a perfect number")

if total > num:
    print("It is an abundant number")

if total == 1:
    print("It is a prime number")

# Palindrome 
word = str(num)
reversedWord = word[::-1]
print('Youre reversed number is',reversedWord)
if word == reversedWord:
    print('It is a Palindrome')

# Even or odd
if num % 2 == 0:
   print(num, 'is even')
else :
   print(num,'is odd')

#self-dividing
def is_self_dividing(n):
    for digit in str(n):
        if digit == '0' or n % int(digit) != 0:
            return False
    return True
selfnum = is_self_dividing(num)
if selfnum == True:
    print("And it is a self-dividing number")
