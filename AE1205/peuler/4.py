start=997


def make_palindrome(num):
	num_str = str(num)
	num_str += num_str[::-1]
	return int(num_str)

n_max=0
j_max=0
for i in range(start, 99, -1):
	n = make_palindrome(i)
	for j in range(100, 1000):
		if n % j == 0:
			if (n/j) < 1000:
				n_max = max(n, n_max)
				j_max = j
print(n_max)

