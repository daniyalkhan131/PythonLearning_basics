#why test?
#reduce bugs in the existing code
#ensure bugs that are fixed stay fixed
#ensures that new features don't break old ones
#ensures that cleaning up code doesn't introduce new bugs
#makes development more fun

#working on bigger softwares where many developers so need testing for that
#we can write function nd then test for that do testing 
#but there is test driven development
#where we do
#developemnts begins by writing tests
#once tests are written, write code to make tests pass
#once tests pass, a feature is considered complete

#it is the way we do write codde for passing the test
#1.Red - Write a test that fails
#2. Green - Write the minimal amount of code necessary to make the test pass
#3. Refactor - Clean up the code, while ensuring that tests still pass

#we write diiferent test and it helps in development to capture bugs as comming to
#project after 6 months and writing new feature than need testing to 
#properly understand

#Assertion
#We can make simple assertions with the assert keyword
#assert accepts an expression
#Returns None if the expression is truthy
#Raises an AssertionError if the expression is falsy
#Accepts an optional error message as a second argument

#now we dont use assertion for testing as have better options

#assert is statement

# def add_pos(x,y):
# 	assert x>0 and y>0, "both should be positive"
# 	return x+y
# print(add_pos(1,1))
#print(add_pos(1,-1))
#assert is like if not condition statement


#if python file run with -O thenit means optimization mode, so no assertion will be
#evaluated
#but this is problemmatic so eed to be avoided, as anyone can enter where we
#put restrictn using assertion


#doctest

# def add(a,b):
# 	"""
# 	>>> add(2,3)
# 	5
# 	>>> add(100,200)
# 	300
# 	"""
# 	return a*b

#and we run this using cmd python3 -m doctest -v Testing.py


#now with red green refractor way of doing
# def double(values):
# 	""" double the values in a list

# 	>>> double([1,2,3,4])
# 	[2, 4, 6, 8]

# 	>>> double([])
# 	[]

# 	>>> double(['a', 'b', 'c'])
# 	['aa', 'bb', 'cc']

# 	>>> double([True, None])
# 		Traceback (most recent call last):
# 		          File "/Users/daniyalkhan/Documents/PythonLearning_basics/Testing.py",line 71, in <module>
# 		            double([True,None])
# 		          File "/Users/daniyalkhan/Documents/PythonLearning_basics/Testing.py", line 69, in double
# 		            return [2 * element for element in values]
# 		                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# 		          File "/Users/daniyalkhan/Documents/PythonLearning_basics/Testing.py", line 69, in <listcomp>
# 		            return [2 * element for element in values]
# 		                    ~~^~~~~~~~~
# 		        TypeError: unsupported operand type(s) for *: 'int' and 'NoneType' 
 
# 	"""
# 	#writing last one is difficult as have to write full exact error that
# 	#python give
# 	return [2 * element for element in values]




#issue with doctest
#spaces,sequence in dic matter which in reality don't
#our function become large
#lack many feature of larger testing tools



#unit testing
#Test smallest parts of an application in isolation (e.g. units)
#Good candidates for unit testing: individual classes, modules, or functions
#Bad candidates for unit testing: an entire application, 
#dependencies across several classes or modules

#we get fancy assertions in this

#Python comes with a built-in module called unittest
#You can write unit tests encapsulated as classes that inherit from unittest. TestCase
#This inheritance gives you access to many assertion helpers that let you test the behavior of your functions
#You can run tests by calling unittest.main ()

import unittest
from testing_called import eat, nap

class ActivityTests(unittest.TestCase): #we have to inherit unittest capability

	def test_eat(self):
		self.assertEqual(
			eat("broccoli", is_healthy=True),
			"broccoli!, because get u fit"
			)
		self.assertEqual(
			eat("pizza", is_healthy=False),
			"pizza!, because taste good"
			)

if __name__=='__main__':
	unittest.main()