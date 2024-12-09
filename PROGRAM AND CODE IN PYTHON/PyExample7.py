#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 11:59:59 2024

@author: marks_old
"""
# Example Problem 7: Count each type of sample and calculate total weight
dataset = [
    (1, 'Sample 1', 10.5),
    (2, 'Sample 2', 5.3),
    (3, 'Sample 3', 8.2),
    (4, 'Sample 4', 7.0),
    (3, 'Sample 5', 9.1),
    (1, 'Sample 6', 12.0)
]

sediment_count, sediment_weight = 0, 0
mineral_count, mineral_weight = 0, 0
fossil_count, fossil_weight = 0, 0
artifact_count, artifact_weight = 0, 0
other_count = 0

for record in dataset:
    record_code, sample_id, weight = record
    if record_code == 1:
        sediment_count += 1
        sediment_weight += weight
    elif record_code == 2:
        mineral_count += 1
        mineral_weight += weight
    elif record_code == 3:
        fossil_count += 1
        fossil_weight += weight
    elif record_code == 4:
        artifact_count += 1
        artifact_weight += weight
    else:
        other_count += 1

print(f"Sediments: {sediment_count}, Total weight: {sediment_weight}")
print(f"Minerals: {mineral_count}, Total weight: {mineral_weight}")
print(f"Fossils: {fossil_count}, Total weight: {fossil_weight}")
print(f"Artifacts: {artifact_count}, Total weight: {artifact_weight}")
print(f"Other records: {other_count}")

