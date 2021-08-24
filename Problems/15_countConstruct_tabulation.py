def countConstruct(target, word_bank):
	tab = [0 for _ in range(len(target)+1)]

	# seed - there's only 1 way to construct an empty string
	tab[0] = 1

	for i in range(len(target)+1):
		if tab[i] != 0:
			for word in word_bank:
				if target[i:].startswith(word):
					tab[i+len(word)] += tab[i]
		
	return tab[-1]


print(countConstruct("purple",["purp","p","ur","le","purpl"]))
print(countConstruct("abcdef", ["ab","abc","cd","def","abcd"]))
print(countConstruct("skateboard", ["bo","rd","ate","t","ska","sk","boar"]))
print(countConstruct("enterapotentpot",["a","p","ent","enter","ot","o","t"]))
print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeef",[
	"e",
	"ee",
	"eee",
	"eeee",
	"eeeee",
	"eeeeee"]))
	