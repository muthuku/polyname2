#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import itertools
import pubchempy as pcp
import cirpy



'''data = pd.read_csv('210512_search_criteria_processed_html6423f3912605d57a99a1bf597fc3dc0fcfd3d387f812b76972b6788961f39554.csv',index_col=0)
print(data)
data2 = pd.read_table('polymer_extract_still.csv')
print(data2)
dfnames = pd.DataFrame(data.polymername.unique(),columns=['polyname'])
dfnames2 = pd.DataFrame(data2.polymername.unique(),columns=['polyname'])

print(dfnames)
print(dfnames2)'''

import pubchempy as pcp
import cirpy
def strip_poly(row,stripstrings):
    s = row.polyname
    new_list = []
    for stripstring in stripstrings:
        lstart = len(stripstring[0])
        lend = len(stripstring[1])
        if s[:lstart]==stripstring[0]:
            sreturn = s.replace(stripstring[0],'')
            if lend!=0:
                sreturn = sreturn[:-lend]
            row.polymername = sreturn
        else:pass
        if "-alt-" in row.polymername:
            row.polymername = row.polymername.split('-alt-')
        if "-co-" in row.polymername:
            row.polymername = row.polymername.split('-co-')
    if isinstance(row.polymername,list):
        return row.polymername
    else:
        return [row.polymername]
# Strip polymer nomenclature
stripstrings = [
               ['poly(',')'],
               ['poly[(',')]'],
               ['poly[',']'],
               ['poly{','}'],
               ['poly-','']
               ]

def get_pubchem_smiles(monomer_name):
    smile_list = []
    for name in monomer_name:
        mname = name.replace("(", "")
        mname = mname.replace(")", "")
        result = pcp.get_compounds(mname, 'name')
        if result == []:
            smile_list.append("None")
        else:
            smile = result[0].isomeric_smiles
            smile_list.append(smile)
    return smile_list

def get_cirpy_smiles(monomer_name):
    cirpy_smiles = []
    for name in monomer_name:
        mname = name.replace("(", "")
        mname = mname.replace(")", "")
        smiles = cirpy.resolve(mname, 'smiles')
        if smiles is None:
            cirpy_smiles.append("None")
        else:
            cirpy_smiles.append(smiles)
    return cirpy_smiles

'''#dfnames['polyname_1'] = dfnames.apply(lambda row: strip_poly(row,stripstrings),axis=1)
#dfnames2['polyname_1'] = dfnames2.apply(lambda row: strip_poly(row,stripstrings),axis=1)
monomer_names1 = dfnames.apply(lambda row: strip_poly(row,stripstrings),axis=1)
dfnames['polyname_1'] = monomer_names1
print(dfnames)

monomer_names2 = dfnames2.apply(lambda row: strip_poly(row,stripstrings),axis=1)
dfnames2['polyname_1'] = monomer_names2
print(dfnames2)
dfnames2['Pubchem Smiles'] = monomer_names2.apply(lambda row: get_pubchem_smiles(row))
dfnames2['Cirpy Smiles'] = monomer_names2.apply(lambda row: get_cirpy_smiles(row))
dfnames2.to_csv("example_extract_monomers.csv", index = False)
#print(dfnames)
#smile_strings = get_smiles(tmp)
#dfnames['Smile strings'] = smile_strings
#print("XYZ")
#print(tmp)



# Deal with Alts
df = dfnames[dfnames.polyname_1.str.contains('-alt-')]
print(df)

row = df.iloc[0]

namelist = []
for polyname in df.polyname_1:
    namelist.append(polyname.split('-alt-'))
dsnames = pd.Series(list(itertools.chain(*namelist)))
print(dsnames)




dsnames.shape


dsnames.unique()





