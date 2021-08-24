def canConstruct(target, word_bank, memo=None):
	'''
	input: target- String
		   word_bank- array of Strings
	output: bool indicating whether the target can be generated from the 
			strings present in word_bank or not. Repetition is always allowed unless stated otherwise.
	'''
	if memo is None:
		memo = {}
	if target in memo:
		return memo[target]
	if target == '':
		return True
	
	for word in word_bank:
		if target.startswith(word):
			suffix = target[len(word):]
			if canConstruct(suffix, word_bank, memo):
				memo[target] = True
				return True

	memo[target] = False
	return False


print(canConstruct("abcdef", ["ab","abc","cd","def","abcd"]))
print(canConstruct("skateboard", ["bo","rd","ate","t","ska","sk","boar"]))
print(canConstruct("enterapotentpot",["a","p","ent","enter","ot","o","t"]))
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeef",[
	"e",
	"ee",
	"eee",
	"eeee",
	"eeeee",
	"eeeeee"]))
