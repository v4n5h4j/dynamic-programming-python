def howSum(targetSum, numbers):
	tab = [None for _ in range(targetSum + 1)]

	tab[0] = []

	for i in range(targetSum+1):
		if tab[i] is not None:
			for num in numbers:
				if (i+num <= targetSum): 
					tab[i+num] = [*tab[i], num]

	return tab[targetSum]

print(howSum(7, [2,3]))
print(howSum(7, [5,3,4,7]))
print(howSum(7, [2,4]))
print(howSum(8, [2,3,5]))
print(howSum(300, [7,14]))