# Up to now we've been making strings using the plus sign to just
# concatenate the parts of the string we wanted to create. An we've used the str
# function to convert numbers into strings so that we can concatenate them, too.
# This works, but it's not ideal, especially when the operations you want to do with
# the string or on the tricky side. There's a better way to do this using the format
# method. Let's see a couple of examples.

name = "Manny"
number = len(name) * 3
print("Hello {}, your lucky number is {}".format(name, number))
# Hello Manny your lucky number is 15
print("Your lucky number is {number}, {name}".format(name=name, number=len(name) * 3))

# In this example, we have two variables, name and number. We generate a string
# that has those variables in it by using the curly brackets placeholder to show
# where the variables should be written. We then pass the variables as a parameter
# to the format method. See how it doesn't matter that name is a string and
# number is an integer? The format method deals with that, so we don't have to.
# Pretty neat, right? The curly brackets aren't always empty. By using certain
# expressions inside those brackets, we can take advantage of the full power of the
# format expression. Heads up, this can get complex fast. If at any point, you get
# confused, don't panic, you only really need to understand the basic usage of the
# format method we just saw. One of the things we can put inside the curly
# brackets is the name of the variable we want in that position to make the whole
# string more readable. This is particularly relevant when the text can get rewritten
# or translated and the variables might switch places. In our earlier example, we
# could rewrite the message to make the variables appear in a different order. In
# that case, we'd need to pass the parameters to format in a slightly different way.



# Modify the student_grade function using the format method, so that it returns the
# phrase "X received Y% on the exam". For example, student_grade("Reed", 80) should
# return "Reed received 80% on the exam".

def student_grade(name, grade):
    return f"{name} received {grade}% on the exam"


print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))

price = 7.5
with_tax = price * 1.09
print(price, with_tax)
print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))

# Because we're using placeholders with variable names, the order in which the
# variables are passed to the format function doesn't matter. But for this to work,
# we need to set the names we're going to use and assign a value of them inside
# the parameters to format. And that's just the tip of the iceberg of what we can do
# with the format method. Want to dive a little deeper? Great, let's keep on going.
# We're going to check out a different example. Let's say you want to output the
# price of an item and with and without tas. Depending on what the tax rate is, the
# number might be a long number with a bunch of decimals. So if something costs
# $7.5 without tax and the tax rate is 9%, the price with tax would be $8.175. First
# off, ouch, and also, since there's no such thing as half a penny anymore, that
# number doesn't make sense. So to fix this we can make the format function print
# only two decimals, like this.


def to_celcius(x):
    return (x - 32) * 5 / 9

for x in range(0, 101, 10):
    print("{:>3} F | {:>6.2f} C".format(x, to_celcius(x)))

# In this case between the curly brackets we're writing a formatting expression.
# There are a bunch of different expressions we can write. These expressions are
# needed when we want to tell Python to format our values in a way that's different
# from the default. The expression starts with a colon to separate it from the field
# name that we saw before. After the colon, we write .2f. This means we're going to
# format a float number and that there should be two digits after the decimal dot.
# So no matter what the price is, our function always prints two decimals.
# Remember when we did the table to convert from Fahrenheit to Celsius
# temperatures? Our table looked kind of ugly because it was full of float numbers
# that had way too many decimal digits. Using the format function, we can make it
# look a lot nicer. In these two expressions we're using the greater than operator to
# align text to the right so that the output is neatly aligned. In the first expression
# we're saying we want the numbers to be aligned to the right for a total of three
# spaces. In the second expression we're saying we want the number to always
# have exactly two decimal places and we want to align it to the right at six spaces.
# We can use string formatting like this to make the output of our program look
# nice and also to generate useful logging and debugging messages. Over the
# course of my sysadmin career I've grown used to formatting strings to create
# more informative error messages. They help me understand what's going on with
# a script that's failing. There's a ton more formatting options you can use when
# you need them. But don't worry about learning them all at once, we'll explain
# any others as they come along and we'll put everything in a cheat sheet that you
# can refer to whenever you need a formatting expression. Let's take a look at that
# now and then we'll having quiz to help you get more familiar with all this new
# knowledge.