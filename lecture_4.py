# example code, Lecture 4, Fall 2008

##def sqrt(x):
##    """Returns the square root of x, if x is a perfect square.
##        Prints an error message and returns None otherwise."""
##    ans = 0
##    if x >= 0:
##        while ans*ans < x: ans = ans + 1
##        if ans*ans != x:
##            print(x, 'is not a perfect square')
##            return None
##        else: return ans
##    else:
##        print(x, 'is a negative number')
##        return None
##
##def f(x):
##    x = x + 1
##    return x

##def solve(numLegs, numHeads):
##    for numChicks in range(0, numHeads + 1):
##        numPigs = numHeads - numChicks
##        totLegs = 4 * numPigs + 2 * numChicks
##        if totLegs == numLegs:
##            return [numPigs, numChicks]
##    return [None, None]

##def solve(numLegs, numHeads):
##    for numSpiders in range(0, numHeads + 1):
##        for numChicks in range(0, numHeads + 1 - numSpiders):
##            numPigs = numHeads - numChicks - numSpiders
##            totLegs = 4 * numPigs + 2 * numChicks + 8 * numSpiders
##            if totLegs == numLegs:
##                return [numPigs, numChicks, numSpiders]
##    return [None, None, None]

##def solveAll(numLegs, numHeads):
##    solutionFound = False
##    for numSpiders in range(0, numHeads + 1):
##        for numChicks in range(0, numHeads + 1 - numSpiders):
##            numPigs = numHeads - numChicks - numSpiders
##            totLegs = 4 * numPigs + 2 * numChicks + 8 * numSpiders
##            if totLegs == numLegs:
##                print('Number of pigs:', pigs)
##                print('Number of chickens:', chickens)
##                print('Number of spiders:', spiders)
##                solutionFound = True
##    if not solutionFound: print('There is no solution')
    
##def barnYard():
##    heads = int(input('Enter number of heads: '))
##    legs = int(input('Enter number of legs: '))
##    pigs, chickens, spiders = solve(legs, heads)
##    if pigs == None:
##        print('There is no solution')
##    else:
##        print('Number of pigs:', pigs)
##        print('Number of chickens:', chickens)
##        print('Number of spiders:', spiders)

##def isPalindrome(s):
##    """Return True if s is a palingrome and False otherwise"""
##    if len(s) <= 1: return True
##    else: return s[0] == s[-1] and isPalindrome(s[1:-1])

##def isPalindrome1(s, indent):
##    """Return True if s is a palingrome and False otherwise"""
##    print(indent, indent * ' ',  'isPalindrome1 called with', s)
##    if len(s) <= 1:
##        print(indent, indent * ' ', 'About to return True from base case')
##        return True
##    else:
##        ans = s[0] == s[-1] and isPalindrome1(s[1:-1], indent + indent)
##        print(indent, indent * ' ', 'About to return', ans)
##        return ans

def fib(x):
    """Return fibonacci of x, where x is a non-nagative int"""
    if x == 0 or x == 1: return 1
    else: return fib(x-1) + fib(x-2)

