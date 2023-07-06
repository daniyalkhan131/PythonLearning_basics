l1=[1,2,3,4,5]
l2=[6,7,8,9,0]
z=zip(l1,l2)
print(z)#get iterator of tuples
print(list(z))
print(dict(z)) #again we are unable to do this
print(dict(zip(l1,l2))) #convert it into dict

#it wil stop with shorter list the iteration
l3=[1,2,3,4,5,6,7]
print(list(zip(l2,l3)))

words=['danu','khan','daniyal','khan']
print(list(zip(l1,l2,words)))


#we can use * to unpack things like
p=[(17,32),(10,42),(31,22),(91,62),(12,26),(13,25)]
print(list(zip(*p)))


mid=[80,91,78]
final=[98,89,53]
students=['danu','naj','mus']

#final_grades=[max(pair) for pair in zip(mid,final)]

final_grades={t[0]:max(t[1],t[2]) for t in zip(students,mid,final)}
print(final_grades)

#or

scores=zip(
	students,
	map(
			lambda pair:max(pair),
			zip(mid,final)
			)
	)
print(dict(scores))

#for avg grades
scores=zip(
	students,
	map(
			lambda pair:(pair[0]+pair[1])/2,
			zip(mid,final)
			)
	)
print(dict(scores))