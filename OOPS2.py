#inheritance

#different users exist like simple users, moderaters and admin
#three function we have to define but many functionalities are
#common so we use inheritance
#class inherits from base or parent class
#inheritance works by passing the parent class as an arg.
#to the defination of a child class

class Animal:
	cool=True

	def make_sounds(self,sound):
		print(f"this animal make sound {sound}")

	
class Cat(Animal):
	pass

a=Animal()
a.make_sounds("CHirp")
blue=Cat()
blue.make_sounds("hoola")
print(blue.cool)
print(Animal.cool)
print(Cat.cool)

print(isinstance(blue,Cat)) #it returns true if blue is instance of cat
print(isinstance(blue,Animal))

print(isinstance(blue,object)) #everything in python the classes
#inherits from base object class

class Human:
	def __init__(self,first,last,age):
		self.first=first
		self.last=last
		if age>0:
			self._age=age  #age is private variable so have to define like this
		else:
			self._age=0
	def get_age(self):
		return self._age
	def set_age(self,new_age):
		if new_age>0:
			self._age=new_age
		else:
			self._age=0

jane=Human("jane","goodall",-9)
print(jane.get_age())
jane.set_age(45)
print(jane.get_age())

#property decorator
class Human:
	def __init__(self,first,last,age):
		self.first=first
		self.last=last
		if age>0:
			self._age=age  #age is private variable so have to define like this
		else:
			self._age=0
	@property  #this is for getter so that no need of parenthesis
	def age(self):
		return self._age

	@age.setter #this is for setting age value
	def age(self,value):
		self._age=max(value,0)

	@property
	def full_name(self):
		return f"{self.first} {self.last}"
	
	@full_name.setter
	def full_name(self,name):
		self.first,self.last=name.split(" ")

jane=Human("jane","Goodall",40)
print(jane.age) #this property allows us to get age as var. even though it is method

jane.age=20 #now here we remove parenthesis, giving arg in that
print(jane.age)
print(f"ful name: {jane.full_name}")

jane.full_name="Daniyal Khan"
print(f"ful name: {jane.full_name}")

print(jane.__dict__)#we dont see full_name here because it a
#propeerty that is working on first and last name

#remember we follow conventions, dont access like jane._age
#because it is considered private, in  real python dont have
#private or public thing so we have to take care of that


#super()
class Animal:
	def __init__(self,name,species):
		self.name=name
		self.species=species
	def __repr__(self):
		return f"{self.name} is a {self.species}"

class Cat(Animal):
	def __init__(self,name,species,breed,toy):
		#self.name=name
		#self.species=species these are in both parent and child
		#so we have to inherit these from parent, for this we can
		# call Animal init so initialize that with name n species

		Animal.__init__(self,name,species)
		#we can use super() insead of this
		self.breed=breed
		self.toy=toy

blue=Cat('Blue','Cat','Scotish Fold','String')
print(blue) #this will use repr from parent class
print(blue.species)
print(blue.breed)
print(blue.toy)
print()
class Animal:
	def __init__(self,name,species):
		self.name=name
		self.species=species
	def __repr__(self):
		return f"{self.name} is a {self.species}"
class Cat(Animal):
	def __init__(self,name,breed,toy):
		super().__init__(name,species='Cat')#dont need self in this
		self.breed=breed
		self.toy=toy
	def play(self):
		print(f"{self.name} plays with {self.toy}")
blue=Cat('Blue','Scotish Fold','String')
print(blue.species)
print(blue.breed)
blue.play()

print()
class User:
	active_users=0

	@classmethod
	def display_active_users(cls):
		return f"there are {cls.active_users} active users"
	@classmethod
	def from_string(cls,data_str):
		first,last,age=data.split(',')
		return cls(first,last,int(age))

	def __init__(self,first,last,age):
		self.first=first
		self.last=last
		self.age=age
		User.active_users+=1

	def logout(self):
		User.active_users-=1
		return f"{self.first} has logout"

	def full_name(self):
		return f"{self.first} {self.last}"

	def initials(self):
		return f"{self.first[0]}.{self.last[0]}."

	def likes(self,thing):
		return f"{self.first} likes {thing}"

	def is_senior(self):
		self.age+=1
		return f"Happy {self.age}th, {self.first}"

