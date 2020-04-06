import sys

morse = {
	'A':'.-',
	'B':'-...',
	'C':'-.-.',
	'D':'-..',
	'E':'.',
	'F':'..-.',
	'G':'--.',
	'H':'....',
	'I':'..',
	'J':'.---',
	'K':'-.-',
	'L':'.-..',
	'M':'--',
	'N':'-.',
	'O':'---',
	'P':'.--.',
	'Q':'--.-',
	'R':'.-.',
	'S':'...',
	'T':'-',
	'U':'..-',
	'V':'...-',
	'W':'.--',
	'X':'-..-',
	'Y':'-.--',
	'Z':'--..',
	' ':' '
	}

i = 1
j = 0
talk = ""

if (2 > len(sys.argv)):
	talk = "<a-zA-Z string>"
while (i < len(sys.argv)):
	for j in sys.argv[i]:
		j = j.upper()
		if (j in morse.keys()):
			talk += morse[j]
		else:
			talk = "<a-zA-Z string>"
			break
	i += 1
print(talk)
