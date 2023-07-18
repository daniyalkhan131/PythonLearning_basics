from random import shuffle
class Card:
	def __init__(self,value,suit):
		self.value=value
		self.suit=suit

	def __repr__(self):
		return "{} of {}".format(self.value,self.suit)


	pass


class Deck:
	cards=52
	def __init__(self):
		suits=['Hearts','Diamonds','Clubs','Spades']
		values=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
		#self.cards=[]
		#	for suit in suits:
		#		for value in values:
		#			self.cards.append(Card(value,suit))

		#or list comp.
		self.cards=[Card(value,suit) for suit in suits for value in values]
		print(self.cards)

	def __repr__(self):
		return f"Deck of {self.count()} cards"

	def count(self):
		return len(self.cards)

	def _deal(self,num): #this is an internal method
		count=self.count()
		actual=min([count,num])
		if count==0:
			raise ValueError('All cards have been dealt')
		cards=self.cards[-actual:]
		self.cards=self.cards[:-actual]
		return cards

	def deal_card(self):
		return self._deal(1)[0]

	def deal_hand(self,hand_size):
		return self._deal(hand_size)

	def shuffle(self):
		if self.count() <52:
			raise ValueError("only full decks can be shuffled")
		shuffle(self.cards)
		return self #it is conventional thing to do


c1=Card("A","Hearts")
c2=Card("9","Diamonds")
c3=Card("K","Spades")

print(c1,c2,c3)

d=Deck()
print(d._deal(5))
print(d.count())
print(d._deal(47))
print(d.count())

d2=Deck()
print(d2.count())
d2.shuffle()
print(d2.cards)

card=d2.deal_card()
print(card)
hand=d2.deal_hand(5)
print(hand)