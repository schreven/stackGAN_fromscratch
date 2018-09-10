#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 16:09:11 2018

@author: Cyril van Schreven
"""

import glob

def load_text_file(file_path):
    text_file = open(file_path,"r")
    lines = text_file.read().split('\n')[:-1]
    
    
    for i_, line in enumerate(lines):
        line = line.replace("\n","")
        lines[i_] = line
        
    return lines


def load_text_folder(folder_path):
    text_dict = dict()
    list_of_docs = glob.glob(folder_path + '/*')
    for doc_ in list_of_docs:    
        bird_class = doc_.split('/')[-1]
        if (bird_class not in text_dict):
            text_dict[bird_class] = dict()            
    
        list_of_files = glob.glob(doc_ + '/*.txt')
        for file_ in list_of_files:
            bird_id = file_.split('/')[-1]
            if (bird_id not in text_dict[bird_class]):
                text_dict[bird_class][bird_id] = [] 
                
            text_dict[bird_class][bird_id] = load_text_file(file_)
            
    return text_dict

"""
##Example usage of 'import_text_file(file_path)'

file_path = '/home/cyril-kubu/Documents/github_repos/stackGan_fromscratch/Data/birds/text_c10/005.Crested_Auklet/Crested_Auklet_0040_794912.txt'
sentence_list =  load_text_file(file_path)
print(sentence_list)
"""


"""
## Example usage of 'import_text_folder(folder_path)' 
folder_path = '/home/cyril-kubu/Documents/github_repos/stackGan_fromscratch/Data/birds/text_c10'
my_text_dict = load_text_folder(folder_path)
print(my_text_dict['005.Crested_Auklet']['Crested_Auklet_0040_794912.txt'])
""" 
    
    
    

