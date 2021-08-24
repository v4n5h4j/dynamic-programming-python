# grid traveller using tabulation; I may need to use numpy...nah I'll use for loops ;)

def createGridTable(m, n):
	tab = []
	for i in range(m+1):
		tab.append([])
		for j in range(n+1):
			tab[i].append(0)
	
	return tab

def gridTraveler(m, n):
	tab = createGridTable(m, n)
	# pprint(tab, width = m+6)
	
	# seed
	tab[1][1] = 1

	# add the current value to right and down element
	for i in range(m+1):
		for j in range(n+1):
			if (j+1 <= n): tab[i][j+1] += tab[i][j]
			if (i+1 <= m): tab[i+1][j] += tab[i][j]

	return tab[m][n]


print(gridTraveler(1,1))
print(gridTraveler(2,3))
print(gridTraveler(3,2))
print(gridTraveler(3,3))
print(gridTraveler(18,18))
