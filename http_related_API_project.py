import requests
import random
import pyfiglet


header=pyfiglet.figlet_format("DAD JOKE 3000")
print(header)
url="https://icanhazdadjoke.com/search"

strr=input("enter domain of joke: ")
res=requests.get(
	url,
	headers={"Accept":"application/json"},
	params={"term":strr}
	)

data=res.json()["results"]
print("----------------------------------------")
if data:
	if len(data)>1:
		print(f"printing one out of {len(data)} jokes")
		print(random.choice(data)["joke"])
	else:
		print("printing the only joke got")
		print(data[0]["joke"])