class Moderator(User):
	total_mods=0
	def __init__(self,first,last,age,community):
		super().__init__(first,last,age) #here active users will be incremented as it is calling init of
		#parent class User so all things done by this
		self.community=community
		Moderator.total_mods+=1

	@classmethod
	def display_active_mods(cls):
		return f"there are {cls.total_mods} active mods"

	def remove_post(self):
		return f"{self.full_name()} removed a post from the {self.community} community"

print(User.display_active_users())
u1=User("tom","harry",45)
print(User.display_active_users())
jasmine=Moderator("Jasmine","Gaur",29,"Piano")
print(User.display_active_users())
#if we have'nt used inheritence then we can copy things to get
#same working but cannot do like incrementing active_users when
#moderator is created
print(jasmine.full_name())
print(jasmine.community)
print(Moderator.display_active_mods())

print()
#multiple inheritance

class Aquatic:
	def __init__(self,name):
		self.name=name
	def swim(self):
		return f"I am {self.name} is swimming"
	def greet(self):
		return f"I am {self.name} of the sea!"

class Ambulatory:
	def __init__(self,name):
		self.name=name
	def walk(self):
		return f"{self.name} is walking"
	def greet(self):
		return f"I am {self.name} of the land!"

class Penguin(Ambulatory,Aquatic):
	def __init__(self,name):
		super().__init__(name=name)

jaws=Aquatic("jaws")
lassie=Ambulatory("lassie")
cook=Penguin("cook")

print(cook.swim()) #from Aquatic class
print(cook.walk()) #from Ambulatory class


print(f"cook istance of penguin: {isinstance(cook,Penguin)}")
print(f"cook istance of Aquatic: {isinstance(cook,Aquatic)}")
print(f"cook istance of Ambulatory: {isinstance(cook,Ambulatory)}")
#all true this means python consider cook as instance of all three classes
#as penguin inherit aquatics and ambulatory


print(cook.greet())
#this will print only of abmulatory greet not aquatic
#why this happened---|
print()
class Aquatic:
	def __init__(self,name):
		print("AQUATIC INIT")
		self.name=name
	def greet(self):
		return f"I am {self.name} of the sea!"

class Ambulatory:
	def __init__(self,name):
		print("AMBULATORY INIT")
		self.name=name
	def greet(self):
		return f"I am {self.name} of the land!"

class Penguin(Ambulatory,Aquatic):
	def __init__(self,name):
		print("PENGUIN INIT")
		super().__init__(name=name) 

mook=Penguin("mook")
print(mook.greet())
#penguine init then ambulatory init, aquatic init never called
#if we change the sequence of class Penguin(Ambulatory,Aquatic):
#to class Penguin(Aquatic,Ambulatory): this then aquatic init called

#if want both init to be called the do this
print()
class Penguin(Ambulatory,Aquatic):
	def __init__(self,name):
		print("PENGUIN INIT")
		Ambulatory.__init__(self,name=name)
		Aquatic.__init__(self,name=name)
look=Penguin("look")
print(look.greet())
#now all three called, but here name is initialized two times
#one for aquatic and other for amulatory


#method resolution order
#it is not like in what sequence we designe multiple inheritance
#it will call same name method in that way
#istead it follows MRO

#Whenever you create a class, Python sets a Method Resolution
# Order, or MRO, for that class, which is the order in which
# Python will look for methods on instances of that class.
#You can programmatically reference the MRO three ways:
#• __mro__ attribute on the class
#• use the mro() method onhhe class
#• use the builtin help(cls) method, this is better
print()
print(help(Penguin))

print()
class A:
	def do_something(self):
		print("method defined in: A")
class B(A):
	pass
	#def do_something(self):
	#	print("method defined in: B")
class C(A):
	def do_something(self):
		print("method defined in: C")
class D(B,C):
	pass
	#def do_something(self):
	#	print("method defined in: D")
#       A
#      /  \
#     B    C
#      \   /
#        D
#print(D.mro())
#it gives [<class '__main__.D'>, <class '__main__.B'>, 
#<class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
#implies D,B,C,A,object sequence will be followed
thing=D()
thing.do_something()

#D,B,C,A,object this sequence will be followed and if we
#call super in D class then it will refer to B, and if we
#call super in B then it will refer to C not A
#remember this

print()
class A:
	def do_something(self):
		print("method defined in: A")
class B(A):
	def do_something(self):
		print("method defined in: B")
		super().do_something()
		#remeber this is not pointing to class A dosomething
		#instead class C as it is MRO
