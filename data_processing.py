#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 18:12:59 2018

@author: Cyril van Schreven
"""

def textdict_to_vect(text_dict, encoder):
    textvect_dict = dict()
    for i_, bird_class in enumerate(text_dict.keys()):
        print("####Vectorizing bird class: " + bird_class + ", which is nb: " + str(i_) + " ####")
        if (bird_class not in textvect_dict):
            textvect_dict[bird_class] = dict()
        for bird_id in text_dict[bird_class].keys():
            textvect_dict[bird_class][bird_id] = encoder.encode(text_dict[bird_class][bird_id])
    return textvect_dict