def countConstruct(target, word_bank, memo = None):
	'''
	input: target- String
		   word_bank- array of Strings
	output: number of ways that the target can be constructed by 
			concatenating elements fo the word_bank array.
	'''

	if memo is None:
		memo = {}
	
	if target in memo:
		return memo[target]

	if target == '':
		return 1

	totalCount = 0

	for word in word_bank:
		if target.startswith(word):
			suffix = target[len(word):]
			numWaysForRest = countConstruct(suffix, word_bank, memo)
			totalCount += numWaysForRest
	
	memo[target] = totalCount
	return totalCount


print(countConstruct("abcdef", ["ab","abc","cd","def","abcd"]))
print(countConstruct("purple",["purp","p","ur","le","purpl"]))
print(countConstruct("skateboard", ["bo","rd","ate","t","ska","sk","boar"]))
print(countConstruct("enterapotentpot",["a","p","ent","enter","ot","o","t"]))
print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeef",[
	"e",
	"ee",
	"eee",
	"eeee",
	"eeeee",
	"eeeeee"]))