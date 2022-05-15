from random_word import RandomWords
from hangman_visual import lives_visual_dict
import string, os


def get_valid_word():
	word = None
	r = RandomWords()
	while word == None or '-' in word or ' ' in word:
		word = r.get_random_word()
	return word

def hangman():
	word =  get_valid_word().upper()
	word_letters = set(word)
	alphabet =  set(string.ascii_uppercase)
	used_letters = set()
	lives = 7

	while len(word_letters) > 0 and lives > 0:

		print('\nLetters have been used: ', ' '.join(used_letters))

		word_list = [letter if letter in used_letters else '-' for letter in word]
		print(' '.join(word_list))
		print(lives_visual_dict[lives])
		user_letter = input('Guess a letter: ').upper()
		os.system('cls||clear')

		if user_letter in alphabet - used_letters:
			used_letters.add(user_letter)
			if user_letter in word_letters:
				word_letters.remove(user_letter)
			else:
				lives -= 1
				print(user_letter,' is not in word')

		elif user_letter in used_letters:
			print(user_letter, ' has been used')

		else:
			print(' is not a valid letter')

	if lives < 1:
		print(' '.join(word_list))
		print(lives_visual_dict[lives])
		print('You died. The word was', word)
	else:
		print('You win!')

if __name__ == '__main__':
    hangman()