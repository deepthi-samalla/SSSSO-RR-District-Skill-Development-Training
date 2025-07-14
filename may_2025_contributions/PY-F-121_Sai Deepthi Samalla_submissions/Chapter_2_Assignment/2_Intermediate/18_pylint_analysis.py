# Chapter 2 - Intermediate Assignment 8: Pylint Analysis
# Question: Analyze a script using pylint and fix at least 3 warnings or errors.

import os, sys # This line is often flagged by pylint (multiple imports on one line)

# A global constant that should ideally be ALL_CAPS
my_constant = 10 

def my_function( a,b): # Pylint will check spacing, and suggest better function names
    # A variable that is not used anywhere else in the function
    unused_var = a + b 
    return( a*b) # Pylint checks spacing around operators and superfluous parentheses

class MyClass: # Pylint often suggests a docstring for classes
    def __init__(self, val):
        self.value = val
    def get_val(self): # Pylint might suggest a docstring here too
        return self.value

def another_function(x):
    print("Hello") # Check for trailing whitespace if copied directly from some sources

    # This variable might be unused if the loop is skipped, or its name is very long.
    long_variable_name_that_is_not_used_in_some_path = 0 

    for i in range(x):
        print(f"Number {i}")

# Calls to functions - Pylint might have warnings about these calls being at the top-level
my_function(my_constant, 5) 
another_function(2)