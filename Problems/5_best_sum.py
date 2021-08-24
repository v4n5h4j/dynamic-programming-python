def bestSum(t, arr, memo=None):
	"""
	m: target sum, t
	n: len(arr)
	time = O(n^m*m)
	space = O(m*m) [in each stack frame, I am storing an array, which in worst case would be m]

	// Memoized complexity
	time = O(n*m*m)
	space = O(m*m)
	"""
	if memo is None:
		memo = {}

	if t in memo:
		return memo[t]

	if t == 0:
		return []
	if t < 0:
		return None

	shortestCombination = None
	for ele in arr:
		r = t - ele
		rRes = bestSum(r, arr, memo)
		if rRes is not None:
			combination = rRes + [ele]
			# If the combination is shorter than current shortest, update it
			if (shortestCombination is None or len(combination) < len(shortestCombination)):
				shortestCombination = combination

	memo[t] = shortestCombination
	return memo[t]


print(bestSum(7, [5,3,4,7]))
print(bestSum(8, [2,3,5]))
print(bestSum(8, [1,4,5]))
print(bestSum(100, [1,2,5,25]))