# -*- coding: utf-8 -*-
"""area_of_regular_polygon.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ilFNpKxRFDl1-okK3UWBjP9-6tc1Y0iM

# New Section
"""

import math
n=float(input("Number of sides:"))
s=float(input("length of a side:"))
p=n*(s**2/(4*math.tan(math.pi/n)))
print("the area of polygon is:",p)

