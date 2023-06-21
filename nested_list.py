temp=list()
for j in range(1,5):
	temp.append([i for i in range(1,5)])
print(temp)

print(temp[0][3])
print(temp[-1][-2])

for i in temp:
	print(i)


# nested list comprehension
[[print(val) for val in l] for l in temp]
# making list of list with comprehension
tt=[[i for i in range(1,4)] for val in range(1,4)]
print(tt)

tx=[["X" if i%2!=0 else "O" for i in range(1,4)] for val in range(1,4)]
print(tx)

print([["*" for i in range(1,4)] for val in range(1,4)])
[[print("*") for i in range(1,4)] for val in range(1,4)]
