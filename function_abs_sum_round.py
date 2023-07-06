print(abs(-23))
print(abs(-23.235))
print(abs(float(-23)))

import math
print(math.fabs(-2))#it first convert nm to float then do

#sum
#takes iterable and an optional start as input

print(sum([1,2,3,4,5],start=9))
print(sum([1,2,3,4,5]))

print(sum((1.1,2,3.5,4,5.4)))
print(sum({1,2,3}))
#sum dont work with strings or list of strings
#print(sum('daniyal'))
#print(sum(['danu','khan'],start='lol'))

#round
#we specify ndigits for precision and value
print(round(1.5343))
print(round(1.2343,ndigits=2))
print(round(1.2343,ndigits=None))