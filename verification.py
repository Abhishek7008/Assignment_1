# -*- coding: utf-8 -*-
"""Verification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_wkqsh79F0fLWnk0MhdOt4IOA6P9vS4N
"""

import numpy as np

A = np.array([[1,1],[-1,1]]) 
B = np.array([12,2])  
P = np.linalg.solve(A, B)

print(P)