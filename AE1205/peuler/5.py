exit = False
n=1999
while exit == False:
	n += 1
	for i in range(2, 21):
		if n % i != 0:
			break
	else:
		exit=True

print(n)
