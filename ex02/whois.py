import sys

if (len(sys.argv) == 2):
	if (sys.argv[1].isnumeric()):
		if (int(sys.argv[1]) == 0):
			print("I'm Zero.")
		elif (int(sys.argv[1]) % 2 == 0):
			print("I'm Even.")
		else:
			print("I'm Odd.")
	else:
		print("AssertionError: argument is not an integer")
elif (len(sys.argv) == 1):
	print("")
else:
	print("AssertionError: more than one argument are provided")