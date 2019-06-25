'''
Created on Jun 19, 2019

@author: karl
'''

#Variables are used in programming to store information so it can be used or changed later

#There are different types of variables
myInteger = 2       #Integer: Whole numbers
myFloat = 2.5   #Floating Point: Non-whole numbers
myString = "ABC"   #String: Characters

#As shown in HelloWorld and Math, variables can be combined
print(myInteger + myFloat)

#Floating points and integers can be combined because they are both numeric values.
#To combine numeric values with a string you have to convert them into strings
print(myString + str(myInteger) + str(myFloat))