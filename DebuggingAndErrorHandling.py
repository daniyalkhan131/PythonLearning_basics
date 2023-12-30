#we all make mistakes all the time
#sometimes mistakes made by us, or sometimes services are not running like connecting 
#to database

#syntax error- typos or not knowing
#nameError- when variable not defined
#TypeError-operatn aplied to wrong type
#indexError-out of range accessing list or string etc
#ValueError- occur when built-in operatn or function recieves arg. that has right type but
#an inappropiate value eg. int('f')
#keyError- when dictioary dont have that key
#AttributeError- like "".hello(), string dont have helo()
#there are many types of errors more


#raise your error
#raise ValueError('invalid value dear')
#raise NameError('blah')
#we can raise any error whenever we want whereever we want
def colorize(text, color):
	colors={'red','green','blue'}
	if type(color) is not str:
		raise TypeError("color must be a str")
	if type(text) is not str:
		raise TypeError("text must be a str")
	if color not in colors:
		raise ValueError("color not present")
	print(f"Printed {text} in {color}")

colorize("hello","red")
#colorize(34,"red")
#colorize("hello","orange")
#colorize([],43)



#handling errors
try:
	foobar
except:
	print("problem")
print("after the try")
#but we have to tell what problem is
#we are not able to correctly identify what went wrong
#we do this way
try:
	foobar
except NameError:
	print("use variable that not intantiated")

def get(d,key):
	try:
		return d[key]
	except KeyError:
		return None
d={'name':'ricky'}
print(get(d,'name'))
print(get(d,'city'))


#else will run when except doesnot, means when error dont occur then else will be run
#and finally will run no matter what, means for all it will run, wthere error occur or not
try:
	num=int(input("enter a number"))
except:
	print("thats not a number")
else:
	print('i am in else')
finally:
	print('i am in finally')
#finally is not commonly used

#we do like this 
while(True):
	try:
		num=int(input("enter a number"))
	except ValueError:
		print("thats not a number")
	else:
		print('correct number entered')
		break


def divide(a,b):
	try:
		result=a/b
	except ZeroDivisionError:
		print("dont divide by 0")
	except TypeError as err: #we can also show the type of error
		print("a and b must be int or floats")
		print(err)
	else:
		print(f"{a} divided by {b} is {result}")
		return result

print(divide(1,2))
print(divide(1,'a'))

#we can also combine errors in except but then have to print generalize message
#but printing err make things clear
def divide(a,b):
	try:
		result=a/b
	except (ZeroDivisionError,TypeError) as err:
		print("something went wrong")
		print(err)
	else:
		print(f"{a} divided by {b} is {result}")
		return result

print(divide(1,'a'))
print(divide(1,0))


#debugging with pdb
#in this when error occured unintentionally so how to debug that

#pdb is a module
#we put pdb.set_trace() before line where things are breaking
#running stop at that and we can explore thing in terminal before after

import pdb
first='first'
second='second'
pdb.set_trace()
result=first+second
third='third'
result+=third
print(result)

#pdb commands
#l-list
#n-next line
#c-finish debugging
#p-print
#q-quit abruptly

#we have p for print because it can happend that variables is code conflict with pdb variable
#so we use p for that
#like p a
#p b

def add(a,b,c,d):
	import pdb;pdb.set_trace()
	return a+b+c+d
add(1,2,3,4)

