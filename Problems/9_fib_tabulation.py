# Tabulation: a recursion alterantive

def fib(n):
	tab = []

	#seed
	tab.append(0)
	tab.append(1)
	
	for i in range(2,n+1):
		tab.append(tab[i-1] + tab[i-2])
	
	return tab[n]

print(fib(6))
print(fib(7))
print(fib(8))
print(fib(50))