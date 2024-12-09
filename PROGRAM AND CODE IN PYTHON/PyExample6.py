#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 11:51:03 2024

@author: marks_old
"""
# Example Problem 6: Count fossils meeting criteria and
# And print fossils meeting criteria and total fossil records
# Note: record 'R' is not a fossile record so it is not included in any Count
dataset = [
    ('F', 150_000_000, 'Location A', 3.5),
    ('R', 200_000_000, 'Location B', 1.0),
    ('F', 50_000_000, 'Location C', 2.1),
    ('F', 120_000_000, 'Location D', 2.5)
]

selected_count = 0
fossil_count = 0

for record in dataset:
    sample_code, age, location, size = record
    if sample_code == 'F':
        fossil_count += 1
        if age > 100_000_000 and size > 2:
            print(f"Fossil - Age: {age} years, Location: {location}, Size: {size} cm")
            selected_count += 1

print(f"Number of selected fossils: {selected_count}")
print(f"Total number of fossils: {fossil_count}")
