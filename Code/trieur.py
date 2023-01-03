#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 09:19:28 2022
 string.digits and mot[i] not in string.ascii_lowercase and mot[i] not in string.ascii_uppercase
@author: k22005807
"""

import string
def clean(carac):
    cleaned = []
    interdit = []
    passable = ["é","à","'","_","è", '"']
    for k in carac:
        for lettre in k :       
            if lettre not in string.digits and lettre not in string.ascii_lowercase and lettre not in string.ascii_uppercase and lettre not in passable and lettre not in interdit:
                interdit.append(lettre)
        for i in interdit :
            if i in k :
                k = k.replace(i," ")
        if k not in cleaned:
            cleaned.append(k)
    return cleaned
                
        
        
    
   
    

               
    


            
    
