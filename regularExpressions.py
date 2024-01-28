#regular expression or regex

#a way of describing patterns withing search strings

#use cases
#• Credit Card number validating
#• Phone number validating 
#• Advanced find/replace in text
#• Formatting text/output
#• Syntax highlighting

#validating emails
#colt@gmail.com carly.simon@yahoo.com rosa-98@meals.org david+lee_roth@hotmail.com

#Starts with 1 or more letter, number,+,_. then
#A single @ sign then
#1 or more letter, number, or - then
#A single dot then
#ends with 1 or more letter, number,-, or.

#(^[a-zA-ZO-9_.+-]+@[a-zA-ZO-9-J+1.[a-zA-ZO-9-J+$)

#without RE we have to use a lot of if statements loops and all

#use pythex website to understand RE


#\. means . use \ for saying that next char is not special


#\d digit 0-9
#\w letter, digit, or underscore
#\s  whitespace character
#\D not a digit
#\W not a word character
#\Snot a whitespace character
# . any character except line break

# + one or more
# {x} exactly x times 
#{x,y} x to y times
#{x,} x or more times
#* zero or more times
#? once or none

#[a-z] define range
#[aeiou] any one in the list will be searched
#[^aeiou] any one not in the list will be searched


#anchors and boundaries
# ^ start of string or line
# $ end of string or line
# \b word boundary


#logical operation
# | or
# 

#(Mr\.|Mrs\.) ([A-Za-z]+) ([A-Za-z]+) it gives 3 match to Mr. daniyal khan as
#3 components matching one after another, in first component having or operator



#import regex module 
import re
#define our phone number regex
pattern = re.compile(r'\d{3} \d{3}-\d{4}') #r for raw string, by this we dont need
#to tell \ before actual \d
print(pattern)
#search a string with our regex
res = pattern.search('Call me at 415 555-4242!')
print(res)

print(res.group())

#search give first macth not all
#use findall
res = pattern.findall('Call me at 415 555-4242! or 334 999-2343')
print(res)


#we can also do without creating RE object
t=re.search(r'\d{3} \d{3}-\d{4}','Call me at 415 555-4242! or 334 999-2343')
print(t.group())



import re
def extract_phone(input):

	phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
	match = phone_regex.search (input)
	if match:
		return match.group ()
	return None

def extract_all_phone(input):

	phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
	match = phone_regex.findall(input)
	if match:
		return match
	return None

print (extract_phone ("my number is 432 567-8976"))
print (extract_phone ("my number is 432 567-897622"))
print (extract_phone ("432 567-8976 sdfvdsvds"))
print (extract_phone ("432 567-8976"))

print(extract_all_phone("432 567-8976 and 988 345-3456"))


def is_valid_phone(input):
	phone_regex = re.compile(r'^\d{3} \d{3}-\d{4}$')
	match = phone_regex.search(input)
	if match:
		return True
	return False
#or can use
def is_valid_phone(input):
	phone_regex = re.compile(r'^\d{3} \d{3}-\d{4}$')
	match = phone_regex.fullmatch(input)
	if match:
		return True
	return False

print(is_valid_phone ("432 567-8976"))
print(is_valid_phone ("432 567-8976 ads"))
print(is_valid_phone ("asd 432 567-8976 d"))


url_re=re.compile(r'https?://www\.[A-za-z-]{2,256}\.[a-z]{2,6}[-a-zA-Z0-9@:%_\+.~#?&//=]*')
match=url_re.search("https://www.udemy.com/course/the-modern-python3-bootcamp")
print(match.group())

url_re=re.compile(r'(https?)://(www\.[A-za-z-]{2,256}\.[a-z]{2,6})([-a-zA-Z0-9@:%_\+.~#?&//=]*)')
match=url_re.search("https://www.udemy.com/course/the-modern-python3-bootcamp")
print(match.groups()) #use groups, but have different components defined in re

#or 
print('all',match.group(0))
print('protocol',match.group(1))
print('domain',match.group(2))
print('remain',match.group(3))



#ading name tag to it ehich we want to extract
def parse_name(input):
	regex=re.compile(r'^(Mr\.|Mrs\.|Ms\.|Mdme\.) (?P<first>[A-Za-z]+) ([A-Za-z]+)$')
	match=regex.search(input)
	print(match.groups())
	print(match.group('first'))

parse_name("Mr. Daniyal Khan")



#compilation flags
pat1=re.compile(r'^( [a-z0-9_\.-]+)@([0-9a-z\.-]+)\.([a-z\.]{2,6})$')
#for more clear writig for large RE's
pattern = re.compile(r"""
	^([a-z0-9 \.-]+) #first part of email 
	@                #single @ sign
	([0-9a-z\.-]+)    #email provider
	\.                #single period
	([a-z\.]{2,6})$   #com, org, net, etc.
""", re.VERBOSE |re.IGNORECASE) #ignore case so that small and capital all
#included and verbose is for writing like this


t=pattern.search("thomas123@Yahoo.com")
print(t.group())
print(t.groups())




#substitution basics
text="last night Mrs. Daisy and Mr. White murdered Ms. Chow"

pattern=re.compile(r'(Mr\.|Mrs\.|Ms\.) [a-z]+',re.I)
print(pattern.search(text).group())

result=pattern.sub("--dash--",text)
print(result)

#we can also do like Mrs. D Mr. W
text="last night Mrs. Daisy and Mr. White murdered Ms. Chow"

pattern=re.compile(r'(Mr\.|Mrs\.|Ms\.) ([a-z])[a-z]+',re.I)
print(pattern.search(text).group())

result=pattern.sub("\g<1> \g<2>",text) #\g<1> means group or component 1st
print(result)





#swapping file names

titles = [
    "Significant Others (1987)",
    "Tales of the City (1978)",
    "The Days of Anna Madrigal (2014)",
    "Mary Ann in Autumn (2010)",
    "Further Tales of the City (1982)",
    "Babycakes (1984)",
    "More Tales of the City (1980)",
    "Sure of You (1989)",
    "Michael Tolliver Lives (2007)"
]
#we want like "1978 - Tales of the city"
titles.sort()
#print(titles)

fixed_titles = []

pattern = re.compile(r'(?P<title>^[\w ]+) \((?P<date>\d{4})\)')
for book in titles:
    # result = pattern.sub("\g<2> - \g<1>", book)
    result = pattern.sub("\g<date> - \g<title>", book)

    fixed_titles.append(result)
fixed_titles.sort()
print(fixed_titles)