temp=list()
for j in range(1,5):
	temp.append([i for i in range(1,5)])
print(temp)
# why we put print inside list brackets, i thought [] is-
# -for making list of value that for loop gives???
[[print(val) for val in l] for l in temp]
# and this gives full nested list
print([[val for val in l] for l in temp])

#how can value be tuple in dictionary
dic={(1,2):"danu","name":"khan",1:4}
print(dic)
# why with dict using we cannot use number as key
#d=dict(2="aaa") it shows error

