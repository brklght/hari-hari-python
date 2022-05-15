import random, string

def generate_password(length):
	return ''.join([random.choice(string.ascii_letters + string.digits) for n in range(length)])

if __name__ == '__main__':
	password = generate_password(8)
	print(f"Your generated password: {password}")