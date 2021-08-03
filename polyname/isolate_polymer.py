#!/usr/bin/env python
'''Isolate all polymer names from all chemical entities and use language rules to capitalize,
remove whitespace and output a textfile with cleaned up polynames'''
#import pandas, numby, itertools and csv
import pandas as pd
import numpy as np
import itertools
import csv

#function polymer_extract, Input:file with all chemical names 
def polymer_extract(file):
	#read file into data frame
	df = pd.read_table(file)
	#isolate names that contain poly or Poly, case sensitive
	df2 = df[df["All_names"].str.contains("poly")]
	df3 = df[df["All_names"].str.contains("Poly")]
	#concacenate them together
	result = pd.concat([df2,df3])
	#turn it into a list called df4
	df4 = result["All_names"].to_list()
	#df4 = result.loc[result["All_names"].str[0].isin(['p']),'All_names'].tolist()
	#initialize new list
	new_list = []
	#loop through df4 list with all polymer names
	for name in df4:
		#if it starts with poly, capitalize 1st letter, add paraentehsis, strip whitespace etc. and return new list
		if name.startswith('poly') or name.startswith('Poly'):
			cap = name[:1].upper() + name[1:]
			string = cap.replace("(", "")
			string1 = string.replace(")","")
			string2 = string1.strip()
			string3 = string2[:4] + "(" + string2[4:]
			string4 = string3.rstrip("s")
			final_name = string4 + ")"
			new_list.append(final_name)
	return new_list
#using function, have a file name, run function polymer_extract which returns a list
'''files_path = '/Users/pmuthuku/Documents/python_scripts_suli/workingscripts/polyname_scripts/all_names.txt'
polymer_list = polymer_extract(files_path)


#turn list into dataframe
data = pd.DataFrame (polymer_list, columns = ['Isolated_poly_names'])
print(data)

data1 = data[data["Isolated_poly_names"].str.startswith("Poly")]
print(data1)
#output list to a textfile
data1.to_csv("polymername_final.txt", index = False)'''