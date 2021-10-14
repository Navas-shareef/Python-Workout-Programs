#program to evaluate string followed by conditions
import re
def evaluate_string(input):
	if len(input) < 8:
		return False
	elif not bool(re.search("[A-Z]",input)):
		return False
	elif not bool(re.search("[1-9]",input)):
		return False
	elif not bool(re.search("['!','@','#','$','^','&','*']",input)):
		return False
	for i in ['abc','123','qwerty']:
		if i in input:
			return False
	return True				
	
print(evaluate_string("W$1fskdjfs@@4429"))	
print(evaluate_string("W$1fskdjfs@123@449"))			