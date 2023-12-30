#why use modules?

#keep python files small
#reuse code across multiple files byimporting
#a module is jusr a python file
#help to do things that we on our own cant do or take time like generating random
#numbers

#builtin modules that comes with python like random, and external modules we need
#to download

import random
print(random.choice([1,2,3,4,59,7,5,3]))
#can give alias to module
import random as r
print(r.randint(1,100))

#importing parts of module
#only import what u need is the good practice
# * for importing all
#from random import * but not good practice
from random import choice,randint
print(randint(1,100))

from random import choice as c, randint as r
print(c([1,2,3,4,59,7,5,3]))


#custom modules
#importing own code
#the need to be in the sme directory otherwise we have to reference that path
import module_called as m
print(m.add(4,5))


#external modules
#can see on pypi site
#we use pip for this
#python3 -m pip install nameofpackage
from termcolor import colored
#print(help(termcolor))
text=colored("hi there",color='cyan',attrs=['blink'])
print(text)


#autopep8 it is used for formatting the python file, auto formatting
#we do this command line
# -i for inplace, deleting old one
# -a for aggresive nature like using if greeting==True, aand greeting is bool
#as we can do if greeting, so it will oreect this

# autopep8 -i codename.py
#for aggression use
# autopep8 -i -a codename.py
#for double aggression use # autopep8 -i -a -a codename.py



#__name__ variable
#every file or module have its name
#if file is main file bring running then its value is __main__
#otherwise its value is __filename__

from module_called import print_name
def say_hi():
	print(f"my __name__ is {__name__}")
say_hi()
print_name()