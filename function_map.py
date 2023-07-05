# it accepts atleast two arguments, a function and an iterable
#runs function for each value in iterable and returns a map
#that can be converted to other data structure
nums=[1,2,3,4,5,6,7]
doubles= map(lambda x:x*2, nums) #we can pass fn also isplace of lambda
print(doubles)
for i in doubles:
	print(i)
print('\n')

#for converting to list we only do this
doubles= list(map(lambda x:x*2, nums))
print(doubles)
#not like this
#print(list(doubles))

names=['danu','khan','aman']
tt=list(map(lambda name:name.upper(),names))
print(tt)

names=[{'first':'danu','last':'khan'},
{'first':'naj','last':'ansari'}
]
tt=list(map(lambda name:name['first'],names))
print(tt)
