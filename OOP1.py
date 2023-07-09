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


#class attributes
#it of class means every obj contain it
class User:
	active_users=0
	def __init__(self,first,last,age):
		self.first=first
		self.last=last
		self.age=age
		User.active_users+=1 #this means every time
		#instance created it got incremented

	def logout(self):
		User.active_users-=1
		return f"{self.first} has logout"

print(User.active_users)
user1=User('danu','khan',23)
user3=User('asad','khan',23)
print(User.active_users)
print(user3.logout())
print(User.active_users)

#can use class attribute for validation
class Pet:
	allowed=['cat','dog','fish','rat']
	def __init__(self,name,species):
		if species not in Pet.allowed: #for accessing class attribute
			#we use class name, can also use self
			raise ValueError(f"You cant have a {species} pet")
		self.name=name
		self.species=species
cat=Pet('billi','cat')
dog=Pet('kutta','dog')
#Pet('tony','tiger') it shows valuerror

#if we dont want class att then put that in init
#so cannot be accessed
class Pet:
	def __init__(self,name,species):
		allowed=['cat','dog','fish','rat']
		if species not in allowed: 
			raise ValueError(f"You cant have a {species} pet")
		self.name=name
		self.species=species
cat=Pet('billi','cat')
dog=Pet('kutta','dog')
#print(cat.allowed) not possble
#print(Pet.allowed) #not possble

#we can change dog species afterwards, this should be stopped
print(dog.species)
dog.species='tiger'
print(dog.species)
#so we make class attribute so dont need to write agin

class Pet:
	allowed=['cat','dog','fish','rat']
	def __init__(self,name,species):
		if species not in Pet.allowed:
			raise ValueError(f"You cant have a {species} pet")
		self.name=name
		self.species=species
	def set_species(self,species):
		if species not in Pet.allowed:
			raise ValueError(f"You cant have a {species} pet")
		self.species=species

cat=Pet('billi','cat')
dog=Pet('kutta','dog')
print(dog.species)
#dog.set_species('tiger')
#but we can append calass att and then add like
Pet.allowed.append('tiger')
dog.set_species('tiger')
print(dog.species)

#instance have allowed attribute but the point to the
#attribute of class, same memory address
print(cat.allowed)
print(dog.allowed)

print(id(cat.allowed)) #id give unique no to loc.
print(id(dog.allowed))
print(id(Pet.allowed))
#implies we can use self.allowed for refering in class that we do with Pet.allowed but prefer Pet,.allowed only


#if change the cat.allowed then it got change 
#but pet and dog remain same dog refering to pet
cat.allowed=['tiger','cat']
print(cat.allowed) #now it is refering to someother loc
print(dog.allowed)
print(Pet.allowed)


#class methods
#very rare to use
# @classmethod decorator
class User:
	active_users=0

	@classmethod
	def display_active_users(cls): #can use any var but standard is cls
		#print(cls)
		return f"there are {cls.active_users}"

	def __init__(self,first,last,age):
		self.first=first
		self.last=last
		self.age=age
		User.active_users+=1 #this means every time
		#instance created it got incremented

	def logout(self):
		User.active_users-=1
		return f"{self.first} has logout"

print(User.display_active_users())
user1=User('danu','khan',23)
user2=User('naj','ans',24)
user3=User('asad','khan',23)
#user1.display_active_users() #cls contain User 
#User.display_active_users()

print(User.display_active_users())
user4=User('naj','ans',24)
user5=User('asad','khan',23)
print(User.display_active_users())


#use of class methods
#like data coming from csv file so we need to organize that
#we do need for that

 #dict.fromkeys() this is class method but it is builtin
 #thats why d is small letter
x=dict.fromkeys(['name','age','city'],'unknown')
print(x) #it is trandorming this rep ti dict rep

#we bas csv then it return user instance
class User:
	active_users=0

	@classmethod
	def from_string(cls,data):
		first,last,age=data.split(',')
		return cls(first,last,int(age)) #cls refering User

	def __init__(self,first,last,age):
		self.first=first
		self.last=last
		self.age=age
		User.active_users+=1
u1=User.from_string('daniyal,khan,23')
print(u1.first)



# __repr__ we can control print(u1) like that
class User:
	active_users=0
	@classmethod
	def from_string(cls,data):
		first,last,age=data.split(',')
		return cls(first,last,int(age)) 
		
	def __init__(self,first,last,age):
		self.first=first
		self.last=last
		self.age=age
		User.active_users+=1

	def __repr__(self):
		return f"{self.first} is {self.age}"

u1=User.from_string('daniyal,khan,23')
print(u1)