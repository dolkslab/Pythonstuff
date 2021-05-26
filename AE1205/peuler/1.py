
num = [3, 5]

allcomb= []
for i in range(1,401):
	for j in num:
		mult = i*j
		try: 
			allcomb.index(mult) 
		except ValueError:
			if mult < 1000:
				allcomb.append(mult)
		else:
			print('already in list')



	
print(allcomb)	
tot_sum=0

for n in allcomb:
	tot_sum += n
	
print(tot_sum)
