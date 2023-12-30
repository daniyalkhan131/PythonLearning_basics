def add(num1,num2):
	return num1+num2
def print_name():
	print(f"my __name__ is {__name__}")

#this will be run when module is imported but we can prevent this using this
if __name__=="__main__":
	print_name()