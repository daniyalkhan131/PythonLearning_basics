#all prints true when all are true or empty iterable
print(all([0,1,2,3,4,5]))  #0 is falsy
print(all([0,0,0,0]))
print(all([1,2,3,4,5]))

print([char for char in 'eio' if char in 'aeiou'])
print(all([char for char in 'eio' if char in 'aeiou']))

names=['danu','dany','daniyal','daniyalkhan']
print([char[0]=='d' for char in names])
print(all([char[0]=='d' for char in names]))

names.append('naj')
print([char[0]=='d' for char in names])
print(all([char[0]=='d' for char in names]))

#any returns true when any of element in iterable is true,
#but for emplty it returns false

print(all(name[0]=='d' for name in names))
#(char[0]=='d' for char in names) this is generator expression
#like lighter version of list
#if we dont want list like in all and any(only want result) we can use this
#it dont waste memory

import sys
list_comp=sys.getsizeof([x*10 for x in range(1000)])
gen_exp=sys.getsizeof(x*10 for x in range(1000))

print('to do same things, it takes...')
print(f'list comprehension {list_comp} bytes')
print(f'generator expr {gen_exp} bytes')

