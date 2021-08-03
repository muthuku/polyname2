#!/usr/bin/env python
'''a script to check the database if the polymer name and corresponding monomer smile strings exist, 
the remove any duplicate entries and then return the database extract and the ones that still need to be extracted'''

#imports
import pandas as pd
import numpy as np
import itertools
import csv



#script to check database-Inputs :polymers input file and database as input
def check_database(file,database):
	#open the polymer names file and read lines and make a list 
	with open(file) as f:
		content = f.readlines()
	content = [x.strip() for x in content]
	print(content)
	#initialize list of names and smies
	names = []
	smiles = []
	#open database and read it in, check every row and in database and content list and find a match, 
	#if there is then append to lists
	with open(database, 'r') as f:
		csvfile = csv.reader(f, delimiter = ',')
		#loop through every row in database
		for row in csvfile:
			if (set(row) & set(content)):
				names.append(row[0])
				smiles.append(row[2])
	return names,smiles


#script to remove duplicates, Inputs: a list of names and smiles
def remove_duplicates(names,smiles):
	#initialize names and smiles list final
	final_names = []
	final_smiles = []
	#loop through names list, remove duplicates and return
	for name in names:
		if name not in final_names:
			final_names.append(name)
	#loop through smiles list, remove duplicates and return
	for smile in smiles:
		if smile not in final_smiles:
			final_smiles.append(smile)
	return final_names,final_smiles


#outputs names that weren't in database, Inputs: polymer names file and final names found in database
def search_names(file, final_names):
	#open polymer names file and make a list
	with open(file) as f:
		content = f.readlines()
	content = [x.strip() for x in content]
	search_names = []
	#loop through list and see if it was in database names, returns names to search
	for item in content:
		if item not in search_names:
			item.replace("P","p")
			search_names.append(item)
	return search_names

#example to run the script
'''files_path = '/Users/pmuthuku/Documents/python_scripts_suli/workingscripts/polyname_scripts/polymername_final.txt'
data_base = "polyname_smiles_test.csv"

name,smile = check_database(files_path,data_base)

final_name,final_smile = remove_duplicates(name,smile)

search_name = search_names(files_path,final_name)



df = pd.DataFrame(final_name, columns = ["Polymer Names"])
df.insert(1,'Monomer Smiles', final_smile)
df.to_csv('database_extract.csv', index = None)

df2 = pd.DataFrame(search_name, columns = ["polymernames"])
df2.to_csv('polymer_extract_still.csv', index = None)'''