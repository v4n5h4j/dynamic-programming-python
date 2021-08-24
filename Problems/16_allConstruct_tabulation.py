import pprint as pp

def allConstruct(target, word_bank):
	tab = [[] for _ in range(len(target)+1)]

	# seed
	tab[0] = [[]]

	for i in range(len(target)+1):
		if tab[i] != []:
			for word in word_bank:
				if target[i:].startswith(word):
					target_ways = list(map(lambda way: [*way, word], tab[i]))
					tab[i+len(word)].extend(target_ways)
	
	return tab[-1]


pp.pprint(allConstruct("abcdef", ["ab","abc","cd","def","abcd","ef","c"]))
