#choice for selecting random element from list-
#-and randint for integer value selecting
from random import choice, randint
l=['s','y','r','w','i']
print(choice(l))
print(randint(-5,5)) #it choose between & including -5 and 5

#for printing samething many times
print("do this!\n"*5)
t="danu"
p=t*5  #it is creating a string having 5 danu
print(p)
print(p[9])

# for lower case the string, it is string function
print("DaniYALKHAn".lower())

#print() automatically produce to newline after printing
# -to avoid this we use end=" " with print whose newline
# -we dont want

print("danu", end=" ")
print("khan")

#pep8 styling is used when we work together, this is standard
# do not learn this instead use autopep8 tool to do this task
# autopep8 --in-plave name.py
# do this command line, but before this install it

# cannot do l= None then l=l+"er" but can do l="" and-
# -then l=l+"er"

# len also used for string
print(len("my name is khan"))

#swapping values
names=["danu","khan"]
names[0],names[1]=names[1],names[0]
print(names)


# bool()
# it return false when inside is empty string list or 0
# number other than 0 it gives true
print(bool(0))
print(bool(''))
print(bool([]))
print(bool(345))
print(bool('sdfds'))
print(bool([1,2,3]))

# in keyword also work with strings
print('l' in 'daniyal')
# .join() is use for concatenating string-
# -with '' in between every char


# .format() method of string
artist = {
    "first": "Neil",
    "last": "Young",
}
full_name = "{} {}".format(artist["first"],artist["last"])
print(full_name)
#or can do same with f string
full_name1= f"{artist['first']} {artist['last']}"
print(full_name1)
#print(f"{artist["first"]} {artist["last"]}") this is not-
# -working because "" cannot be inside "" we have to change-
# - the qoutation to ''


# using builtin function sum()
donations = dict(sam=25.0, lena=88.99, chuck=13.0, 
	linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
total= sum(i for i in donations.values())
print(total)
# or
total=sum(donations.values())
print(total) # sum is working on dict_values class

#list of list then it will equalise to element of nested list
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
for i,j in person:
    print(i,j)

# .chr() function for getting char. from ascii no.
print(chr(90))