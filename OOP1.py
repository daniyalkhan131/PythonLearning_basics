#print(help(int))
print(type(list))

#use camelcase for class
#variables function names are snake case

class User:
	pass #for definig working class otherwise empty so give error
user1=User() #instansiation
user2=User()
print(user1)
print(user2) #at diff mem. loc.

print(type(user1))

#__init__ called automatically everytime instance is created
class Userr:
	def __init__(self):
		print("A new user created")
user1=Userr()
user2=Userr()
user3=Userr()

#we initialize data in __init__ not print something
#self refers to specific instance of user class
class Userr:
	def __init__(self,first,last,age):
		self.first=first
		self.last=last
		self.age=age
user1=Userr('danu','khan',23)
user2=Userr('naj','ans',24)
user3=Userr('asad','khan',23)

print(user1.first,user1.last,user1.age)
print(user2.first,user2.last,user2.age)
print(user3.first,user3.last,user3.age)
#self must be the first parameter to __init__
#and any methods and properties on class instances.


# _name this is way of telling develops that it is supposed
#to be private

# __name name mingling, main purpose to make this 
#perticular for this class, usage in inheritance
#python change name and put class name infron
#it become _Person__name

# __name__ dundar methods, only define when overwriting things,
#something that exist in python, special thingsthat python looks for

class Person:
	def __init__(self):
		self.name='Tony'
		self._secret='hi'
		self.__msg='i like her'
	#def __hello__(self) this is wrong
p=Person()
print(p.name)
print(p._secret) # no diference at all, both are printed

#print(p.__msg) error
print(p._Person__msg)
print()
print(dir(p)) # for getting all the things related to p
print()


# __something__ should be put at top of class, convention it is

class User:
	def __init__(self,first,last,age):
		self.first=first
		self.last=last
		self.age=age

	def full_name(self):  #it is instance method not class method
		return f"{self.first} {self.last}"

	def initials(self):
		return f"{self.first[0].upper()}.{self.last[0].upper()}."
	def likes(self,thing):
		return f"{self.first} likes {thing}"

	def is_senior(self):
		return self.age >= 65

	#above all are getter 
	#now setter
	def birthday(self):
		self.age+=1
		return f"Happy {self.age}th, {self.first}"

	#you need to have self in method doesnot matter whether using or not	
	#def say_hi():
	#	print('HELLO!')

user1=User('danu','khan',23)
user3=User('asad','khan',23)
print(user1.full_name())
print(user1.initials())
print(user1.likes('ice cream'))
print(user1.is_senior())
print(user1.birthday())
#print(user1.say_hi()) it gives error says a arg given