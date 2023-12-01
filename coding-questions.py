#Question 1: Write a function to print "hell0_USERNAME!"
   #USERNAME is the input of the function.
   #The first line of the code has been defined as below:
      #def hello_name(user_name):

def hello_name(user_name):
    """Display a greeting."""
    print("hello_" + user_name + "!")
hello_name(user_name = "USERNAME" )

#Question 2: Write a Python finction, first_odds that prints the odd numbers 
# from 1-100 and returns nothing.
    #def first_odds():

def first_odds():
    """Print odd numbers from 1-100."""
    current_num = 0
    while current_num < 100:
        current_num += 1
        if current_num % 2 == 1:
            print(current_num)
            continue
first_odds()


#Question 3: Write a python function, max_num_in_list to return
 #the max number of a given list.
 #The first line of the code has been defined as below:
    #def max_num_in_list(a_list):

def max_num_in_list(a_list):
    """Return the maximum number in the list."""
    a_list = [1, 2, 3, 4, 5]
    x = max(a_list)
    return x
print(max_num_in_list("x"))


#Question 4: Write a Python function to return if the given year is a leap year.
    #A leap year is divisible by 4, but not divisible by 100, unless it is also 
    #divisible by 400. The return should be boolean Type (true/false).
    #def is_leap_year(a_year):

def is_leap_year(a_year):
    """Tell if a given year is a leap year."""
    return (a_year % 4 == 0 and a_year % 100 != 0) or (a_year % 400 == 0)

print(is_leap_year(2024))


#Question 5: Write a function to check to see if all numbers in a list are consecutive numbers.
    #For example, [2, 3, 4, 5, 6, 7] are consecutive numbers, but [1, 2, 4, 5] are not consecutive numbers. 
    #The return should be boolean Type.
        #def is_consecutive(a_list):
    
def is_consecutive(a_list):
    """See if all numbers in list are consecutive."""
    current_number = a_list[0]
    i = 1
    while i < len(a_list):
        next_number = a_list[i]
        if current_number + 1 == next_number:
            current_number = next_number
            i += 1
        else:
            return False
    return True    

print(is_consecutive([8, 9, 10, 11]))

print(is_consecutive([8, 9, 10, 12]))