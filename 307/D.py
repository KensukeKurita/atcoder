
import re

def remove_enclosed_letters(S):

    R = re.sub(pattern, '', S)
    
    if len(S) == len(R):
        return False, R
    else:
        return True, R


pattern = re.compile(r'\([a-z]*\)')
N = input()
result = input()
status = True
while status:
    status, result = remove_enclosed_letters(result)

print(result) 