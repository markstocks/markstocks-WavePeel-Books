#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 12:07:44 2024

@author: marks_old
"""
# Example Problem 8: Calculate biomass based on growth stage multiplier
dataset = [
    ('Sample 1', 100, 'S'),
    ('Sample 2', 150, 'M'),
    ('Sample 3', 200, 'L'),
    ('Sample 4', 120, 'M')
]

for record in dataset:
    sample_id, mass, growth_stage = record
    if growth_stage == 'S':
        biomass = mass * 0.05
    elif growth_stage == 'M':
        biomass = mass * 0.07
    elif growth_stage == 'L':
        biomass = mass * 0.10
    
    print(f"Sample ID: {sample_id}, Mass: {mass}, Estimated Biomass: {biomass}")
