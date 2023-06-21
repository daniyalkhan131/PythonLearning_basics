#[2, 3, 'ads', 'A', [1, 2, 3], (1, 2), {1: 2, 4: 5}]
#anything can be in list
#there are limitations of list so we use dictionaries,
#-beacue it is unclear about the data in list
#key vaue pair, list has key indices while in dictionary
#-we can define it

#keys can either number or string while values can be
#-anything

#for comments, you can use a multiline string.Since-
#-Python will ignore string literals that are not-
#-assigned to a variable, you can add a multiline-
#-string (triple quotes) in your code,-
#-and place your comment inside it.

#dict with function- dict(key='value')

# keys cannot be repeated but values can

t=[{'name':'danu','age':23,'pet':False,
 'hobbies':['cri','football']},{'name':'khubaib',
'age':28,'pet':False,'hobbies':['videogame','football']}]
#this is list of dictionaries that has one value as list

print(t)

#t2=dict('name'='danu',age=23,pet=False,hobbies=['cri','football'])
#expression cannot contain assignment, perhaps you meant "=="?
#this error comes
#print(t2)

t2=dict(name='danu',age=23,pet=False,hobbies=['cri','football'],
	u=24)
print(t2)

#temp=dict(2 ="danu") this is showing error

hh={1:"qqq",4:5,"wfee":"svs","qqq":1}
print(t2["age"])
print(t2["hobbies"])
print(hh[4])
#print(hh[56]) it will give key error(not present the key)


#for accessing aall values or loopinf over dictionry
# these things make dictionary iterable
# .value() method of dictionary
print(type(hh.values())) # class dict_values is iterable
print(hh.values())
for i in hh.values():
	print(i,end=" ")

# for keys use .keys() method
print(f"\n\n{hh.keys()}")
for i in hh.keys():
	print(i,end=" ")

# using .items() method
print(f"\n\n{hh.items()}")
for key,value in hh.items():
	print(f"key={key} and value={value}")

# no specific order guaranteed in dict unlike list where ordered,-
#-in dictionary things are floating around


# in keyword in dictionary check only for keys
print("wfee" in hh)

# instead of this write with in as don't show error
# show error - if hh["wfe"]:
	#print("present")
if "wfe" in hh:
	print("present")


# for checking in values we do
print("qqq" in hh.values())

# dictionary methods
# .clear()  it clears all keys and values
d=dict(a=1,b=2,c=3)
d.clear()
print(d)

# .copy()  it make copy of dictionary
d=dict(a=1,b=2,c=3)
e=d.copy()
f=d
print(e is d) #false
print(f is d) #true

# {}.fromkeys(arg1,arg2)  creates key-value pair from comma seperated values
# arg1 is iterable object and arg2 is simply copied as value-
# - to every element of iterable object
x={}.fromkeys("a","b")
print(x)
x={}.fromkeys(["email",1,2,3],"b")
print(x)
x={}.fromkeys("a",[1,2,3,4,5])
print(x)
x={}.fromkeys([1,2,3,4,5],[1,2])
print(x)
# it is useful for creating default dictionary
new_user={}.fromkeys(["name","score","email","profile"],"unknown")
print(new_user)
# can use dict or {} or any other dictionary above, no change-
# -will occur same thing
x=new_user.fromkeys("danu","khan")
print(x)
print(new_user)

x=dict.fromkeys(range(1,7),"out")
print(x)

# .get(key) it will give value of keya and give None if-
# - not present
print(x.get(3))
print(x.get(9))

# .pop(key) remove key value froom dict. and return value
a=dict(a=1,b=2,c=3)
print(a.pop("a"))
print(a)
#a.pop("g") it gives error

# a.pop() # no arg than it wont work as list pop as in dict there is 
#- no order


# .popitem() randomly remove keyvalue from dict. -
# - no argument givien in this
a=dict(a=1,b=2,c=3,d=4,e=5,f=6)
print(a.popitem())
print(a.popitem())
print(a)

# dic1.update(dic2) add dic2 keyvalue pair in dic1
dic1={1:'a',2:'b'}
dic2={'a':1,'b':2}
dic1.update(dic2)
print(dic1)
# update also rewrite things up
dic1['b']=99
print(dic1)
dic1.update(dic2)
print(dic1)

# EX
inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1}
stock_list=inventory.copy()
stock_list.update({"cookie":18})
#or stock_list["cookie"]=18 also add item
stock_list.pop("cake")
print(stock_list)

# DICTIONARY COMPREHENSION
# {_:_for_in_}
#making dict. from dict.
numbers=dict(first=1,second=2,third=3)
squared_num={key:value**2 for key,value in numbers.items()}
print(squared_num)
# making dict. with list using dict. comp.
q={num:num**2 for num in [1,2,3,4,5]}
print(q)
# from string
str1="ABC"
str2="123"
w={str1[i]:str2[i] for i in range(len(str1))}
print(w)

details=dict(name='danu',city='rampur',gate='qualified')
details1={key.upper():value.upper() for key,value in details.items()}
print(details1)

# with conditional logic
num_list=[1,2,3,4]
num_dic={num:("even" if num%2==0 else "odd") for num in num_list}
print(num_dic)

details1={(key.upper() if key is 'gate' else key):value.upper()
	for key,value in details.items()}
print(details1)

#EX
list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]
answer = {key:value for key,value in zip(list1,list2) }
		#or 
#answer = {list1[i]:list2[i] for i in range(len(list1)) }
print(answer)

#EX
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = {i[0]:i[1] for i in person}
print(answer)
		#or
#answer = {i:j for i,j in person}
		#or
#answer=dict(person)

#EX
print({i:0 for i in "aeiou"})
		#or
print(dict.fromkeys("aeiou",0))

#EX
answer = {i:chr(i) for i in range(65,91)}
print(answer)

