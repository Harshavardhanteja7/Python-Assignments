# -*- coding: utf-8 -*-
"""two lists.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ilFNpKxRFDl1-okK3UWBjP9-6tc1Y0iM

# New Section
"""

list1=[1,3,5,7,9]
list2=[1,2,4,6,7,8]
diff_list1_list2=list(set(list1)-set(list2))
diff_list2_list1=list(set(list2)-set(list1))
total_diff=diff_list1_list2+diff_list2_list1
print(total_diff)

