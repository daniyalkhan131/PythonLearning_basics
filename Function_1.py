def wish():
	print('happy birthday')

wish()

def return_function():
	return 7**2
	print("hi") #this won't get exec.
	#return pops function off of the call stack
print(return_function())

from random import random as rndm
def flip_coin():
	r=rndm() #generate radom no. between 0-1

	if r>0.5:
		return "heads"
	else:
		return "tails"
def flip_coin():
	r=rndm() #generate radom no. between 0-1

	if r>0.5:
		return "heads".upper()
	else:
		return "tails".upper()
		#this function will overwritten previous

print(flip_coin())

#passing parameters
def square(num):
	return num**2
print(square(3))

def add(a,b):
	return a+b
print(add(1,4))

def sum_odd_num(num):
	ttl=0
	for n in num:
		if n%2!=0:
			ttl+=n
		#return ttl dont do this mistake
	return ttl
print(sum_odd_num([1,2,3,4,5,6,7,8,9]))

# dont use unnecessary else return

#default parameter- if not passed then it uses that and 
#dont throw error, and if passed then overwrite it
def exponent(x,power=2):
	return x**power
print(exponent(3,6))
print(exponent(3))
#default parameter can be anything, function,list,dict,...
def do_add_then_fn(x,y,fn=exponent): #here we give fn as parameter
	z=x+y
	return fn(z)
print(do_add_then_fn(2,3))

def triple(x):
	return x*x*x
print(do_add_then_fn(2,3,triple)) #here passing another fn
# we have to pass parameters in that order only the way written in function

#but can use keyword argument to pass anyway
print(do_add_then_fn(fn=triple,y=3,x=2))
#it gives flexibility
#very useful when passing a dict to a function and unpacking itss values


#Scope
#where are variables can be accessed
#variables created in functions are scoped in that only
#if created outside then function can access them but cannot modify
instructor='Colt'
def hello():
	return f'hello {instructor}'
print(hello())

def hello():
	instructor1='Colt'
	return f'hello {instructor1}'
#print(instructor1)#it will show error

total=0
def increment():
	total+=1
	return total
#print(increment()) #it will error beacue total can be seen
#by function but cannot be modified
# we have to define global to it

total=0
def increment():
	global total
	total+=1
	return total
print(increment())
print(increment())

#nonlocal
#modify parent's variable in a child function
def outer(c):
	count=0
	def inner():
		nonlocal count
		count+=1
		return count
	return inner()
print(outer(5))


#documenting function- use """"""
def hello():
	"""it says hello"""
	return "hello"
print(hello.__doc__) # it shows documentation

from random import randint
print([1,2].pop.__doc__)
print(randint.__doc__)