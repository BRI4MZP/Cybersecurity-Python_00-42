import sys
morsedict = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ' ':'/'}

if len(sys.argv) > 1:
	changer = ""
	returner = ""
	count = 0
	for i in range(len(sys.argv) - 1):
		count+= 1
		for x in sys.argv[count]:
			if x.upper() not in morsedict.keys():
				# print(morsedict.keys())
				quit("ERROR")
			changer = changer + str(morsedict[x.upper()] + ' ')
		returner = returner + ' ' + str(sys.argv[i + 1])
	print(changer)

#     data = sys.argv[1]
#     keys = list(morsedict.keys())
    
#     changer = ""
#     returner = ""
#     for x in data:
#         if x.upper() not in keys:
#             quit('ERROR')
#         changer += str(morsedict[x.upper()])
#     print(changer)