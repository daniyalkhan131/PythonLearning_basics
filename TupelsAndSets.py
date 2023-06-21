# TUPLES

# tuples is ordered collection or grouping of items
# same as list
# but it is immutable means cannot alter or change
x=(1,2,3)
print(x)
print(3 in x)
#x[0]=3 not possible

#why use?
# it is faster than list, make code safer
# commonly used for unchanged data:
days=("mon","tues","wed","thur","fri","sat","sun")
print(days[3])
# can have duplicate data
tt=(1,2,3,3,3,3)
print(tt)

# tuple() take iterable item as argument
m = tuple([1,2,3,3,3,3,3,3])
print(m)

# tuples can be used as keys in dictionaries
loc={(1.34,4.345):"rampur",
	(1.23,5.57):"delhi",
	(5.35,8.45):"barielly"}
print(loc[1.34,4.345])
# we cannot use list it show error unhashable type
#loc={[1.34,4.345]:"rampur"}
# if we want to use ordered data as key then use tuples

# .items() return a view object that displays a list of tuples-
# -becase we cannot chnage key value
list_tuple=loc.items()
print(list_tuple)

#loopig
for i in days:
	print(i,end=" ")
print()
i=len(days)-1
while i >=0:
	print(days[i],end=" ")
	i-=1

print()
# tuples methods

# .count(value) return no. of time value occured
print(m.count(3))

# .index(values) return index of value
# and give error if not present
print(m.index(2))
print(m.index(3)) # gives first matching index


#nested tuples
q=(1,2,3,4,(3,4,5,6),7,7,8)
print(q[4])
print(q[4][3])

# can using slicing in tuples
print(q[3:])


# SETS

# sets are maths sets (same)
# no order, no duplicates
# no order so cannot access them with index

s={1,2,3,4,5,5,5,5}
print(s)
s=set({1,23,3,3,33,5,5})
print(s)
#s[0] not possible

print(23 in s)

s={1,4,5,'a','b',23.33}
print(s)# see order got change( no order in set)

for i in s:
	print(i,end=" ")

print()

l=[1,2,3,3,33,4,4,5,6,7,77,8,8,8,8,9]
print(set(l))
print(list(set(l)))

# sets methods

# .add(element) add element to set or append
s.add("danu")
print(s)

# .remove(value) remove value and give error if not present
s.remove("danu")
print(s)

# use .discard(value) if dont want error to occur if-
# -value not present
s.discard("khan")
print(s)

# .copy() create duplicate 
x=s.copy()
print(x)
print(x is s)
print(x==s)

# .clear() clear the entire set
x.clear()
print(x)

qq={"daniyal","khan","is","a","boy"}
qt={"daniyal","khan","is","not","a","girl"}

# union |
print(qq | qt)

# intersection &
print(qq&qt)

x=(1)
print(type(x)) # it is int

x=tuple([1])
print(type(x)) #but it is tuple
#or
x=(1,)
print(type(x))


# set comprehension

tt={x**2 for x in range(10)}
print(tt)

tt={char.upper() for char in "hellllo"}
print(tt)

def isAllVowels(str1):
	return len({char for char in str1 if char in "aeiou"})==5

print(isAllVowels("daniyal"))
print(isAllVowels("asdsvaeiou"))