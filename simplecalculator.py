#!/usr/bin/env python
# coding: utf-8

# In[1]:


#****************HOW TO BUITLD A SIMPLE CALCULATOR IN PYTHON**************
# 1. ADD
# 2. SUBTRACT
# 3. MULTIPLY
# 4. DIVIDE

print("Select an operation to perform:")
print("1. ADD")
print("2. SUBSTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

operation = input()

if operation == "1":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number")
    print("The sum is " + str(int(num1) + int(num2)))
elif operation == "2":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number")
    print("The difference is " + str(int(num1) - int(num2)))
elif operation == "3":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number")
    print("The product is " + str(int(num1) * int(num2)))
elif operation == "4":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number")
    print("The result is " + str(int(num1) / int(num2)))
else:
    print("Invalid Entry")


    



# In[ ]:




