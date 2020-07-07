#1. Importing Modules

import random

shapes = ('HEARTS','DIAMONDS','CLUBS', 'SPADES')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

play_on = True

#2. Card Class

class Card:

	def __init__(self,shape,rank):
		self.shape = shape
		self.rank = rank

	def __str__(self):
		return self.rank+ " of " +self.shape

#3. Deck Class

class Deck:

	def __init__(self):
		self.deck = []
		for shape in shapes:
			for rank in ranks:
				self.deck.append(Card(shape,rank))

	def __str__(self):
		deck_comp = ''
		for card in self.deck:
			deck_comp = deck_comp + '\n' + card.__str__()

		return 'The deck composes of: '+deck_comp

	def shuffle(self):
		random.shuffle(self.deck)

	def deal(self):
		single_card = self.deck.pop()
		return single_card

'''
Test Region I
decktester = Deck()
decktester.shuffle()
print (decktester)

'''


#4. Hand Class

class Hand():

	def __init__(self):
		self.cards = []
		self.value = 0
		self.aces = 0

	def add_card(self,card):
		self.cards.append(card)
		self.value = self.value + values[card.rank]

		if card.rank == 'Ace':
			self.aces = self.aces + 1

	def ace_adjust(self):

		while self.value > 21 and self.aces:
			self.value = self.value - 10
			self.aces = self.aces - 1


'''
Test Region II
decktester = Deck()
decktester.shuffle()

playertester = Hand()
removed_card = decktester.deal()
print(removed_card)
playertester.add_card(removed_card)
print (playertester.value)

'''

#5. Token Class

class Token:

	def __init__(self):
		self.total = 150
		self.bet = 0

	def winningbet(self):
		self.total = self.total + self.bet

	def losingbet(self):
		self.total = self.total - self.bet


#6. Functions for making bets

def take_bets(token):

	while True:

		try:
			token.bet = int(input("Place tokens to bet: "))
		except ValueError:
			print("Please provide an integer")
		else:
			if token.bet > token.total:
				print('Insufficient amount of tokens, you currently have {} tokens'.format(token.total))
			else:
				break

#7. Functions for taking hits

def hit(deck,hand):

	#single_card = deck.deal()
	hand.add_card(deck.deal())
	hand.ace_adjust()

#8. Functions for prompting player to hit or walk

def hit_or_walk(deck,hand):
	global play_on

	while True:
		z = input('Hit or Walk? Enter h or w')

		if z[0].lower() == 'h':
			hit(deck,hand)

		elif z[0].lower() == 'w':
			print('Player has chosen to walk with, Dealers turn')
			play_on = False
		else:
			print("Request not understood. Try again")
			#print("\n")
			#print("Enter h or w only!")
			continue
		break

#9. Functions for displaying cards

def reveal_some(player,dealer):
	print("\n Dealer's Hand:")
	print("One Hidden Card")
	print (dealer.cards[1])
	print ("\n Player's Hand")
	for card in player.cards:
		print(card)

def reveal_all(player,dealer):
	print ("\n Dealer's Hand")
	for card in dealer.cards:
		print(card)
	print ("\n Player's Hand")
	for card in player.cards:
		print(card)

#10. Functions for End of Game Scenarios

def player_bust(player,dealer,token):
	print ("PLAYER BUST!")
	token.losingbet()

def player_wins(player,dealer,token):
	print ("PLAYER WINS!")
	token.winningbet()

def dealer_bust(player,dealer,token):
	print ("DEALER BUST!PLAYER WINS!!")
	token.winningbet()

def dealer_wins(player,dealer,token):
	print ("DEALER WINS!!")
	token.losingbet()

def push_factor(player,dealer):
	print ("PUSH!!DEALER AND PLAYER DRAW!!")

#11. Game Logic

while True:
	#A. <--- Print an Opening Statement --->

	print ("WELCOME TO CEELO'S BLACK JACK version 1.01!!!")

	#B. <--- Create and shuffle a deck, then deal two cards to each player --->

	deck = Deck()
	deck.shuffle()

	playerhand = Hand()
	playerhand.add_card(deck.deal())
	playerhand.add_card(deck.deal())

	dealerhand = Hand()
	dealerhand.add_card(deck.deal())
	dealerhand.add_card(deck.deal())

	#C. <--- Provide Player tokens --->

	playertokens = Token()

	#D. <---Alert player to place bet --->

	take_bets(playertokens)

	#E. <--- Show cards but keep one dealer card hidden --->

	reveal_some(playerhand,dealerhand)

	#F. <--- Recall variable from hit or walk function --->

	while play_on:

		#G. <--- Alert a player to hit or walk --->
		hit_or_walk(deck,playerhand)

		#H. <---Show cards but keep one dealer card hidden again --->
		reveal_some(playerhand,dealerhand)

		#I. <--- If players hand exceeds 21, run player bust and break out of loop --->
		if playerhand.value > 21:
			player_bust(playerhand,dealerhand,playertokens)

			break


	if playerhand.value <= 21:

		while dealerhand.value < playerhand.value:
			hit(deck,dealerhand)

		#J. Show all Cards
		reveal_all(playerhand,dealerhand)

		#K. Run different winning scenarios
		if dealerhand.value > 21:
			dealer_bust(playerhand,dealerhand,playertokens)
		elif dealerhand.value > playerhand.value:
			dealer_wins(playerhand,dealerhand,playertokens)
		elif dealerhand.value < playerhand.value:
			player_wins(playerhand,dealerhand,playertokens)
		else:
			push_factor(playerhand,dealerhand)

	#L. Inform player of their token tota
	print('\n Player Total Tokens are at: {}'.format(playertokens.total))

	#M. Ask to play again
	new_game = input("Would you like to play another hand? y/n")

	if new_game[0].lower() == 'y':
		play_on = True
		continue
	else:
		print ("Thanks for playing :D")

		break

'''
Game: Black Jack
Version: 1.01
Developed by: Ceelo
Second attempt after walkthrough
Ref: Udemy (Python Bootcamp from Zero to Hero)
	 Google.com
	 www.w3schools.com
Date: 07/07/2020
'''



	



