from random import choice
l=["rock","paper","scissor"]
option="y"
while(option!='n'):
	print("-------ROCK PAPER SCISSORS-------")
	player1=choice(l)
	player2=input("enter your move").lower()

	print(f"computer selected- {player1}")
	print(f"you selected- {player2}")

	if(player1==player2):
		print("game tie play again")
	elif(player1=="rock"):
		if(player2=="scissor"):
			print("computer wins")
		else:
			print("you wins")
	elif(player1=="paper"):
		if(player2=="rock"):
			print("computer wins")
		else:
			print("you wins")
	elif(player1=="scissor"):
		if(player2=="rock"):
			print("you wins")
		else:
			print("computer wins")
	option=input("do you want to play again (y/n)")
