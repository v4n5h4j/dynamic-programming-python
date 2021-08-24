def canSum(t, arr, memo=None):
	'''
	input: target- t
		   arr- array of numbers
	output: bool indicating whether it's possible to generate t by adding 
	 		numbers in arr
	'''
	if memo is None:
		memo = {}

	if (t in memo):
		return memo[t]
	if t == 0:
		return True
	if t < 0:
		return False

	for ele in arr:
		if canSum(t-ele,arr,memo) is True:
			memo[t] = True
			return True
		
	memo[t] = False
	return False


print(canSum(7, [2,3]))
print(canSum(7, [5,3,4,7]))
print(canSum(7, [2,4]))
print(canSum(7, [2,3,5]))
print(canSum(300, [7,14]))