# 1- DNS lookup
# 2-computer request
# 3- server process request
# 4- server response
# 2-4 is request response cycle

#DNS lookup is like phonebook for internet 

#view/developers/developers tools for seeing the website request response


#http headers, it contains meta data
#request header include accept(like html,xml,json), cache control, user-agent
#response headers include access-control-allow-origin, allowed

#response status- 2xx success, 3xx redirect, 4xx clieant error, 5xx server error


#http verbs
#get useful for retreiving data, data passed in query string, no side effects, 
#can be cached, can be bookmarked

#post useful for writing data, data passed in request body, side effects
#can't be cached, can't be bookmarked

#API- application programming interface
#it allows to get data from another app without needing to understand how app works
#json xml are standrd for data transfer

import requests

url='https://news.ycombinator.com/' #http means we want to get html back
res=requests.get(url)
print(res)
print(res.ok)
print(res.headers)
#print(res.text)
print(res.status_code)

#we want only data and in json , so we do this using headers
url='https://icanhazdadjoke.com/'

#res=requests.get(url,headers={"Accept":"text/html"}) we can pass multiple in headers
#res=requests.get(url,headers={"Accept":"text/plain"}) #but site must be 
#setup to handle this

#for getting in json
res=requests.get(url,headers={"Accept":"application/json"}) 
print("only joke from that website not entire html text")
print(res.text)
print(res.json()) #it convert to python dict


#query string
#A way to pass data to the server as part of a GET request
#http://www.example.com/?key1=value1&key2=value2

## option 1
#response = requests.get (
#"http://www.example.com?keyl=valuelskey2=value2"
# option 2 - preferable!
#response = requests.get (
#"http://www.example.com",
#params={
#"keyl": "valuel"
#"key2": "value2"
#}

url='https://icanhazdadjoke.com/search'

res=requests.get(
	url,
	headers={"Accept":"application/json"},
	params={"term":"dad", "limit":1}
	) 
data=res.json()
print(data["results"])