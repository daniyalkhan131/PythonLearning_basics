#You can read a file with the open function
#open returns a file object to you
#file contain other info also like format type, etc so we get object of file
#You can read a file with the read method

f=open("file_data.txt")
print(f)
#print(help(f))

print(f.read()) #arg in read is -1 default that means all the letters in file

#print(f.read()) it will read nothing because of cursor is at end position 
#when we read first

#Python reads files by using a cursor
#This is like the cursor you see when you're typing
#After a file is read, the cursor is at the end

#to move the cursor use seek method

#python open is different, like we dont need to read again the file if 
#we make some changes then in terminal it will track and when we write
#f.read() then show the added part if previous text read
#se we have to close the file after work done

f.seek(0)
print(f.read())

print()
#if having thousands of line and want to read line by line after another then
f.seek(0)
print(f.readline())
print(f.readline())

#.readlines() give all lines but put them in list
f.seek(0)
print(f.readlines())


#closing a file
#You can close a file with the close method
#You can check if a file is closed with the closed attribute
#Once closed, a file can't be read again

print(f.closed)
f.close()
print(f.closed)


print()
#generaly used 'with', because anything happen, file read or error occur
#file will close automatically
with open('file_data.txt') as file:
	data=file.read()

print(data) #file is closed and we read data from that
print(file.closed)

# .__enter__() for opening file and .__exit__() for exiting file
#if we define these for our object then we can use 'with' keyword

#writing files
#You can also use open to write to a file
#Need to specify the "w" flag as the second argument

with open("file_data.txt", "w") as file:
	file.write("Writing files is great\n")
	file.write("Here's another line of text\n")
	file.write("Closing now, goodbye!")
#the original content in file is overwriten with write and this will be written
#and if file not exist then it will be created


#Modes for Opening Files
#r - Read a file (no writing) - this is the default
#w - Write to a file (previous contents removed)
#a - Append to a file (previous contents not removed)
#r+ - Read and write to a file (writing based on cursor)

with open("file_data.txt", "a") as file:
	file.write("daniyal khan\n")
	file.write("----------\n")

with open("file_data.txt", "a") as file:
	file.seek(0) #but append nly append at last
	file.write("daniyal khan\n") 

#r+ can write anywhere by it will replace after cursor size equal to text inserted
with open("file_data.txt", "r+") as file:
	file.write("daniyal khan\n")
	file.seek(10)
	file.write("-----::::-------")