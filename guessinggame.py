from random import randint
option="y"
print("---------game sarted-------")
while(option!="n"):
	guess=int(input("guess a number between 1 and 10"))
	number=randint(1,10)
	while(guess!=number):
		if(guess>number):
			print("too high")
		else:
			print("too low")
		guess=int(input("guess a number between 1 and 10"))
	print("you guessed it! you won!")

	option=input("do you want to play again? (y/n)")
print("thanks for playing. bye!")