#generators are iterators (chota bhai bada kaam of iterators)
#it is short way of creating iterators

#created using generator functions which use yield function
#and created also using generator expression

#function vs generator function
#uses return            #uses yield
#return once			# can yield multiple times
#when invoked,			#when invoked,
#returns return value	#returns retuns a generator


#it is generator function
def count_up_to(max):
	count=1
	while count<=max:
		yield count
		count+=1
print(count_up_to(5))

counter=count_up_to(3)
#now what generator function do is like return 1 then stop at yield
#then agin when called start from yield doing count+1 and then
#check conditn and return new value and rest at yield.....so on

print(next(counter))
print(next(counter))
print(next(counter))
#yield keeping track of state
#generator dont have all data in memory at once
#it keeps the most recent once

#we impelement counter previously by creating class then implementing
#next and iter and so on but here we get sme functionality by
#simply making a function
#it automatically have next and iter
#print(help(counter)) can see here

for i in counter:
	print(i)

#counter=count_up_to(3) if we dont define this than below wont
#do anything because for loop encounter stopping error and it stops
for i in counter:
	print(i)

print()
counter=count_up_to(7)
print(next(counter))
print('--------------')
for i in counter:
	print(i)

#generator is faster as take less memory
#in sum() can pass generator

def current_beat():
	max=100
	nums=(1,2,3,4)
	i=0
	result=[]
	while len(result)<max:
		if i>=len(nums): i=0
		result.append(nums[i])
		i+=1
	return result

print(current_beat())
#but we dont want like this, we want one by one the value and
#infinite values to be generated, and list cannot hold infinite values

def current_beat():
	nums=(1,2,3,4)
	i=0
	while True:
		if i>= len(nums):i=0
		yield nums[i]
		i+=1

counter=current_beat()
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print('--------------')
for i in range(3):
	print(next(counter))


#testing memory usage with generators

def fib_list(max):
	nums=[]
	a,b=0,1
	while len(nums)<max:
		nums.append(b)
		a,b=b,a+b 
	return nums
print(fib_list(10))

def fib_gen(max):
	x=0
	y=1
	count=0
	while count<max:
		x,y=y,x+y 
		yield x
		count+=1
for i in fib_gen(10): 
	print(i)
#generator are easy on memory



#generator expressions
def nums():
	for num in range(1,10):
		yield num
g=nums()
print(next(g))
print(next(g))
print(next(g))
print(g)

#we can do this simply with
g=(num for num in range(1,10))
#this is list comprehension g=[num for num in range(1,10)]
print(next(g))
print(next(g))
print(g)

import time
gen_start_time=time.time()
print(sum(n for n in range(100000000)))
gen_stop=time.time()-gen_start_time

list_start_time=time.time()
print(sum([n for n in range(100000000)]))
list_stop=time.time()-list_start_time

print(f"sum(n for n in range(10000000)) took : {gen_stop}")
print(f"sum([n for n in range(10000000)]) took : {list_stop}")