import pprint as pp

def allConstruct(target, word_bank, memo=None):
	'''
	input: target- String
		   word_bank- array of Strings
	output: 2D array containing all of the ways that the target can be 
			constructed by concatenating elements of the word_bank array. Each element of the 2D array should represent one combination that constructs the target
	'''
	if memo is None:
		memo = {}
	if target in memo:
		return memo[target]
	if target == '':
		return [[]]
	result = []
	for word in word_bank:
		if target.startswith(word):
			suffix = target[len(word):]
			suffix_ways = allConstruct(suffix, word_bank)
			target_ways = list(map(lambda way: [word, *way], suffix_ways))
			result.extend(target_ways)

	memo[target] = result
	return result


pp.pprint(allConstruct("purple",["purp","p","ur","le","purpl"]))
pp.pprint(allConstruct("abcdef", ["ab","abc","cd","def","abcd","ef","c"]))
pp.pprint(allConstruct("skateboard", ["bo","rd","ate","t","ska","sk","boar"]))
pp.pprint(allConstruct("aaaaaaaaaaaaaaaaaaz",["a","aa",'aaa','aaaa','aaaaa']))



