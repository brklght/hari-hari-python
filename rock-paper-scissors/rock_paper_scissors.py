import random, os, time

def wait(x):
	return time.sleep(x)

def play():
	user = input('"r" for rock, "p" for paper, "s" for scissors\n').lower()
	os.system('cls||clear')
	if user == 'r':
		print('You choose "Rock"')
	elif user == 'p':
		print('You choose "Paper"')
	else:
		print('You choose "Scissors"')	

	computer = random.choice(['r','s','p'])

	wait(1)

	for jankenpon in ['Jan','Jan Ken','Jan Ken Pon!']:
		os.system('cls||clear')		
		print(jankenpon)
		wait(.5)
	if user == computer:
		return 'It\'s a tie'

	if is_win(user,computer):
		return 'You won!'

	return 'You lost!'

def is_win(player,opponent):
	if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
		return True

print(play())