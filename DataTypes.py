bool1=True
print(bool1)
bool2=False
print(bool2)
#bool3=true invalid

int1=343
print(int1)

str1="daniyalkhan is very brilliant guy"
print(str1)

list1,list2=[1,2,3,4,5],["e","4","re","56"]
print(list1,"\t",list2)

print(list1[2]), print(list2[2])

list3=[[1,2,883,4],[5,6,7,8],[3,4]]
print(list3[0][2])
print(list3)

for i in range(0,11):
	print(str1[i])

#DYNAMIC TYPING - reassiging variables to diff types
a="danu"
print(a)
a=56
print(a)
a=None # it means nothing 
print(a)
a=True
print(a)
a="danu"
print(a) 
b=56
print("b=",b)
b="danu"
print("b=",b)

t=None # it is python version of null
# it used so that variable name is allocated but value
# is None that means we can call that, it don't show error
print(type(t))

#Converting Data types
#in string interpolation data types are implicitly-
#-converted into string form like using f string for-
#- formatting convert to string implicitly
# we do explicitly also
x=12.3334
y=int(x)
print(x,y)
tt=[1,2,3]
ts=str(tt) 
print(tt,ts)
print(ts[0])

x=1/2 # implicitly converted into fload
print(x)

#workout example

kms=float(input("how do you kms you cycled\n"))
#input always take value as string, we have to change datatype
miles=kms/1.609
print(f"you saidv{round(miles,3)} miles")
# round(thing to round,how many decimal places)