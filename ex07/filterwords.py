import sys
import string

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

def text_analyzer(array=None, limit=None):

	changer = []
	for word in array:
		count = 0
		for letter in word:
			if (letter in punctuations):
				count += 1
		if len(word) - count > limit:
			changer.append(word)
	changer = changer
	print(changer)

if __name__ == "__main__":
	try:
		array = sys.argv[1].translate(str.maketrans('', '', punctuations))
		number = int(sys.argv[2])
		text_analyzer(array.split(' '), number)
	except:
		quit(print("ERROR\n"))
