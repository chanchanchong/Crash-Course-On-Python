# We've seen a few arithmetic expressions so far, like addition,
# subtraction, and division. Remember when we turned Python into a
# calculator? Well, Python can also compare values. This lets us check
# whether something is smaller than, equal to, or bigger than something
# else. This allows us to take the result of our expressions and use them to
# make decisions. Check out these three examples. In the first example 10 is
# greater than 1, so the value true is printed as a result. True is a value that
# belongs to another data type called the Boolean. Booleans represent one
# of two possible states, either true or false. Every time you compare things
# in Python the result is a Boolean of the appropriate value. In the second
# example we can see your very first equality operator, which is formed by
# putting two equal signs together. We use this operator to test whether two
# things are equal signs together. We use this operator to test whether two
# things are equal to each other. In this example the string cat is not equal to
# the string dog, so the Boolean that's printed is false. In our third example
# we're doing the opposite comparison. By pairing an exclamation mark and
# an equal sign we're using the not equals operator, which is the negated
# form of the equality operator. In this particular line of code the operator
# checks that 1 isn't equal to 2. We call out before that the plus operator
# doesn't work between integers and string? Let's find out by seeing if the
# number 1 is taller than the string 1.

# Wha , wha, wha, we get a type error. That's the same error we got before.
# This happens because Python doesn't know how to check if a number is
# smaller than a string. And what about the equality operator?

# In this case the Interpreter has no problem telling us that the integer 1 and
# the string 1 aren't the same. So what gives? Basically although they may
# seem similar to us because they both contain the same number, it's clear
# to the computer that one is a number and the other is the string. For the
# computer it's obvious that they are completely different entities.

# On top of the comparison and equality operators, Python also has a set of
# logical operators. These operators allow you to connect multiple
# statements together and perform more complex comparisons. In Python
# the logical operators are the words and, or, and not, let's look at some
# examples.

# To evaluate as true the and operator would need both expressions to be
# true at the same time here. Here we're comparing strings, and the bigger
# and smaller operators refer to alphabetical order. Yellow comes after cyan,
# but brown doesn't come after magenta. So this means that the first
# statement is true, but the second one isn't, which makes the result of the
# whole expression false. If we use or operator instead the expression
# will be true if either of the expressions are true, and false only when both
# expressions are false. Let's try it out. 25 is definitely not bigger than 50, but
# 1 is different than 2. So in the end the whole expression is true. Last up,
# the not operator inverts the value of the expression that's in front of it. If
# the expression is true, it becomes false. If it's false, it becomes true. Just
# like this. Logical operators are important because they help us write more
# complex expressions. We'll see this in action in the next few videos. If this
# is the first time you've come across these operators it might seem like
# there's a lot to remember. But don't worry, you'll learn most of them very
# quickly just by practicing. And in the next reading we have a cheat sheet
# that lists all the operators available and what each one does. It's a handy
# resource you're sure to find useful when writing your own scripts.


# Figure out what's the relationship between the strings "cat" and "Cat" by
# replacing the plus sign with comparison operators.

print("cat" > "Cat")
