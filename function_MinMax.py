print(max(1,5,3,88,4))
print(max('a','f','b','p','z'))
print(max('4','3','45')) #how python interpret this?

#we can also pass an iterable
print(max([1,5,3,88,5,5,9,677,5,4]))
print(max((1,5,3,88,5,5,9,677,5,4)))
print(max('daniyalkhan'))
print(max({1:'a',3:'c',2:'b',4:'z',5:'g'}))

x='helloworld'
print(max(x))
print(min(x))

names=['danu','Naj','fizza','mu','nausheen','gulgulgul']
#it is giving according to ascii value as otherwise give danu
print(min(names))
print(max(names))

#for based on len of name
print(min(len(name) for name in names)) #inside is generator
#we want name
print(min(names,key=lambda x:len(x)))
print(max(names,key=lambda x:len(x)))



data = [{'title': 'sravan', 'name': 'jyothika','playcount':2},
{'title': 'yyyj', 'name': 'sfvfv','playcount':67},
{'title': 'dbbvc', 'name': 'xcvdb','playcount':6},
{'title': 'sddfdgf', 'name': 'ftyirti','playcount':4}]

print(max(data,key=lambda x: x['playcount']))
print(min(data,key=lambda x: x['playcount'])['title'])

#if not then we have to do like this, very very big
min=99999
for x in data:
	if x['playcount'] <min:
		min=x['playcount']
		t=x['title']
print(t,min)