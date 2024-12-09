#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 16:39:52 2024

@author: marks_old
"""
# Example Problem 1: Compare and print temperatures in ascending order
temperature1 = float(input("Enter temperature from sensor 1: "))
temperature2 = float(input("Enter temperature from sensor 2: "))

if temperature1 < temperature2:
    print(temperature1, temperature2)
else:
    print(temperature2, temperature1)
