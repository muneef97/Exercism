def latest(scores):
    return scores[-1]

def personal_best(scores):
    return max(scores)

def personal_top_three(scores):
	maximum = []
	for i in range(len(scores)):
		maximum.append(max(scores))
		scores.remove(max(scores))
		if(i == 2):
			break
	return maximum
	
