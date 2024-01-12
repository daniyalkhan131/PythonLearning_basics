#for tabular data, simply saving records directly

#CSV files are a common file format for tabular data
#We can read CSV files just like other text files
#Python has a built-in CSV module to read/write CSVs more easily

with open("UsedForCSV.csv") as file:
    data = file.read()
print(data) #we get data in string format of full doc
#and then we split based on \n and ,

#instead use csv module

#reader - lets you iterate over rows of the CSV as lists Reader (file)
#DictReader - lets you iterate over rows of the CSV as OrderedDicts
#Keys are determined by the header row

from csv import reader
with open("UsedForCSV.csv") as file:
	csv_reader = reader(file)
	next(csv_reader)#for skipping the first row
	for fighter in csv_reader: #it is generator means loose value after once
		print(fighter)
		print(f"{fighter[0]} is from {fighter[1]}") #Use index to access data

from csv import reader
with open("UsedForCSV.csv") as file:
	csv_reader = reader(file)
	data=list(csv_reader) #converting to list
	
	print(data)


# Reading/Parsing CSV Using a DictReader:
from csv import DictReader
with open("UsedForCSV.csv") as file:
    csv_reader = DictReader(file)
    for row in csv_reader:
        # Each row is an OrderedDict!
        print(row['Name']) #Use keys to access data
        #it is ordered list because every time name comes first then other n so on

#Readers accept a delimiter kwarg in case your data isn't separated by commas.
#csv_reader = reader(file, delimiter="|")



#writing csv files

#using list

from csv import writer
with open("cats.csv", "w") as file: #if file dont exist then created
    csv_writer = writer(file)
    csv_writer.writerow(["Name", "Age"])
    csv_writer.writerow(["Blue", 3])
    csv_writer.writerow(["Kitty", 1])


#reading from one and prcoessing then stroing into another
from csv import reader, writer

with open('UsedForCSV.csv') as file:
	csv_reader = reader(file)
	# data converted to list and saved to variable
	fighters = [[s.upper() for s in row] for row in csv_reader]

with open('cats.csv', "w") as file:
	csv_writer = writer(file)
	for fighter in fighters:
		csv_writer.writerow(fighter)
#when we are writing in the same file then it is overwriting

# using nested with statements
with open('UsedForCSV.csv') as file:
	csv_reader = reader(file) #data never converted to list
	with open('cats.csv', "w") as file:
		csv_writer = writer(file)
		for fighter in csv_reader:
			csv_writer.writerow([s.upper() for s in fighter])
#it is more better as dont need to store in another variable


#using dictionary

#Dictwriter - creates a writer object for writing using dictionaries
#fieldnames - kwarg for the DictWriter specifying headers
#writeheader - method on a writer to write header row
#writerow - method on a writer to write a row based on a dictionary

from csv import DictWriter
with open("cats.csv", "w") as file:
	headers = ["Name", "Breed", "Age"]
	csv_writer = DictWriter(file, fieldnames=headers)
	csv_writer.writeheader()
	csv_writer.writerow({
		"Name": "Garfield",
		"Breed": "Orange Tabby",
		"Age": 10
	}) #we dont need to specify data in order unlike list


#example
from csv import DictReader, DictWriter

def cm_to_in(cm):
	return float(cm) * 0.393701

with open("UsedForCSV.csv") as file:
	csv_reader = DictReader(file)
	fighters = list(csv_reader)

with open("inches_fighters.csv", "w") as file:
	headers = ("Name","Country","Height")
	csv_writer = DictWriter(file, fieldnames=headers)
	csv_writer.writeheader()
	for f in fighters:
		csv_writer.writerow({
			"Name": f["Name"],
			"Country": f["Country"],
			"Height": cm_to_in(f["Height (in cm)"])
		})


#pickling
#storing the state of object state like game state in python
#and it convert to binary stream, serialized and stored
#and can be used by unpickling it

import pickle
class Animal:
	def __init__(self, name, species):
		self.name = name
		self.species = species

	def __repr__(self):
		return f"{self.name} is a {self.species}"

	def make_sound(self, sound):
		print(f"this animal says {sound}")


class Cat(Animal):
	def __init__(self, name, breed, toy):
		super().__init__(name, species="Cat") # Call init on parent class
		self.breed = breed
		self.toy = toy

	def play(self):
		print(f"{self.name} plays with {self.toy}")


blue = Cat("Blue", "Scottish Fold", "String")

# To pickle an object:
with open("pets.pickle", "wb") as file:
	pickle.dump(blue, file)
#if want data to be read by other like java or db then dont pickel it
#we pickle when want to be for python

#To unpickle something:
with open("pets.pickle", "rb") as file:
	zombie_blue = pickle.load(file)
	print(zombie_blue)
	print(zombie_blue.play())

print('-----for more objetcs pickling----')

buck= Cat("wetrwt", "sdvsv", "sdc")
with open("pets.pickle", "wb") as file:
	pickle.dump((blue,buck), file)
with open("pets.pickle", "rb") as file:
	zombie_blue,zombie_buck = pickle.load(file)
	print(zombie_blue)
	print(zombie_blue.play())
	print(zombie_buck)
	print(zombie_buck.play())


#json- javascript objet notation
#just like csv for representing data

#we can convert python data into json
#json.dumps formats a python object as a STRING of JSON.
#I didn't do a good job of emphasizing the fact that it returns a STRING.

import json

class Cat:
	def __init__(self, name, breed):
		self.name = name
		self.breed = breed
		
c = Cat("Charles", "Tabby")

# json.dumps returns a JSON STRING:

j = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
print(j)
# results in '["foo", {"bar": ["baz", null, 1.0, 2]}]'

j = json.dumps(c.__dict__)
print(j)
# results in '{"name": "Charles", "breed": "Tabby"}'


#using jsonpickel
#in this pickle using json it so can be stored in file
import jsonpickle

class Cat:
	def __init__(self, name, breed):
		self.name = name
		self.breed = breed

c = Cat("Charles", "Tabby")

# To JSONPICKLE 'c' the cat:
with open("cat.json", "w") as file:
	frozen = jsonpickle.encode(c)
	print(frozen)
	file.write(frozen)

# To bring back 'c' the cat using JSONPICKLE
with open("cat.json", "r") as file:
	contents = file.read()
	unfrozen = jsonpickle.decode(contents) #now we get back our object cat
	print(unfrozen)