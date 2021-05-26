from random import randint

#This function takes in the amount of dice in the and, and then rolls the missing dice.
#Uses randint. Also sorts the rolled dice.
def roll(hand):
	out=[]
	for i in range(5-len(hand)):
		out.append(randint(1, 6))

	return sorted(out)





#This function calculates the score of a set of 5 dice(die?)
def score(hand):
	#First create a list with only the unique 'faces' of the die in the hand. A set can only contain one instance of a value, so it automatically works for this.
	unique = sorted(set(hand))
	
	countlist = []
	is_consecutive = True
	last = 0
	
	#Then a list is created which will contain how many times each face shows up in the hand.
	for i in unique:
		countlist.append(hand.count(i))
		
		#The loop also checks for each item in unique if it is consecutive to the previous item(or zero for the first item). This is to check if the hand is a straight later
		if i - last > 1:
			is_consecutive = False
		last = i
	
	#The function also returns which face is responsible for the score. So for a hand of [3,3,3,4,5] it needs to return [3, 4, 5].
	#This is done by sorting the 'unique' list based on what is corresponding value is in 'countlist'.
	values = sorted(unique, reverse = True, key = lambda j: countlist[unique.index(j)])
	#The countlist is sorted in reverse order, and a string containing the items in countlist is created.
	countlist.sort(reverse = True)
	countstring=''.join(str(e) for e in countlist)
	
	#This string is used to input into a dictionary, containing the score corresponding to each combination of dice.
	scores = {
		'5':(1, 'five of a kind'),
		'41':(2, 'four of a kind'),
		'32':(3, 'full house'),
		'11111':(4, 'straight'), 
		'311':(5, 'three of a kind'),
		'221':(6, 'two pair'),
		'2111':(7, 'pair')
	}
	
	score = scores[countstring]
	
	#The 'countlist' will be [1,1,1,1,1] for both Straight and Bust. In order to distinguish between these the 'is_consecutive' variable is checked. 
	#If it's true, then the hand is a Straight. Else the hand is a bust.
	if score == 4 and is_consecutive == False:
		score = (8, 'bust')
	return score, values, countlist
	

#this function acts as the 'ai' for the cpu player. It takes in a hand, and then outputs the dices to keep.
def ai_select(hand):
	#check if all the dices are unique.
	unique = sorted(set(hand))
	if len(unique) == 5:
		#If they are all unique then the cpu has either a strate or a bust. The cpu will then select the largest consecutive series of numbers from the hand.
		last = 0
		cut = 0
		for i in range(1, len(unique)):
			if unique[i] - unique[i-1] > 1 :
				cut = i
		print(cut)
		if cut < 3:
			new_hand = unique[cut:5]
		else:
			new_hand = unique[0:cut]
	else: 
		#Else the hand contains multiple of the same dice faces. The cpu will then select all the dice faces which occur more than once.
		cur_score = score(hand)
		new_hand = hand
		
		for i in cur_score[1]:
			if cur_score[2][cur_score[1].index(i)] == 1:
				new_hand.remove(i)
	
	return new_hand

def player_select(hand):
	player_keep = input('Your answer: ')
	new_hand=[]
	for c in player_keep:
			if c.isdigit():
				new_hand.append(hand[int(c)-1])
	return(new_hand)			
				
def format_roll(roll):
	return (''.join((str(c)+', ') for c in roll))[:-2]


	

dummy = input('Welcome to Dice Poker! Beat the computer by getting the highest score')




hand_comp = []
hand_player = []

#Main loop
for i in range(3):
	print('\nRound #{}'.format(i+1))
	#computer roll
	roll_comp = roll(hand_comp)
	hand_comp += roll_comp
	print('The computer rolled: {}'.format(format_roll(hand_comp)))
	if i < 2:
		hand_comp = ai_select(hand_comp)
	print('and kept: {}\n'.format(format_roll(hand_comp)))

	
	#player roll
	dummy = input('Press enter to roll')
	roll_player = roll(hand_player)
	hand_player += roll_player
	print('You rolled: {}'.format(format_roll(hand_player)))
	if i < 2:
		print('Which dice do you want to keep?(choose from dice 1, 2, 3, 4, 5)')
		hand_player = player_select(hand_player)
	
	
#After the main loop is finished, compare the scores using the score functions. whoever has the lowest score wins.
score_comp = score(hand_comp)
score_player = score(hand_player)

print('The computer has a {}'.format(score_comp[0][1]))
print('You have a {}'.format(score_player[0][1]))

if score_comp[0][0] < score_player[0][0]:
	print('The computer won, haha!')

elif score_comp[0][0] > score_player[0][0]:
	print('Congratulatioooonss! You won')

else:
	#If the scores are equal then we check the values[] from the score function.
	for i in range(len(score_comp[1])):
		if score_comp[1][i] > score_player[1][i]:
			print('The computer won, haha!')
			break
			
		elif score_comp[1][i] < score_player[1][i]:
			print('Congratulatioooonss! You won')
			break
		else:
			print('tie')
			break




	











