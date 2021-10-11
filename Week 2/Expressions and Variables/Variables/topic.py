# When we ask a computer to perform an operation for us, we usualy need
# to store values and give them names so that we can refer to them later.
# This is where variables come in handy. Variables are names that we give to
# certain values in our programs. Those values can be of any data type;
# numbers, strings or even the results of operations. We already used
# variables in some of our initial examples like using them to store a name
# or a value. Now we are going to kearn exactly how they work and how to
# make the most of them. Think of variables as containers for data. When
# you create a variable in your code, your computer reserves a chunk of its
# own memory to store that value. This lets the computer access the
# variable later to read or modify the value. Let's see this in action. Imagine a
# simple script that calculates the area of a rectangle using the formula area
# equals length times width. Area, length and width can all be represented
# by variables like this. In this script we are creating three variables and
# storing different values in each. The process of storing a value inside a
# variable is called assignment. Here we assign the length variable the value
# of 10. We assign the width variable the value of two and we assign the
# area variable with the result of the expression length times width. An
# expression is a combination of numbers, symbols or other variables that
# produce a result when evaluated. In this example, we are multiplying the
# value of two variables to arrive at the value that we want. Finally, we use
# our old friend the print function to display the value of the area on the
# screen. All right. We have just seen how to assign values to variables, use
# expressions to calculate more complex values and then print the contents
# of a variable. Variables are important in programming because they let
# you perform operations on data that may change. For example, if we
# extended our rectangle script to accept any input as the value of the
# length and width variables, we could calculate the area of a rectangle of
# any size or to give a more IT focused example, say we have a script that
# performs a specific operation on a file. We can extend that script to
# perform the same operation on anh file but only if the program that we assign a
# value to a variable by using equal sign in the form of variable equals
# value. Generally, you can name variables whatever you like but there a re
# some restrictions. First, shouldn't use as variable names any of the key
# reserved terms wil make your program confusing to read and will result in
# errors. Python also has some restrictions on the characters you can use to
# define a variable. Variable names can't have any spaces and they must
# start with either a letter or any underscore. Also, they can only be made up
# of letters, numbers, and underscores. Let's check out some examples of
# valid and invalid variables names to understand this better.

# I_am_a_variable is the valid variable name.

# I_am_a_variable2 is also a valid variable name. 1_is_a_number is invalid
# because variable names must start with a letter or underscore.
# Apples_&_oranges is invalid because it uses the special character uppers
# hand. Last thing, remember that precision is important when
# programming. Python variabels are case sensitive, so capitaliation
# matter.s Lowercase name, uppercase name and all caps name are all valid
# and different variable names, and that rule on variables is invariable.


base = 5
height = 3
area = (base * height) / 2

print(area)