class C(A):
	def do_something(self):
		print("method defined in: C")
class D(B,C):
	def do_something(self):
		print("method defined in: D")
		super().do_something()

thing=D()
thing.do_something()


print()
#Polymorphism
#an object can take one many forms
# 1- same class method works in a similar way for diff. classes
#A common implementation of this is to have a method in a 
#base (or parent) class that is overridden by a subclass. 
#This is called method overriding.
#• Each subclass will have a different implementation of the 
#method.
#• If the method is not implemented in the subclass, 
#the version in the parent class is called instead.
class Animal():
	def speak(self):
		raise NotImplementError("subclass needs to implement this")
class Dog(Animal):
	def speak(self):
		return "woof"
class Cat(Animal):
	def speak(self):
		return "meow"
class Fish(Animal):
	pass

d=Dog()
print(d.speak())
f=Fish()
#print(f.speak()) name 'NotImplementError' is not defined

print()
# 2- same operation works for different kinds of objects
# like 8+2=10 and '8'+'2'='82'
#the answere is special methods- dundar methods
#The answer is "special methods"!
#Python classes have special (also known as "magic") methods, 
#that are dunders (i.e. double underscore-named).
#These are methods with special names that give instructions 
#to Python for how to deal with objects.

# + operator is speacial method called __add__() that get
#called on the first operand
#If the first (left) operand is an instance of int, 
#__add__() does mathematical addition. If it's a string, 
#it does string concatenation.

#Therefore, you can declare special methods on your own 
#classes to mimic
#the behavior of builtin objects, like so using __len__

#The __repr__ method is one of several ways to provide a 
#nicer string representation

class Human:
	def __init__(self,first,last,age):
		self.first=first
		self.last=last
		self.age=age 
	def __repr__(self):
		return f"Human named {self.first} {self.last}"
	def __len__(self):
		return self.age 
	def __add__(self,other): 
		#self for first arg and other for second
		#self point to object but for other we need to check
		if isinstance(other,Human):
			return Human(first=self.first, last=other.last,age=0)
		return "you can't add that!" #in reallife we need to raise error for this
	def __mul__(self,other):
		if isinstance(other,int):
			return [self for i in range(other)]
		return "cant multiply"

j=Human("jen","lar",47)
k=Human("kev","jon",49)
print(j)
print(len(j))
i=j+k 
print(i)
#print(2+j) show error by int class
print(j+2) # show from Human class

print(j*2) #we are getting 'human named jen lar' because of repr 

print()
tiplets=j*3
#now triplets contain list of 3 objects referencing to same
#object as we have return list of self that points to a single object
#now if change one value other will be changed
tiplets[1].first='xyz'
print(tiplets) 

#and if we want three different objects then we do
from copy import copy
class Human:
	def __init__(self,first,last,age):
		self.first=first
		self.last=last
		self.age=age 
	def __repr__(self):
		return f"Human named {self.first} {self.last}"
	def __len__(self):
		return self.age 
	def __add__(self,other): 
		if isinstance(other,Human):
			return Human(first=self.first, last=other.last,age=0)
		return "you can't add that!"
	def __mul__(self,other):
		if isinstance(other,int):
			return [copy(self) for i in range(other)]
		return "cant multiply"
j=Human("jen","lar",47)
tiplets=j*3
tiplets[1].first='xyz'
print(tiplets)
print()
k=Human("kev","jon",49)
t=(k+j)*3
print(t)

print()
#magical methods along with inheritance

class GrumpyDict(dict):
	#we are not defining our own __init__ as will be using of
	#the parent class dict

	def __repr__(self):
		print("none pf your business")
		return super().__repr__()

	def __missing__(self,key): #missing automatically called in dict
		#usually when thrown error 
		print(f"you want {key}? well it aint here!")

	def __setitem__(self,key,value):
		print("you cant change the dictionary")
		print("ok fine")
		super().__setitem__(key,value)

	def __contains__(self,item):
		print('no it aint in here')
		return False

d=GrumpyDict({'name':'yoko','city':'new york'})
print(d)
d['age']
d['city']='SF'
print(d)

'city' in d
#by this we can add additional functionality to the existing 
#things along with there impelemented things without copy pasting
#directly using parent functionality with super()
#use python docs to get what dundar methods are present in that class
