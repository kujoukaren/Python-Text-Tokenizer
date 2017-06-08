## Mengqi Li
## 92059150
## CS 121 Assignment 1 part B

import os
import re
import sys
import timeit

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
	
def compare_token(token_1, token_2):
	return len(list(set(token_1) & set(token_2)))
	
def main():
	if len(sys.argv) != 3:
		print("Need two arguments for input file")
		sys.exit(0)
	else:
		input_file_1 = sys.argv[1]
		input_file_2 = sys.argv[2]
		if os.path.exists(input_file_1) and os.path.exists(input_file_2):
			print(input_file_1,"loaded successfully!")
			print(input_file_2,"loaded successfully!")
			
			start_point=timeit.default_timer()
			
			token_1 = tokenize(input_file_1)
			print("File_1 token collected")
			token_2 = tokenize(input_file_2)
			print("File_2 token collected")
			print(compare_token(token_1, token_2))
			
			end_point=timeit.default_timer()
			
			print("Process using:",end_point-start_point)
		
		else:
			print("File does not exist!")
			sys.exit(0)
			
if __name__ == "__main__":
    main()
	