# *args
def sum_of_all(num1,num2,num3,num4,num5):
	return num1+num2+num3+num4+num5
#here we need to define all params
#instead of this use *args that take any no. of input as a tuple

def sum_of_all(*args):
	total=0
	for num in args:
		total+=num
	return total

print(sum_of_all(1,2,3,4,5,6,7,8))
print(sum_of_all(1,2))

def ensure_correct_info(*args):   #args is vatiable only * is important
	print(args)
	if "Colt" in args and "Steele" in args:
		return "Welcome back Colt"
	return "not sure who your are"
print(ensure_correct_info())
print(ensure_correct_info(1,True,'Steele','Colt'))

def ensure_correct_info(nn,*args):   #args is vatiable only * is important
	print(f"nn={nn}")
	print(args)
	if "Colt" in args and "Steele" in args:
		return "Welcome back Colt"
	return "not sure who your are"
print(ensure_correct_info(1,True,'Steele','Colt'))


# **kwargs

#gathers remaining keywords argument as a dict

def fav_colors(**kwargs):
	print(kwargs)
	for person,color in kwargs.items():
		print(f"{person} likes {color}")
fav_colors(sara='blue',danu='black',naj='green')

def special_greeting(**kwargs):
	if "david" in kwargs and kwargs["david"]=="special":
		return "you are special"
	elif "david" in kwargs:
		return f"{kwargs['david']} david"
	return "not sure"
print(special_greeting(david='hello'))
print(special_greeting(bob='hello'))
print(special_greeting(david='special'))



#standard parameter ordering
#1.parameters
#2. *args
#3. default parametrs
#4. **kwargs

def display_info(a,b,*args,instructor="Colt",**kwargs):
	return [a,b,args,instructor,kwargs]

print(display_info(1,2,3,last_name="Steel",jon="Instructor"))


# using * as an argument to a function to unpack values
def sum_of_all(*args):
	total=0
	for num in args:
		total+=num
	return total

num1=(1,2,3,4,5,6,7)
num2=[1,2,3,4,5]
#print(sum_of_all(num1)) 
#for passing the list or tuple of arguments
# it will give error as num1/num2 qill be considered as 1 elmenet of tuple args
# correct way
print(sum_of_all(*num1))
print(sum_of_all(*num2))
# it is unpackung because we are unpackung the values n sending


#using ** as an argument: dictionary unpacking
def display_names(first,second):
	print(f"{first} says hello to {second}")
names={"first":"colt","second":"rusty"}
#display_names(names) error
display_names(**names)

def add_mult_nums(a,b,c,**kwargs):
	print(a+b*c)
	print("other stuff.....")
	print(kwargs)

data=dict(a=1,b=2,c=3,d=55,name='tony')  #ther than a,b,c go in to kwargs
add_mult_nums(**data)
add_mult_nums(**data,cat="blue")