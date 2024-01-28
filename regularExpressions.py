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



