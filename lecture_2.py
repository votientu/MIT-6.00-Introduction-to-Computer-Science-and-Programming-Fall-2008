# sample code for use in Lecture 2, Fall 2008

##x = 3   # Create variable x and assign value 3 to it
##x = x*x # Bind x to value 9
##print(x)
##
##n = input('Enter a number: ')
##print(n)
### print(n/n)

##x = 15
##if x%2 == 0:
##    print('Even')
##else: print('Odd')

##z = 'b'
####if 'x' < z:
####    print('Hello')
####    print('Mom')
##if 'x' < z:
##    print('Hello')
##print('Mom')

##x = 15
##y = 13
 ##z = 11
##print(x, y, z)
##### Is this right?
####if x < y:
####    if x < z: print('x is least')
####    else: print('z is least')
####else: print('y is least')
####
##if x < y and x < z: print('x is least')
##elif y < z: print('y is least')
##else: print('z is least')

y = 0
x = 3
itersLeft = x
while itersLeft > 0:
    y = y + x
    itersLeft = itersLeft - 1
    print('y =', y, 'itersLeft =', itersLeft)
print(y)

