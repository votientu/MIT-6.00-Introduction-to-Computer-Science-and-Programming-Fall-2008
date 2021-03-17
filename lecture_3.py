# example code, Lecture 3, Fall 2008

# find the square root of a perfect square
##x = 123456
##ans = 0
##while ans * ans < x:
##    ans = ans + 1
##print(ans)

##ans = 0
##if x >= 0:
##    while ans*ans < x:
##        ans = ans + 1
##        print('ans =', ans)
##    if ans*ans != x:
##        print(x, 'is not a perfect square')
##    else: print(ans)
##
##else: print(x, 'is a negative number')

##x = 10
##i = 1
##while i < x:
##    if x % i == 0:
##        print('divisor ', i)
##    i = i + 1

##x = 10
##for i in range(1, x):
##    if x % i == 0:
##        print('divisor ', i)

##x = 100
##divisors = []
##for i in range(1, x):
##    if x % i == 0:
##        divisors = divisors + [i]
##print('divisors', divisors)

##x = 17
##for ans in range(0, x):
##    if ans * ans < x:
##        print('ans =', ans)
##    elif ans * ans != x:
##        print(x, 'is not a perfect square')
##        break
##    else:
##        print(ans)
##        break

##s1 = 'abcdefg'
##s2 = 'hijklmn'
##
##print(s1 + s2)

sumDigits = 0
for c in str(1952):
    sumDigits += int(c)
print(sumDigits)
