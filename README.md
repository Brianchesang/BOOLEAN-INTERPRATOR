# BOOLEAN-INTERPRATOR
Program Description
This program allows the user to input a boolean operation using T and F variables, Boolean operations (A= and, O = or, N = not) and variables within brackets.

The program then takes the input, breaks it down into individual units of information, and extracts the key elements i.e. brackets, variables, and Boolean instructions.

Finally, the program performs boolean operations by evaluating the boolean expression.

Functions
Input_breakdown()
This function takes the input from the user and breaks it into individual units of information in a list.

element_detectionAndBreakdown(list)
This function scans through and notes the position of key elements which are the brackets, and the Boolean operands that are in use, it then stores their positions in variables for the booleans and in lists for the brackets both square and regular brackets.

the_Value_changer(list)
This function changes every T value to 1 and every F value to 0.

boolean_solve(list,list2)
This function uses the broken down input and the positional information of all operands and brackets in the broken-down input to perform boolean operations.

and_Op(condition1, condition2)
This function performs an AND operation. It takes two conditions as arguments and returns 1 if both conditions are true, otherwise 0.

or_Op(condition1, condition2)
This function performs an OR operation. It takes two conditions as arguments and returns 1 if at least one of the conditions is true, otherwise 0.

not_OP(condition)
This function performs a NOT operation. It takes one condition as an argument and returns the opposite of the condition.

the_merge()
This function executes the entire program. It checks whether the input has brackets or not, and if it does, it evaluates the expression within the brackets first. If there are square brackets, it stores the variables in a dictionary. Finally, it evaluates the entire expression using the boolean_solve function.

Variables
variableStore
A dictionary that stores variables and their values.

brackets
A list that stores the positions of regular brackets.

sbrackets
A list that stores the positions of square brackets.

A
A list that stores the positions of "A" operands (AND).

O
A list that stores the positions of "O" operands (OR).

N
A list that stores the positions of "N" operands (NOT).

assign
An integer that stores the position of the "=" operator.

inputx
A string that stores the user's input.

temp_position
An integer that keeps track of the position while breaking down the input.

values
A list that stores the broken-down input.

elements
A list that stores the broken-down input.

sub_list_brackets
A list that stores the broken-down expression within brackets.

How to Use
type in the boolean operation you want to be done. 
the program takes T for true and F for false so an example of input is TAT this will perform an and operation and give 1 as output.


