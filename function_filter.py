#there is a lamda for each value in iterable
#returns filter object that canbe converted
#the functn or lambda define need to return true or false (bool)

names=['danu','asad','aman','naj','sundus']
a_names=filter(lambda x: x[0]=='a', names)
print(a_names)
print(list(a_names)) #only first time we can do this conversion

#we can do these things map n filter using lsit comprehension also

users=[{'username':'danu','tweets':['akdnfafka']},
{'username':'gul','tweets':['akdnfafka']},
{'username':'naushen','tweets':[]},
{'username':'fizza','tweets':[]},
{'username':'naj','tweets':[]},
{'username':'mus','tweets':'akdnfafka'}]


inactive_users=list(filter(lambda x: len(x['tweets'])==0,users))
print(inactive_users)

#[] '' 0 are inherently empty
inactive_users1=list(filter(lambda x: not x['tweets'],users))
print(inactive_users1)


#combining filter and map
names=['danu','asad','aman','naj','sundus']
#print of those less than 5 char

friend=list(map(lambda name: f"your friend is {name}",filter(lambda value: len(value)<5,names)))
print(friend)
#filter gives list of selected firends then map gives string

#for tweeter users only username
inactive_users=list(map(lambda x: x['username'].upper(),filter(lambda x: not x['tweets'],users)))
print(inactive_users)


#why use this when have list comprehension
print([f"your friend is {name}" for name in names if len(name)<5])
print([user['username'].upper() for user in users if not user["tweets"]])
#we can do with this but need to know as can find in docs or projects etc
