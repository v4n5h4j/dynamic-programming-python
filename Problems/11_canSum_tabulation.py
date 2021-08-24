def canSum(targetSum, numbers):
	tab = [False for _ in range(targetSum+1)]

	# seed
	tab[0] = True

	for i in range(targetSum+1):
		if tab[i] is False:
			continue
		for num in numbers:
			if (i+num <= targetSum): tab[i+num] = True
	
	return tab[targetSum]


print(canSum(7, [2,3]))
print(canSum(7, [5,3,4,7]))
print(canSum(7, [2,4]))
print(canSum(8, [2,3,5]))
print(canSum(300, [7,14]))