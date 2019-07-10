#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
def assignchp(u, path, path_len, Sum, k): 
	global chp, days, NOLINK, d_path, Directed_Acyclic_Graph, Min


	if (k < 0): 
		return

	path[path_len] = u 
	path_len += 1


	if (k == 0 and u == chp): 
		if (Sum < Min): 
			getpath(path, path_len) 
			Min = Sum

	# DFS - Depth First Search for sink 
	for v in range(u + 1, chp + 1): 
		Sum += Directed_Acyclic_Graph[u][v] 
		assignchp(v, path, path_len, Sum, k - 1) 
		Sum -= Directed_Acyclic_Graph[u][v] 


def find_min(pages): 
	global chp, days, NOLINK, d_path, Directed_Acyclic_Graph, MIN
	

	avg_pages = 0
	Sum = 0
	S = [None] * (chp + 1) 
	path = [None] * (days + 1) 
	S[0] = 0

	for i in range(chp): 
		Sum += pages[i] 
		S[i + 1] = Sum

	avg_pages = math.ceil(Sum/days) 


	for i in range(chp + 1): 
		for j in range(chp + 1): 
			if (j <= i): 
				Directed_Acyclic_Graph[i][j] = NOLINK 
			else: 
				Sum = abs(avg_pages - (S[j] - S[i])) 
				Directed_Acyclic_Graph[i][j] = Sum


	assignchp(0, path, 0, 0, days) 


	print("Optimal Chapter Assignment :") 
	ch = None
	for i in range(days): 
		ch = optimal_path[i] 
		print("Day", i + 1, ": ", ch, end = " ") 
		ch += 1
		while ((i < days - 1 and ch < optimal_path[i + 1]) or
			(i == days - 1 and ch <= chp)): 
			print(ch, end = " ") 
			ch += 1
		print() 

def getpath(path, path_len): 
	for i in range(path_len): 
		optimal_path[i] = path[i] + 1

if __name__ == "__main__":
    chp = int(input("Enter Chapter Numbers: "))
    days = int(input("Enter Reading book days: "))
    NOLINK = -1
    optimal_path = [None] * (days + 1) 
    Directed_Acyclic_Graph = [[None] * (chp + 1) 
    	for i in range(chp + 1)] 
    Min = 999999999999
    pages = [int(x) for x in input("Enter pages space separated: ").split()]
    find_min(pages) 
