def is_isogram(string):
	for i in string.lower():
		if(i.isalpha()==True):
			count = 0
			for j in string.lower():
				if(j.isalpha()==True):
					if(j == i):
						count += 1
					if(count > 1):
						return False  
	return True

