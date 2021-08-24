import os, sys, importlib
sys.path.append(os.path.join(os.getcwd(),'Problems'))
"""
Collection of dynamic programming problems from https://youtu.be/oBt53YbR9Kk
"""

index = {"1":'1_nth_fibonacci'\
		,"2":'2_grid_traveler'\
		,"3":'3_can_sum'\
		,"4":'4_how_sum'\
		,"5":'5_best_sum'\
		,"6":'6_can_construct'\
		,"7":'7_count_construct'\
		,"8":'8_all_construct'\
		,"9":'9_fib_tabulation'\
		,"10":'10_grid_tabulation'\
		,"11":'11_canSum_tabulation'\
		,"12":'12_howSum_tabulation'\
		,"13":'13_bestSum_tabulation'\
		,"14":'14_canConstruct_tabulation'\
		,"15":'15_countConstruct_tabulation'\
		,"16":'16_allConstruct_tabulation'}


while True:
	try:
		qName = index[input('Enter question number: ')]
		break
	except KeyError:
		print(">> Enter correct number.\n")
		continue

print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
importlib.import_module(qName)
