# iterable objects is collectn of items like list,string,range etc
# "hello" [1,2,3,4,5] range(1,10)
# range(1,8) generate 1 to 7 numbers

for i in "daniyal":
	print(i)
for i in [4,7,3,'h',[4,5]]:
	print(i*10)
for i in range(1,8):
	print(i)
print('\n')

# ranges represents immutable sequence of numbers(which are
# -ordered) , range generate sequence of ordered nmbers
# range(7)  give 0 to 6
# range(1,7) give 1 to 6
# range(1,10,2) stepsize is 2
# range(7,0,-1)

r=range(7,0,-1)
l1=list(r)
print(l1)
print(r)

# adding odd numbers
sum=0
for i in range(101,200,2):
	sum+=i
print(sum)

# EX
times=int(input("how many times i have to say"))
for time in range(times):
	print(f"time {time+1}:clean up your room")

#EX
x=None
for i in range(1,21):
	if i==4 or x==13:
		x="unlucky"
	elif i%2==0:
		x="even"
	else:
		x="odd"
	print(f"{i} is {x}")


msg=input("secret password")
while msg != "banana":
	print("wrong")
	msg=input("secret password")
print("right")

for i in range(1,11):
	print(i)
i=1
while i<11:
	print(i)
	i+=1

#EX
#for i in range(1,10):
#	print()
#	for j in range(i):
#		print("\U0001f600", end="")
#or (this is string multiplication methon)
print()
for i in range(1,10):
	print("\U0001f600"*i)

i=1
while i<10:
	j=0
	print()
	while j<i:
		print("\U0001f600", end="")
		j+=1
	i+=1

print()
print("---------centered-------")
for i in range(1,10):
	print()
	for k in range(i,10):
		print(" ", end="")
	for j in range(i):
		print("* ", end="")

#EX
str1=input("hey how's it going")
while(str1!="stop copying me"):
	print(str1)
	str1=input() # we can also do str1=input(str1)
				 # or str1=input(f"{str1} :")
				 #here we are actuall combining print and input
				 #because input has inbuilt
print("UGH FINE YOU WIN")

times=int(input("How many time do i have to tell you?"))
for time in range(times):
	print("clean your room!")
	if time==4:
		print("do you even listen anymore?")
		continue
