import random as rand
def coffey():
	random_day = rand.randint(1,5)
	random_per = rand.randint(1,8)
	if random_day == 3:
		random_per_choice = [1,2,3,5,7,8]    
		random_per = random.choice(random_per_choice)
	if random_day == 4:
		random_per_choice = [2,3,4,6,7,8]
		random_per = random.choice(random_per_choice)
	if random_day == 5:
		random_per_choice = [1,3,4,5,6,7]
		random_per = random.choice(random_per_choice)
	print("The day is", random_day)
	print("It is period", random_per)
	if random_day == 2:
		return("I'm Happy")
	else:
		if random_per == 7:     
			return("I'm not happy")
		if random_per == 5:
			return("I'm extremely happy")
	else:
		return("I'm Happy")
    print(coffey())
