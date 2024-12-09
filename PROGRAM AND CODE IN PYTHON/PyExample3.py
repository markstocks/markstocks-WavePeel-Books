#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 11:41:26 2024

@author: marks_old
"""
# Example Problem 3: Read experimental readings and calculate the cumulative total until outlier -999
total_readings = 0
reading = float(input("Enter experimental reading (-999 to stop): "))

while reading != -999:
    print("Reading:", reading)
    total_readings += reading
    reading = float(input("Enter experimental reading (-999 to stop): "))

print("Total of valid readings:", total_readings)
