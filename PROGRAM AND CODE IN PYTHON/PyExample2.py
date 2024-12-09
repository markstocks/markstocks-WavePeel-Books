#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 11:38:03 2024

@author: marks_old
"""
# Example Problem 2: Calculate total pH from 10 water samples
total_ph = 0
for sample in range(10):
    ph_level = float(input(f"Enter pH level for sample {sample + 1}: "))
    total_ph += ph_level

print("Total pH:", total_ph)
