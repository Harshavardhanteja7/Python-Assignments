# -*- coding: utf-8 -*-
"""any_two_of_them_should_be_equal.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NdskDQEnLhitrMeG62_BqTFoaRtW55T7
"""

print("Enter any Two (or) Three numbers identical...")
value_1=input()
value_2=input()
value_3=input()
if ((value_1==value_2) or (value_1==value_3)) and (value_2!=value_3):
  print("Entered two of them are Equal")
elif ((value_2==value_3) or (value_2==value_1)) and (value_3!=value_1):
  print("Entered two of them are Equal")  
elif ((value_3==value_1) or (value_3==value_2)) and (value_2!=value_1):
  print("Entered two of them are Equal")    
elif (value_1==value_2) and (value_2==value_3) and (value_3==value_1):
  print("All entered numbers are equal..")
else: 
  print("Entered numbers are not equal, please enter like any two of them should be equal ")