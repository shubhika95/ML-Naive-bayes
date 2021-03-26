#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 09:14:36 2021
This script merges all the reviews from the IMDB dataset in a large tsv file named 'imdb_all.csv' with the following columns:
- review (converting to lower case, removing punctuation and replacing special characters and tags for spaces by spaces)
- dataset (train or test)
- sentiment (pos or neg)
- rating (1 to 4 = neg and 7 to 10 = pos)
The current directory is the 'aclimdb' directory after unzipping of the tar.gz file. For convenience, .txt files contained in the folders but not used (like url_neg.txt) were deleted before running the script.
@author: PaulineRiviere
"""

#%%
import os
import re

#%%

MasterList = []
Punctuation_discarded = re.compile("[.;:!\'?,\"()\[\]]")
Spaces_replaced = re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)")

for Root, Dirs, Files in os.walk("."):
    for FileName in Files:
        if FileName.endswith(".txt"):
            Filepath = os.path.join(Root, FileName)
            InFile = open(Filepath, 'r')
            for Line in InFile:
                Line = Line.strip('\n').strip('\r').lower()
                Line = Punctuation_discarded.sub("", Line)
                Line = Spaces_replaced.sub(" ", Line)
            OriginList = Root.split('/')
            Rating = re.split('[_.]',FileName)
            MasterList.append(Line + ';' + OriginList[1] + ';' + OriginList[2] + ';' + Rating[1]) 
            InFile.close()

#%%
OutFileName = 'imdb_all.csv'
OutFile = open(OutFileName, 'w')

Header = ['review', 'dataset', 'label', 'rating']
OutFile.write(';'.join(Header) + '\n')

for Item in MasterList:
    OutFile.write(str(Item) + '\n')
    
OutFile.close()

