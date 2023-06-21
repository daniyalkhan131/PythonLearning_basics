#can use single or double quote -> your choice
#can use qoute inside qoute- nesting
#but shouldn't use same one
x="my name is 'Daniyal Khan'"
print(x)
x='my name is "Daniyal Khan"'
print(x)

# String escape character- do something special
# like- \n newline, \\ for \ in string, \t tab
x="my name is \\ daniyal"
print(x)
#for double quotes inside double quote
x="my name is daniyal \"khan\""
print(x)

# for string concatenation use + operater
# both should be string
x="daniyal"
y="khan"
print(x+" "+y)
#print(x+8) it will show error

x="colt"
x+="steele"
print(x)

#formatting string
#for concatenating string values with int float..
# new way(in py 3.6+) called f-strings

guess=9
print(f"your guess of {guess} was worng")
# can write expression inside it
print(f"your guess of {guess+10} was worng")
print(f"{x} your guess of {guess} was worng")

#old way of doing
print("your guess of {} was worng".format(guess))
print("{} your guess of {} was worng".format(x,guess))
#very old way
print("your guess of %d was worng"%(guess+2))

#string start from 0 index and all have indeces
# something like list can access with index value
print("daniyal"[0])
print("daniyal"[1])
print("daniyal"[-1])