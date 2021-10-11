# As we've called out before, functions are powerful because you
# can create your own. You can use them to organize the code in your
# scripts into logical blocks, which makes the code you write easier to use
# and reuse. Check you this example.

# This script uses the len function, which returns the length of a string. In
# this example the script then uses that length to calculate a number, which
# we're calling the lucky number here. And finally, it prints a message with
# the name and the number. Each time you want to perform the calculation,
# we change the values of the variables and write the formula. Then, print a
# greeting followed by the lucky number. See how there are exactly two lines
# that are the same, in the first and second part of the code. When you find
# code duplication in your scripts, it's a good idea to check if you can clean
# things up  a bit by using a function. How about we rewrite this code
# creating a function to group all the duplicated code into just one line. The
# updated script gives us the exact same result as the original one, but it
# looks a lot cleaner. First, we've defined a function called lucky number,
# which carries out our calculation and prints it for us. Then we call the
# function twice, once with each name. Since we've grouped the calculation
# and print statements into a function, our code is not only easier to read
# but it's also now reusable. We can execute the code inside the lucky
# number function as many times as we need it, by just calling it with a
# different name. So we don't have to write it out and again and again for
# each new name, that makes sense?

# Hopefully, these examples have helped explain how functions are used
# and defined. And also demonstrated how useful they can be. Did you
# notice that we're feeding information into a function through their
# parameters? This is one of the many ways that we can input data into our
# code. The value for those parameters may come from different places,
# like a file on our computer or through a form on a website, but that
# doesn't impact our code. The result of the function is still the same, no
# matter where the parameters come from. Function are your friends. They
# can help clean up your code and do a math so you don't have to. You'll be
# using them a lot both in this course and in your programming life. So get
# ready to get real friendly with functions.


# Ready to try it yourself? See if you can reduce the code duplications in this script.

# In this code, identify the repeated pattern and replace it with a function called
# month_days, that receives the name of the month and the number of days in that month
# as parameters. Adapt the rest of the code so that the result is the same. Confirm the
# results by making a function call with the correct parameters for both months listed.

# REPLACE THIS STARTER CODE WITH YOUR FUNCTIONS
def month_days(month, days):
    print(month, "has", days, "days.")


month_days("June", 30)
month_days("July", 31)
