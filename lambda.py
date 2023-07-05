#lambdas are like anonymous functions

def square(num): return num*num #fn name is square here

square2= lambda num: num*num #square2 is variable, not a function name
#lambda fn has no name
#in lambda only single expression is allowed, and automatically
#returns

print(square(7))
print(square2(7))

add= lambda a,b: a+b

print(square.__name__) #for printing name of function
print(square2.__name__)
print(add.__name__)

#we use lambda when passing function as a parameter to other
#function and dont want to use that again

import tkinter as tk
root=tk.Tk()
frame=tk.Frame(root)
frame.pack()

def say_hi():
	print("hello")

button = tk.Button(frame,
	text="click me",
	fg="red",
	command=lambda:print("hello"))     #print("hello"))                #say_hi)

button.pack(side=tk.LEFT)
root.mainloop()

# this will print hello on click, we can replace fn with
#lambda and cannot put print hello in command as it
#will print hello without button pressing
