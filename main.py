from math import log
from string import ascii_uppercase # pre-initialized string 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def bijective_base26(n):
	label = ""

	digitnum = int(log(n,26)) + 1
	for i in range(digitnum)[::-1]:
		label += ascii_uppercase[int(n/(26**i))-1]
		n -= (int(n/(26**i))*(26**i))

	return label

print(bijective_base26(27))