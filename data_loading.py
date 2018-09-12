#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 16:09:11 2018

@author: Cyril van Schreven
"""
from PIL import Image
import PIL.Image.Bilinear

import torch
from torch.utils import data
from torchvision import transforms

class Dataset(data.Dataset):
  'Characterizes a dataset for PyTorch'
  def __init__(self, image_path, image_list_IDs, text_embedding_path, text_list_IDs):
        'Initialization'
        
        self.image_path = image_path
        self.image_list_IDs = image_list_IDs
        
        self.text_embedding_path = text_embedding_path
        self.text_list_IDs = text_list_IDs
        
        
        
  def __len__(self):
        'Denotes the total number of samples'
        return len(self.text_list_IDs)

  def __getitem__(self, index):
        'Generates one sample of data'
        # Select sample
        ID_image = self.image_list_IDs[index]
        
        ID_embedding = self.text_list_IDs[index]

        # Load data and get label
        
        img = Image.open(ID_image).convert('RGB')
        img = img.resize((64, 64), PIL.Image.BILINEAR)
        trans_to_tensor = transforms.ToTensor()
        img = trans_to_tensor(img)
        
        
        embedding = torch.load(ID_embedding)
        embedding
        
        #y = self.labels[ID]

        return img, embedding
