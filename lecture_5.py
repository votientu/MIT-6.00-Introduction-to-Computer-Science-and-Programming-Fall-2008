def squareRootBi(x, epsilon):
    """Assumes x >= 0 and epsilon > 0
       Return y s.t. y*y is within epsilon of x"""
    assert x >= 0, 'x must be non negative, not' + str(x)
    assert epsilon > 0, 'epsilon must be positive, not' + str(epsilon)
    low = 0
    high = x
    guess = (low + high)/2.0
    ctr = 1
    while abs(guess**2 - x) > epsilon and ctr <= 100:
        # print('low:', low, 'high:', high, 'guess:', guess)
        if (guess**2 < x):
            low = guess
        else:
            high = guess
        guess = (low + high)/2.0
        ctr += 1
    assert ctr <= 100, 'iteration count exceeding'
    print('Bi method. Num. iteration:', ctr, 'estimate:', guess)
    return guess
