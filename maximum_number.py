# -*- coding: utf-8 -*-
"""maximum_number.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ilFNpKxRFDl1-okK3UWBjP9-6tc1Y0iM

# New Section
"""

a=int(input("enter first number:"))
    b=int(input("enter second number:"))
    c=int(input("enter third number:"))
    if a==b==c:
        print("all are equal... no maximum number")
    if(a>b and a>c):
        print("maximum number is",a)
    elif(b>c and b>a):
        print("maximum number is",b)
    else:
        print("maximum number is",c)