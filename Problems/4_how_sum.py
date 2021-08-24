def howSum(t, arr, memo=None):
	'''
	- Returns an array containing any combination of elements that adds up to t (targetSum).
	- If there is no combination that adds up to t, then return None.
	- If there are multiple combinations, return any single one.
	'''
	if memo is None:
		memo = {}

	if t in memo:
		return memo[t]
	if t == 0:
		return []
	if t < 0:
		return None
	
	for ele in arr:
		r = t - ele
		rRes = howSum(r, arr, memo)
		if rRes is not None:
			memo[t] = rRes+[ele]
			return memo[t]
	
	memo[t] = None
	return None


print(howSum(7, [2,3]))
print(howSum(7, [5,3,4,7]))
print(howSum(7, [2,4]))
print(howSum(8, [2,3,5]))
print(howSum(300, [7,14]))
