#reverse returns an reversed iterator
l=[1,2,3,4,5]
l.reverse()
print(l) #it is list method , inplace

print(reversed([1,2,3,4,5])) #returns object

print(list(reversed([1,2,3,4,5])))


print('helloworld'[::-1])
for i in reversed('helloworld'):
	print(i,end='')
print()
#or
print(''.join(list(reversed('helloworld'))))