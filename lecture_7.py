##Ivys = ['Yale', -1, 'Princeton']
##print(Ivys)
##
##input()
##Ivys[1] = -15
##print(Ivys)

##def showDicts():
##    EtoF = {'one': 'un',
##            'soccer': 'football',
##            'never': 'jamais'}
##    print(EtoF['soccer'])
##
##    input()
####    print(EtoF[0])
##    print(EtoF)
##
##    input()
##    NtoS = {1: 'one',
##            2: 'two',
##            'one': 1,
##            'two': 2}
##    print(NtoS)
##    print(NtoS.keys())
##
##    input()
##    print(NtoS.keys)
##
##    input()
##    del NtoS['one']
##    print(NtoS)
##    input()
##
##    L = [['un', 'one'], ['deux', 'two']]
##    
##showDicts()

# examples of structured code

##import math
##
###Get base
##inputOK = False
##while not inputOK:
##    base = float(input('Enter base: '))
##    if type(base) == type(1.0): inputOK = True
##    else: print('Error. Base must be a floating point number')
##
###Get height
##inputOK = False
##while not inputOK:
##    height = float(input('Enter height: '))
##    if type(height) == type(1.0): inputOK = True
##    else: print('Error. Height must be a floating point number')
##
##hyp = math.sqrt(base*base + height*height)
##
##print('Base:', str(base), ', height:', str(height), ', hyp:', str(hyp))



import math

def getFloat(requestMsg, errorMsg):
    inputOK = False
    while not inputOK:
        val = float(input(requestMsg))
        if type(val) == type(1.0): inputOK = True
        else: print(errorMsg)
    return val

base = getFloat('Enter base: ', 'Error: Base must be a floating point number')
height = getFloat('Enter height: ', 'Error: Height must be a floating point number')

hyp = math.sqrt(base*base + height*height)

print('Base:', str(base), ', height:', str(height), ', hyp:', str(hyp))

def exp1(a, b):
    ans = 1
    while b > 0:
        ans *= a
        b -= 1
