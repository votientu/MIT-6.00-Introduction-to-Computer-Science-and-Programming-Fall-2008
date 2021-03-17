##def squareRootBi(x, epsilon):
##    """Assumes x >= 0 and epsilon > 0
##       Return y s.t. y*y is within epsilon of x"""
##    assert x >= 0, 'x must be non negative, not' + str(x)
##    assert epsilon > 0, 'epsilon must be positive, not' + str(epsilon)
##    low = 0
##    high = max(x, 1)    # For square root of x < 1
##    guess = (low + high)/2.0
##    ctr = 1
##    while abs(guess**2 - x) > epsilon and ctr <= 100:
##        # print('low:', low, 'high:', high, 'guess:', guess)
##        if (guess**2 < x):
##            low = guess
##        else:
##            high = guess
##        guess = (low + high)/2.0
##        ctr += 1
##    assert ctr <= 100, 'iteration count exceeding'
##    print('Bi method. Num. iteration:', ctr, 'estimate:', guess)
##    return guess
##
##def squareRootNR(x, epsilon):
##    """Assumes x >= 0 and epsilon > 0
##       Return y s.t. y*y is within epsilon of x"""
##    assert x >= 0, 'x must be non negative, not' + str(x)
##    assert epsilon > 0, 'epsilon must be positive, not' + str(epsilon)
##    x = float(x)
##    guess = x/2.0
####    guess = 0.001
##    diff = guess**2 - x
##    ctr = 1
##    while abs(diff) > epsilon and ctr <= 100:
####        print('Error:', diff, 'guess:', guess)
##        guess = guess - diff/(2.0*guess)
##        diff = guess**2 - x
##        ctr += 1
##    assert ctr <= 100, 'iteration count exceeding'
##    print('NR method. Num. iteration:', ctr, 'estimate:', guess)
##    return guess
##
##def testBi():
##    print('squareRoot(4, 0.0001)')
##    squareRootBi(4, 0.0001)
##    print('squareRoot(9, 0.0001)')
##    squareRootBi(9, 0.0001)
##    print('squareRoot(2, 0.0001)')
##    squareRootBi(2, 0.0001)
##    print('squareRoot(0.25, 0.0001)')
##    squareRootBi(0.25, 0.0001)
##
##def compareMethods():
##    print('squareRoot(2, 0.01)')
##    squareRootBi(2, 0.01)
##    squareRootNR(2, 0.01)
##    input()
##    print('squareRoot(2, 0.0001)')
##    squareRootBi(2, 0.0001)
##    squareRootNR(2, 0.0001)
##    input()
##    print('squareRoot(2, 0.000001)')
##    squareRootBi(2, 0.000001)
##    squareRootNR(2, 0.000001)
##    input()
##    print('squareRoot(123456789, 0.0001)')
##    squareRootBi(123456789, 0.0001)
##    squareRootNR(123456789, 0.0001)
##    input()
##    print('squareRoot(123456789, 0.000001)')
##    squareRootBi(123456789, 0.000001)
##    squareRootNR(123456789, 0.000001)
##    input()
##    print('squareRoot(2736336100, 0.0000001)')
##    squareRootBi(2736336100, 0.0001)
##    squareRootNR(2736336100, 0.0001)

input()
Techs = ['MIT', 'Cal Tech']
print(Techs)

input()
Ivys = ['Havard', 'Yale', 'Brown']
print(Ivys)

input()
Univs = []
print(Univs)

input()
Univs.append(Techs)
print(Univs)

input()
Univs.append(Ivys)
print(Univs)

input()
for c in Univs:
    print(c)
    for e in c:
        print(e)

input()
Univs = Techs + Ivys
print(Univs)

input()
Ivys.remove('Havard')
print(Univs)
