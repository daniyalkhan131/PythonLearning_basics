# ordered collection or group of items
task=["install","learn","break",3,5,4.345]
print(task)

print(len(task))

#creating using list()
r=range(1,10)
l=list(r) #it is type casting range to list
print(r)
print(l)
l1=list(range(5,7))
print(l1)

# list index start from 0 always or if negative then-
# -last element of list is -1

# use in for checking element in list
print("install" in task) # it return boolean value

people = ["Hanna","Louisa","Claudia", "Angela",
			"Geoffrey", "aparna"]
people[-len(people)]="Hannah"
people[-2]="Jeffrey"
people[5]="Aparna"
print(people)
# for accessing all elements
for i in people:
	print(i)
i=0
while i<len(people):
	print(people[i])
	i+=1

# there is difference between functions and methods
# for methods we use dot operator
# like [1,2,3].append() is method while len() is function
data=[1,2,3]
data.append("danu")
print(data)

data.extend([4,5,6]) # cannot add multiple items with apend
print(data)

data.append([9,8])
print(data)

# above ones add at end of list
# insert add at specific location .insert(pos,value)

data.insert(2,"hello")
print(data)
# with -ve pos it won't work as expected as take previous value
data.insert(-1,"end")
print(data)

l1=list()
l1.extend(["danu","daniyal","khan"])
print(l1)

# .clear() for deleting all elements => empty list
l1.clear()
print(l1)

# .pop(pos) or .pop() removes and return that element
# if empty then last element

data.pop()
print(data)
tt=data.pop(2)
print(f"list={data} and deleted element is {tt}")

# .remove(element)  delet first element and gives-
# -error if not present

data.remove("danu")
print(data)

# .index(element,start) give index of element starting from-
# -that start given(including it)
# .index(element) gives element index from strating
# .index(element,start,end)

l2=list(range(1,10))
print(l2.index(5,3,8))

# .count(element) tells no. of times element occures
# if no element then 0 returns

l2.extend([1,1,2,2,2,2])
print(l2.count(2))

# .reverse() it reverse elements in-place => no extra list needed
l2.reverse()
print(l2)

# .sort() it sorts in-place
l2.sort()
print(l2)

# "string".join(ourlist) is string method, it convert list to string
# and string is concati. in between every element
l3=["my","name","is","danu"]
string1=" ".join(l3)
string2="-".join(l3)
print(string1,string2)


#Slicing  (same syntax is for string slicing)
# slicing is not method
# list1[start:end:step]
# start is included and end is not included
l4=[1,2,3,4,"daniyalkhan","khan",44,5.5]
print(l4[4:])
print(l4[-1:])
print(l4[-4:])

print(l4[0:]) # it copy the full list and l4[:] also
l5=l4
print(l5==l4)
print(l5 is l4)
l6=l4[:]
print(l6==l4)
print(l6 is l4)


print(l4[:2])
print(l4[:4])
print(l4[:-1])
print(l4[1:-1])


print(l4[::2])
print(l4[1::-1])    # if -ve step then empty start=last index-
print(l4[:1:-1])	# -and empty end= first index -1
print(l4[2::-1])


# reversing with slicing
print(l4[::-1])

# modifying portions of lists
num=list(range(1,6))
print(num)
num[1:3]=['a','b']
print(num)

print(l4[4][::-1]) #slicing apply to string also
print("helllooooworldd"[:5])
print("helllooooworldd"[::2])
print("helllooooworldd"[5:8])
