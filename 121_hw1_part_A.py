## Mengqi Li
## 92059150
## CS 121 Assignment 1 part A

import operator
import os
import re
import timeit
import sys

def tokenize(TextFilePath):
	SYMBOL ='[-_\s\n,.<>/?:;\"\'\[\]{ }\\\|`~!@#$%^&*()=\+]+'
	pattern = re.compile(SYMBOL)
	Token = []
	try:
		File = open(TextFilePath, encoding='ASCII')
		for Line in File:
			temp = pattern.split(Line.lower())
			Token.extend([x for x in temp if len(x) >= 1])
		return Token
	except:
		print("Not a ASCII encoding file!")
		sys.exit(0)

def computeWordFrequencies(Token):
	Result = {}
	for t in Token:
		if t not in Result.keys():
			Result[t] = 1
		else:
			Result[t] += 1
	return Result

def main():
	if len(sys.argv) != 2:
		print("Need one arguments for input file")
		sys.exit(0)
	else:
			TextFilePath = sys.argv[1]
			if os.path.exists(TextFilePath):
				print(TextFilePath,"loaded successfully!")
				
				start_point=timeit.default_timer()
		
				TokenList = sorted(computeWordFrequencies(tokenize(TextFilePath)).items(), key=operator.itemgetter(1), reverse = True)
		
				end_point=timeit.default_timer()
		
				for word in TokenList:
					print("\"",word[0], "\" :", word[1])
				print("Process using:",end_point-start_point)
				
			else:
				print("File does not exist!")
				sys.exit(0)
		
		

if __name__ == "__main__":
    main()