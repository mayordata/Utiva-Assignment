#!/usr/bin/env python
# coding: utf-8

# In[87]:


# writing a is_even function 

def is_even():
    x = int(input("Enter a Number: "))
    
    # using the modulus operator to determine any number divided by 2 without reminder as a Even number
    
    if x % 2 == 0:
        return True
    else:
        return False
    


# In[81]:


is_even()


# In[35]:


# writing calculate_grade function

def calculate_grade():
    score = int(input("Enter a number: "))
    
    # using the if-elif Condition to pass the operation
    
    if score >= 90:
        print('A')
    elif score >= 80:
        print('B')
    elif score >= 70:
        print('C')
    elif score >= 60:
        print('D')
    else:
        print('F')


# In[36]:


calculate_grade()


# In[40]:


# writing calculate_area

def calculate_area():
    length = int(input("Enter the length of the rectangle: "))
    breadth = int(input("Enter the breadth of the rectangle: "))
    
    #calculate the area of the rectangle
    
    area  = length * breadth
    print(f'Area of Rectangle is {area}')
    


# In[41]:


calculate_area()


# In[33]:


# writing is_triangle Function

def is_triangle():

    # prompting user for length value intake
    
    a = int(input("Enter the length of the first side: "))
    b = int(input("Enter the length of the second side: "))
    c = int(input("Enter the length of the third side: "))
    
    # calculating two side and writing function if the sides can form a triangle using triangle inequality theorem.
    # Triangle inequality theorem says the sum of any of the two sides must be greater or equal to the third side.
    
    d = a + b 
    if d >= c:
        return True
    else:
        return False


# In[34]:


is_triangle()


# In[82]:


# writing max_of_three function

def max_of_three():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = int(input("Enter the third number: "))
    
    # using the if-elif to reyrun the maximum number than using an inbuilt function
    
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


# In[83]:


max_of_three()


# In[85]:


# writing reverse_string Function

def reverse_string():
    word = input("Enter a Word: ")
    
    # using the reverse indexing to change the direction of the word
    
    reverse_word = word[::-1]
    print(reverse_word)


# In[86]:


reverse_string()


# In[ ]:




