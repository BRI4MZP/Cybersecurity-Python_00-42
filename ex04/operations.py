import sys
import string

def operations(numa, numb):
	
	try:
		numa = int(numa)
		numb = int(numb)
	except:
		quit(print("AssertionError: only integers\n"))
	try:
		print("Sum:              " + str(numa + numb))
	except:
		print("Sum:      Error")
	try:
		print("Difference:       " + str(numa - numb))
	except:
		print("Difference:      Error")
	try:
		print("Product:          " + str(numa * numb))
	except:
		print("Product:        Error")
	try:
		print("Quotient:         " + str(numa / numb))
	except:
		print("Quotient:         ERROR (division by zero)\n")
	try:
		print("Remainder:        " + str(numa % numb))
	except:
		print("Remainder:        ERROR (modulo by zero)\n")

if __name__ == "__main__":
	if len(sys.argv) == 3:
		operations(sys.argv[1], sys.argv[2])
	if (len(sys.argv) > 3 or len(sys.argv) < 3):
		if (len(sys.argv) == 1):
			print("Usage: python operations.py <number1> <number2>\nExample:\n    python operations.py 10 3\n")
		else:
			quit(print("you only can put 2 argument, and you send " + str(len(sys.argv) - 1) + " Arguments\n"))