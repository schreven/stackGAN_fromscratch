#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 18:12:59 2018

@author: Cyril van Schreven
"""

def textdict_to_vect(text_dict, encoder, class_nbs='default'):
    textvect_dict = dict()
    if class_nbs == 'default':
        class_nbs = len(textvect_dict.keys())
    for i_, bird_class in enumerate(text_dict.keys()[:class_nbs]):
        print("#### Vectorizing bird class: {}, which is nb: {}/{} ####".format(bird_class, str(i_+1), len(text_dict.keys()[:class_nbs])))
        if (bird_class not in textvect_dict):
            textvect_dict[bird_class] = dict()
        for bird_id in text_dict[bird_class].keys():
            textvect_dict[bird_class][bird_id] = encoder.encode(text_dict[bird_class][bird_id],verbose = False)
    return textvect_dict