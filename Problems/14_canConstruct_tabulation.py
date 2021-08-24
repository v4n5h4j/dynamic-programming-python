def canConstruct(target, word_bank):
	tab = [False for _ in range(len(target)+1)]
	
	# seed
	tab[0] = True # creating an empty string is always possible

	for i in range(len(target)+1):
		if tab[i] is True:
			for word in word_bank:
				# If the word matches the characters starting at position i
				if target[i:].startswith(word):
					tab[i+len(word)] = True
	
	return tab[-1]

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


