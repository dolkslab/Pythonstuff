
def iseven(num):
	if num % 2 ==0:
		return True
	else:
		return False
		
print(iseven(1))

fib=[1,2]
i = 0
while i <= 4000000:
	i = fib[-1]+fib[-2]
	fib.append(i)
	i = fib[-1]+fib[-2]
sum_tot=0

for j in fib:
	if iseven(j):
		sum_tot+=j

print(sum_tot)
