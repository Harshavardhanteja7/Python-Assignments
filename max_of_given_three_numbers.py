# -*- coding: utf-8 -*-
"""max_of_given_three_numbers.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ilFNpKxRFDl1-okK3UWBjP9-6tc1Y0iM

# New Section
"""

a=int(input("enter num1:"))
    b=int(input("enter num2:"))
    c=int(input("enter num3:"))
    if a==b==c:
        print("all are equal..no maximum number")
    elif (a>b and a>c):
        print("maximum number is:",a)
    elif (b>c and b>a):
        print("maximum number is:",b)
    else:
        print("maximum number is:",c)
max()

