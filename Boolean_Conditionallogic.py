#if_________:
#elif________:
#else:
name=input("enter\n")
if name.lower()=="danu":
	print("danu")
elif name.lower()=="khan":
	print("khan")
else:
	print("not your name")

from random import randint
choice = randint(1,10)
if choice==7:
    print("lucky")
else:
    print("unlucky")

# we use like if,elif,elif,...,else for multiple checking


#Truthiness
x=1
#if(x is 1):         why it is showing syntax warning
#	print("x")
print(x is 1)      # it is also
# if a=[1,2] and b=[1,2] then a is b returns false because-
# - is checks location is same or not but here these are-
# - two diff. instances of object(diff loc.)
print("for is ")
aa=[1,2,3]
bb=[1,2,3]
print(aa==bb) # it prints true
print(aa is bb) #prints false
# now we do
clone=aa
print(clone is aa) # prints true because clone point to same-
#- location



# value resolve to true are truthy and to false are falsy
#things naturally falsy are empty objects strings, None, zero
if 0:
	print(0) # never print
if 1:
	print("adaf") # always it get print

animal=input("enter animal")
if animal:        # if empty string then print never occur
	              #because empty string give false
	print(animal+" this you entered")
else:
	print("you didnt said anything")

#comparision operators
# ==,!=,<,>,<=,>=   greater smaller one works with characters too

# Logical operators
# and,or,not

print(not False) #used for negating sentence
print(not (1>3 or 1!=9))
# ~(P or Q) = ~P and ~Q


string=input("enter no.")
if int(string)>2:     #but if we give empty string then it cannot-
	# -convert into int so show error
	print("boo")
else:
	print("wweew")

# so we do like this
# this is a kind of handling error but more we will learn-
#-afterwards
string=input("enter no.")
if string !="":   # or if string:
	if int(string)>2:
		print("boo")
	else:
		print("wweew")
else:
	print("enter valid no.")

