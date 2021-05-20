import re
def valid_emails(filename):
	with open(filename, 'r') as f:
		f.readline()
		for line in f:
				lines = line.strip().split()
				pattern = r'^[A-Za-z0-9][A-Za-z0-9-]+@[A-Za-z]+\.(com|net|edu|gov)$'
				if re.match(pattern, lines[2]):
					print(lines[2])
		print('---------')
valid_emails('emails.txt')
