import sys
import string

def text_analyzer(cadena=None):
	upper, lower, punctation, spaces, sis = 0, 0, 0, 0, False
	print(cadena)
	changer = ""
	if (isinstance(cadena, list)):
		quit(print("you only can put 1 argument, and you send " + str(len(sys.argv) - 1) + " Arguments\n"))
	while not(cadena):
		cadena = input("What is the text to analyze?\n")
	changer = cadena
	if not(isinstance(cadena, str)):
		print(type(changer))
		quit(print("AssertionError: argument is not a string\n"))
	print(type(cadena[0]))
	print(type(changer))
	for character in str(changer):
		if (character.isupper()):
			upper += 1
		elif (character.islower()):
			lower += 1
		elif (character.isspace()):
			spaces += 1
		elif (character in string.punctuation):
			punctation += 1
	print("- " + str(upper) + " upper letter(s)")
	print("- " + str(lower)+ " lower letter(s)")
	print("- " + str(punctation) + " punctuation mark(s)")
	print("- " + str(spaces) + " space(s)")

if __name__ == "__main__":
	if len(sys.argv) == 2:
		text_analyzer(sys.argv[1])
	if (len(sys.argv) > 2):
		quit(print("you only can put 1 argument, and you send " + str(len(sys.argv) - 1) + " Arguments\n"))
