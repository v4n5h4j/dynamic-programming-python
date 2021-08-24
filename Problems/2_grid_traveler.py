import math
"""
There are 2 ways to solve this problem. 
1. Simply count the number of arrangements of rightward and downward steps. O(1) time complexity, O(1) space complexity.
2. Use dynamic programming approach. O(n) time complexity (after memoization, it was O(2^n) before memoization), O(r+c) = O(max(r,c)) space complexity.
"""

def gridTraveler(r,c):
	return math.factorial(r+c-2)/math.factorial(r-1)/math.factorial(c-1)

def gridTraveler2(r,c,memo={}):
	'''
	input: integer r - number of rows
		   integer c - number of columns
	output: number of ways to travel r*c grid by going only down or right 
	'''
	# base conditions
	if r == 1 and c == 1:
		return 1
	if r == 0 or c == 0: # grid is empty
		return 0

	# recursion & memoization
	if (r,c) in memo:
		return memo[(r,c)]
	elif (c,r) in memo:
		return memo[(c,r)]
	else:
		memo[(r,c)] = gridTraveler2(r-1,c,memo) + gridTraveler2(r,c-1,memo)
	return memo[(r,c)]


print(gridTraveler2(1,1))
print(gridTraveler2(2,3))
print(gridTraveler2(3,2))
print(gridTraveler2(3,3))
print(gridTraveler2(18,18))