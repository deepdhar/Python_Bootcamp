# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 18:32:51 2020

@author: Deep Dhar
"""
#uncomment every block of code before running them in IDE
# double-# before any line is comment




## logical operator (and, or, not)

# physics=90+ and chemistry=90+  GRADE A
# physics=90+ and chemistry=70   GRADE B
# physics=50 and chemistry=40    GRADE C

#phy,chem = map(int, input().split(" "))
#
#if phy>=90 and chem>=90:
#    print("GRADE A")
#elif phy>=90 or chem>=90:
#    print("GRADE B")
#else:
#    print("GRADE C")






##loops (for and while)

#n = 10
#for i in range(1,n+1):
#    print(i, end=" ")



##breaks when it encounters 6
#i = 1
#while i<=6:
#    print(i)
#    i = i+1











##1 
##1 2 
##1 2 3 
##1 2 3 4 
##1 2 3 4 5 
#
#n = 10
#
#for i in range(1, n+1):
#    for j in range(1, i+1):
#        print(j, end=" ")
#    print()








#* 
#* * 
#* * * 
#* * * * 
#* * * * * 

n = 5

for i in range (1,5+1):
    for j in range(1,i+1):
        print("*", end=" ")
    print()








#    * 
#   * * 
#  * * * 
# * * * * 
#* * * * * 

#n = 5
#k = n-1
#for i in range(0, n):
#    for j in range(0, k):
#        print(end=" ")
#    
#    k = k-1
#    
#    for j in range(0, i+1):
#        print("*", end=" ")
#        
#    print()

