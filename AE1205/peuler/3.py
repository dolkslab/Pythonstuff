n = 600851475143

primes = [2]
for i in range(3, 100000):
	for j in range(2, i-1):
		if i % j == 0:
			break
	else:
		primes.append(i)
		if n % i == 0:

print(primes)


for i in primes:
	if n % i == 0:
		max_fact=i

print(max_fact)
