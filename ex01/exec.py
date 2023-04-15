import sys
def run():
	arg = sys.argv[1:]
	if (len(sys.argv ) > 1):
		tup = []
		for palabra in arg:
			tup.append(palabra[::-1])
		print(" ".join(tup[::-1]).swapcase())

if __name__ == "__main__":
	run()
