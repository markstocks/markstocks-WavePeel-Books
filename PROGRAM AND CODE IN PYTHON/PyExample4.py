#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 11:45:02 2024

@author: marks_old
"""
# Example Problem 4: Print fossil records only
dataset = [
            ('F', 'Sample 1'), 
            ('R', 'Sample 2'), 
            ('F', 'Sample 3'), 
            ('R', 'Sample 4')
          ]                     # Example dataset

for record in dataset:
    sample_code, sample_name = record
    if sample_code == 'F':
        print("Fossil record:", sample_name)