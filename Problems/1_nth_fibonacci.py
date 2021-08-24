def fib(n, memo = None):
	'''
	input: integer n
	output: nth term of fibonacci sequence (1,1,2,3,5...)
	'''
	if memo is None:
		memo = {}

	# base conditions
	if (n<=2):
		return 1

	# memoization and recursion
	if n in memo:
		return memo[n]
	else:
		memo[n] = fib(n-1,memo) + fib(n-2,memo)
		return memo[n]


print(fib(6))
print(fib(7))
print(fib(8))
print(fib(50))
