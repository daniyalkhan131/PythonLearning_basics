#sorted works on anything that is iterable
#return new list sorted
l=[2,5,2,9,4,6,9,4]
l1=sorted(l)
print(l1)
print(sorted('daniyalkhan'))

#.sort() method sort in that list only
l.sort()
print(l)

l=[2,5,2,9,4,6,9,4]
#descending order
print(sorted(l,reverse=True))

print(sorted((1,7,3,5,9,88,0,45,678,23)))#returns list but accept tuple

users=[{'username':'danu','tweets':['akdnfafka']},
{'username':'gul','tweets':['akdnfafka']},
{'username':'naushen','tweets':[]},
{'username':'fizza','tweets':[]},
{'username':'naj','tweets':[],'num':10,'tt':'io'},
{'username':'mus','tweets':'akdnfafka','color':'pruple'}]

print(sorted(users,key=len)) #key is for telling what should be sorted
#and should be sorted

print()
#for sorting based on username
print(sorted(users,key=lambda user:user['username']))
print()
#based on len of tweets
print(sorted(users,key=lambda user:len(user['tweets']),reverse=True))