#arg can be sequnce like string tuple list range
#pr collection like dictionary set
print(len([]))
print(len((1,2,3,4,5)))

#iterable has builting method (dundar len)
print("hello".__len__())
print((1,2,3,4,5,6,6).__len__())

#when we call len() it is calling __len__() behind the scene


#we ca define our own __len__() method in our class
#and can do len(something..) it will call that and do task
class SpecialList:
	def __init__(self,data):
		self.__data=data
	def __len__(self):
		return 50
l1=SpecialList([1,40,30,100])

print(len(l1))
l2=SpecialList([])
print(len(l2))

class SpecialList1:
	def __init__(self,data):
		self.__data=data
	def __len__(self):
		return self.__data.__len__()//2

l1=SpecialList1([1,40,30,100])

print(len(l1))
l2=SpecialList1([1,2,3,4,5,6,7,8,9])
print(len(l2))