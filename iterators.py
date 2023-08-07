#iterators vs iterables
#iterator- an object can be iterated upon. An object which returns
#data onee element at a time when next() is called on it
#iterable- an object which will return an iterator when iter()
#is called on it.

name='Danu' # it is iterable not iterator
#next(name) this shows error

it=iter(name) #now it become iterator
print(it)
#when we write for i in "Danu": then for loop first
#apply iter() to string then access using next()

#when next() is called on an iterator, the iterator returns the 
#next item. it keeps doing so until it raises a StopIteration error

print(next(it))
print(next(it))
print(next(it))
print(next(it))
#print(next(it)) raise error

l=[1,2,3,4,5]
it=iter(l)
print(next(it))
print(next(it))
print(next(it))
print(next(it))

#custom For loop

def my_for(iterable):
	iterator=iter(iterable)
	while True:
		try:
			print(next(iterator))
		except StopIteration:
			print("END OF ITERATOR!")
			break
my_for("hello")

#giving function for what to do
def my_for(iterable,func):
	iterator=iter(iterable)
	while True:
		try:
			thing=next(iterator)
		except StopIteration:
			break
		else:
			func(thing)
def square(x):
	print(x*x)

my_for("danu",print)
my_for([1,2,3,4,5],square)


#custom iterator

class Counter:
	def __init__(self,low,high):
		self.low=low
		self.high=high
	def __iter__(self): #we need to define this as iter()
		#will use this what to do means how to convert this
		#iterable to iterator
		#if we dont define this then applying iter() to it
		#show that it is not iterable

		return self
	def __next__(self):
		if self.low<self.high:
			num=self.low
			self.low+=1
			return num 
		raise StopIteration

c=Counter(0,4)
iter(c) # it works as we defines __iter__

for x in Counter(0,4):
	print(x)

