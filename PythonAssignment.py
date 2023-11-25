
# writing  is_even function to determine if any number is even or not

def is_even():
    x = int(input("Enter a Number: "))
    
    # using the modulus operator to determine any number divided by 2 without reminder as a Even number
    
    if x % 2 == 0:
        return True
    else:
        return False
    

# writing calculate_grade function to determine the grade of the students

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


# writing calculate_area Fuction to calculate the area of a rectangle

def calculate_area():
    length = int(input("Enter the length of the rectangle: "))
    breadth = int(input("Enter the breadth of the rectangle: "))
    
    # calculate the area of the rectangle using the area formula
    
    area  = length * breadth
    print(f'Area of Rectangle is {area}')
    

# writing is_triangle Function to determine if the sides can form a valid triangle

def is_triangle():

    # prompting user for lengths of the sides
    
    a = int(input("Enter the length of the first side: "))
    b = int(input("Enter the length of the second side: "))
    c = int(input("Enter the length of the third side: "))
    
    # calculating two side and writing function if the sides can form a triangle using triangle inequality theorem.
    # Triangle inequality theorem says the sum of any of the two sides must be greater than to third side.
    
    if (a+b) > c and (a+c) > b and (b + c) > a:
        return True
    else:
        return False


# writing max_of_three function to determine the higest number.

def max_of_three():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = int(input("Enter the third number: "))
    
    # using the if-elif to return the maximum number than using an inbuilt function
    
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


# writing reverse_string Function to reverse any phrase or text.

def reverse_string():
    word = input("Enter a Word: ")
    
    # using the reverse indexing to change the direction of the word
    
    reverse_word = word[::-1]
    print(reverse_word)





