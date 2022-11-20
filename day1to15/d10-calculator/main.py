"""
   This program will prompt the user to use calculator.
   This program is implemented by dictionary and use loops in the functions

   Aurel Villyani
"""

from art import logo

def add(n1, n2):
   return n1 + n2

def subtract(n1, n2):
   return n1 - n2

def multiply(n1, n2):
   return n1 * n2

def divide(n1, n2):
   return n1 / n2

# create a dictionary named operations
# keys and values
operations ={
   "+": add,
   "-": subtract,
   "*": multiply,
   "/": divide
}

def calculator():
   """ Prompt the user to use the calculator """
   print(logo)
   number1 = int(input("what's the first number: "))
   # loop through all the keys
   for symbol in operations:
      print(symbol)
   should_continue = True

   while should_continue:
      operation_symbol = input("Pick an operation from the line above: ")
      number2 = int(input("what's the second number: "))
      calculation_function = operations[operation_symbol]
      first_answer = calculation_function(number1, number2)
      
      print(f"{number1} {operation_symbol} {number2} = {first_answer}")

      if input(f"Type 'y' to continue calculating with {first_answer}, or type 'n' to start a new calculation: ") == "y":
         number1 = first_answer
      else:
         should_continue = False
         calculator()
         
calculator()