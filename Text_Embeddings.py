#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 16:00:06 2018

@author: root
"""


import glob
import torch

def load_text_file(file_path):
    text_file = open(file_path,"r")
    lines = text_file.read().split('\n')[:-1]
    
    
    for i_, line in enumerate(lines):
        line = line.replace("\n","")
        lines[i_] = line
        
    return lines


"""
##Example usage of 'import_text_file(file_path)'

file_path = '/home/cyril-kubu/Documents/github_repos/stackGan_fromscratch/Data/birds/text_c10/005.Crested_Auklet/Crested_Auklet_0040_794912.txt'
sentence_list =  load_text_file(file_path)
print(sentence_list)
"""



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
## Example usage of 'import_text_folder(folder_path)' 
folder_path = '/home/cyril-kubu/Documents/github_repos/stackGan_fromscratch/Data/birds/text_c10'
my_text_dict = load_text_folder(folder_path)
print(my_text_dict['005.Crested_Auklet']['Crested_Auklet_0040_794912.txt'])
""" 
    


def text_to_vect_files(text_dict, encoder, class_nbs='default',embedding_path='./Data/embeddings'):
    embedding_path = './Data/birds/generated_text_embeddings/'
    print('Generated embeddings will be saved to: '+ embedding_path)
    if class_nbs == 'default':
        class_nbs = len(text_dict.keys())
    for i_, bird_class in enumerate(text_dict.keys()[:class_nbs]):
        print("# Vectorizing bird class: {}, which is nb: {}/{} #".format(bird_class, str(i_+1), len(text_dict.keys()[:class_nbs])))
        for bird_id in text_dict[bird_class].keys():
            x_temp = torch.Tensor(encoder.encode(text_dict[bird_class][bird_id],verbose = False))
            x_array = torch.mean(x_temp, dim = 0)
            torch.save(x_temp,embedding_path+bird_class+'-'+bird_id+'.pt')
    return

"""
## Example usage of 'text_to_vect_files(text_dict, encoder, class_nbs='default',embedding_path='./Data/embeddings')'
embd_path = './Data/birds/generated_text_embeddings/'
text_to_vect_files(my_text_dict,encoder,class_nbs = 2, embedding_path = embd_path)
my_test_embedding = torch.load(embd_path+'038.Great_Crested_Flycatcher-Great_Crested_Flycatcher_0125_29593.txt.pt')
print(my_test_embedding)
"""