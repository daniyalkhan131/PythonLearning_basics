#higher order functions

#functions that returns another functions from inside or accepts
#a function as arg.

def sum(n,func):
	total=0
	for num in range(1,n+1):
		total+=func(num)
	return total
def square(x):
	return x*x
def cube(x):
	return x*x*x

print(sum(3,square))
print(sum(3,cube))

#nesting a function inside another function
from random import choice
def greet(person):
	def get_mood():
		msg=choice(('hello there ','go away ','i love u '))
		return msg

	result=get_mood()+person
	return result

print(greet('toby'))

#now functn calling and returning function

from random import choice
def make_laugh_func():
	def get_laugh():
		l=choice(('hahaha','lol','tehehehe'))
		return l
	return get_laugh
laugh=make_laugh_func()
print(laugh())

print()
#inner functions can access outer function scope
from random import choice
def make_laugh_at_func(person):
	def get_laugh():
		l=choice(('hahaha','lol','tehehehe'))
		return f"{l} {person}"
		#here we are returning person that is outer function scope
	return get_laugh
laugh_at=make_laugh_at_func('linda')
print(laugh_at())
print(laugh_at())
print(laugh_at())

print()
#decorators are functions that wrap other functions and enhance
#their behavior
#Decorators are examples of higher order functions 
#Decorators have their own syntax, using "@" (syntactic sugar)

def be_polite(fn):
	def wrapper():
		print("what a pleasure to meet you!")
		fn()
		print("have a great day!")
	return wrapper
	#wrapper add something to the function greet here
def greet():
	print("my name is danu")
def rage():
	print("i hate you")

greet=be_polite(greet)
greet()
greet()
polite_rage=be_polite(rage)
polite_rage()

print()
#nnow doing this with syntactic sugar @ sign
#python automatically take care of that
#it helps us creating decorator faster

@be_polite #this is our wrapper we want to add
def go_away(): #and in this we want to add so we do like this
	print("go away from here")
#ow we dont need to do go_away=be_polite(go_away)
go_away()


print()
#till now decorated function did'nt accept arg.
#but now we give arg to decorated fn like greet (not decorator fn)
def shout(fn):
	def wrapper(name):
		return fn(name).upper()
	return wrapper

@shout
def greet(name):
	return f"Hi, I'm {name}."
@shout
def order(main,side):
	return f"Hi, I'd like the {main}, with a side of {side}, please"

print(greet("todd"))
#print(order('burger','fries')) it print error as wrapper only
#take one agr and two were given

#so for this we use args and kwargs
#it gives decorator function more flexibility

def shout(fn):
	def wrapper(*args,**kwargs):
		return fn(*args,**kwargs).upper()
	return wrapper

@shout
def greet(name):
	return f"Hi, I'm {name}."
@shout
def order(main,side):
	return f"Hi, I'd like the {main}, with a side of {side}, please"
@shout
def lol():
	return "lol"

print(greet("todd"))
print(order('burger','fries'))
print(lol())
#can do like
print(order(main='burger',side='fries'))#kwargs will take care of this


print()
#using wrapper to preserve meta data

def log_function_data(fn):
	def wrapper(*args, **kwargs):
		"""I AM A WRAPPER FUNCTION"""
		print((f"you are about to call {fn.__name__}"))
		print((f"documentation {fn.__doc__}"))
		return fn(*args,**kwargs)
	return wrapper
@log_function_data
def add(x,y):
	"""ADD TWO NUMBERS"""
	return x+y

print(add(10,40))
#problem is that when we want to read add docs then it shows
#of that of wrapper functn
print(add.__doc__)
print(add.__name__)
print(help(add))
#if other people are working with our code then this will create
#a problem

#so there is simple way of preserving meta data
#wraps form functools
print('--------------')
from functools import wraps
def log_function_data(fn):
	@wraps(fn)
	def wrapper(*args, **kwargs):
		"""I AM A WRAPPER FUNCTION"""
		print((f"you are about to call {fn.__name__}"))
		print((f"documentation {fn.__doc__}"))
		return fn(*args,**kwargs)
	return wrapper
@log_function_data
def add(x,y):
	"""ADD TWO NUMBERS"""
	return x+y
#now we can see the add functn docs n ol
print(add.__doc__)
print(add.__name__)
print(help(add))


print("-------------")
#building a speed test decorator

#we check speed of suming the list element vs generator element
#so here we wraps our function sum with speed test code
#it will return how much time both take

from math import fsum #we use this because sum we defined above
from functools import wraps
from time import time
def speed_test(fn):
	@wraps(fn)
	def wrapper(*args, **kwargs):
		start_time=time()
		result = fn(*args, **kwargs)
		end_time = time()
		print(f"executing {fn.__name__}")
		print(f"Time Elapsed: {end_time-start_time}")
		return result
	return wrapper

@speed_test
def sum_nums_list():
	return fsum([x for x in range(50000)])
@speed_test
def sum_nums_gen():
	return fsum(x for x in range(50000))
print(sum_nums_list())
print(sum_nums_gen())

print('------------------')
#we can use decorators to enforce certain restrictions on 
#arguments

#like we dont want args using keywords
from functools import wraps
def ensure_no_kwargs(fn):
	@wraps(fn)
	def wrapper(*args, **kwargs):
		if kwargs:
			raise ValueError("No kwargs allowed! sorry")
		return fn(*args,**kwargs)
	return wrapper
@ensure_no_kwargs
def greet(name):
	print(f"hi there {name}")
greet("Tony")
#greet(name="Tony") #it show valueerror



print("-----------")
#now decorator takes an argument value
#we do this when we want something to be fixed argument
#we can also use decorator when we want to put some restriction
#on the functions....

#when we write
#@decorator
#def func(*args,**kwargs):
#	pass
#we mean this
#func=decorator(func)

#when we write this
#@decorator(arg)
#def func(*args,**kwargs):
#	pass
#we mean this
#func=decorator(arg)(func)

from functools import wraps
def ensure_first_arg_is(val):
	def inner(fn):
		@wraps(fn)
		def wrapper(*args,**kwargs):
			if args and args[0] !=val:
				return f"First arg need to be {val}"
			return fn(*args,**kwargs)
		return wrapper
	return inner

@ensure_first_arg_is("burrito")
def fav_food(*foods):
	print(foods)
print(fav_food("burrito","ice cream"))
print(fav_food("milk","ice cream"))

@ensure_first_arg_is(10)
def add_to_ten(num1,num2):
	return num1+num2
print(add_to_ten(10,12))
print(add_to_ten(1,2))


print("---------------------")
#enforcing argument types with a decorator
def enforce(*types):
	def decorator(f):
		def new_func(*args,**kwargs):
			#convert args to something mutable
			newargs=[]
			for (a,t) in zip(args,types):
				newargs.append(t(a))
			return f(*newargs, **kwargs)
		return new_func
	return decorator

@enforce(str,int)
def repeat_msg(msg,times):
	for time in range(times):
		print(msg)
repeat_msg("hello",'3')

@enforce(float,float)
def divide(a,b):
	return a/b
print(divide(2,9))
print(divide('2','9'))