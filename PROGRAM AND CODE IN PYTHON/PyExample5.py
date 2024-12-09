#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 11:48:30 2024

@author: marks_old
"""
# Example Problem 5: Print fossil samples over 100 million years old and larger than 2 cm
dataset = [
            ('F', 150_000_000, 'Location A', 3.5),
            ('R', 200_000_000, 'Location B', 1.0),
            ('F', 50_000_000, 'Location C', 2.1),
            ('F', 120_000_000, 'Location D', 2.5)
          ]

for record in dataset:
    sample_code, age, location, size = record
    if sample_code == 'F' and age > 100_000_000 and size > 2:
        print(f"Fossil - Age: {age} years, Location: {location}, Size: {size} cm")
