def bestSum(targetSum, numbers):
	tab = [None for _ in range(targetSum + 1)]

	tab[0] = []

	for i in range(targetSum+1):
		if tab[i] is not None:
			for num in numbers:
				if (i+num <= targetSum): 
					if tab[i+num] is None:
						tab[i+num] = [*tab[i], num]
					else:
						temp = [*tab[i], num]
						if len(temp) < len(tab[i+num]):
							tab[i+num] = temp
		
	
	return tab[targetSum]


print(bestSum(7, [5,3,4,7]))
print(bestSum(8, [2,3,5]))
print(bestSum(8, [1,4,5]))
print(bestSum(100, [1,2,5,25]))
