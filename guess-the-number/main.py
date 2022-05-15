
import random
import os, time

def guess(x):
	random_number = random.randint(1,x)
	guess = 0
	while guess != random_number:
		guess = int(input(f'Guess a number between 1 and {x}: '))
		if guess > random_number:
			print('try lower')
		elif guess < random_number:
			print('try higher')
		else:
			print(f'{guess} is the correct number')

def computer_guess(x):
	low = 1
	high = x
	feedback = ''
	while feedback != 'c':
		if low != high:
			guess = random.randint(low,high)
		else:
			guess = low
		feedback = input(f'Is {guess} too high (H), too low(L), or correct (C)?').lower()
		if feedback == 'h':
			high = guess - 1
		elif feedback == 'l':
			low = guess + 1

	print(f'Your number is {guess}')


def guess_given_number():
	l = random.sample(range(100), 21)
	set_l = [[],[],[]]
	for i in range(3):
		for j in range(7):
			set_l[i].append(l[0])
			l.pop(0)
	for i in range(3):
		l, set_l = draw_deck(l, set_l)
		l, set_l = sort_deck(set_l)
	print(f'Your number is: {l[10]}')

def draw_deck(l,set_l):
	confirm = False
	while confirm not in [1,2,3]:

		print('In which row is your choosen number?')
		for i in range(3):
			print(f'row {i+1}: {set_l[i]}')
				
		confirm = int(input())
		if confirm not in [1,2,3]:
			print('pick row 1, 2, or 3!')
			time.sleep(1)
		os.system('cls||clear')
		if confirm == 1:
			temp_set = set_l[0]
			set_l[0] = set_l[1]
			set_l[1] = temp_set
		elif confirm == 3:
			temp_set = set_l[2]
			set_l[2] = set_l[1]
			set_l[1] = temp_set
	return l, set_l

def sort_deck(set_l):
	l = []
	for i in range(3):
		for number in set_l[i]:
			l.append(number)
	temp_l = l
	set_l = [[],[],[]]
	while len(temp_l) > 0:
		for i in range(3):
			set_l[i].append(temp_l[0])
			temp_l.pop(0)
	for i in range(3):
		for number in set_l[i]:
			l.append(number)			
	return l, set_l	

guess_given_number()