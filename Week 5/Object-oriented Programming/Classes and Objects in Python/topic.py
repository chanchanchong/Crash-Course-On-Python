# Remember how we use the type function when checking what type
# a certain variable was? Let's do that again now.

# When we use the type function as we just did here, Python tells us which
# class the value or variable belongs to. And since this is a class, it has a bunch
# of attributes and methods associated with it. Let's take the string class for
# an example. In this case, the only attribute is the content of the string. What
# about the methods? Well, in earlier videos, we looked at a bunch of methods
# provided by the string class, like upper() to create an uppercase version of
# the string. Or isnumeric() which checks whether or not the contents are all
# numeric. Each string we've used in Python up to now has been a different
# instance of the string class. They all had the same methods, but the
# contents were different. This meant that the result of calling those methods
# was different also. You can get your computer to list all the attributes and
# methods in a class To do that Just use the dir function. This gets the
# interpreter to print to the screen a list of all the attributes and methods.

# Well, that's a lot of items. Let's break this down a little bit, so we all
# understand what's going on. The first bunch here are special methods that
# begin and end with double underscores. These methods aren't usually
# called by those weird names. Instead, they're called by some of the internal
# Python functions. For example, the __len__method is called by the len
# function that we've used before to find out the length of a string. Or the
# __ge__ method is used to compare if one string is greater than or equal to
# another, when using the greater than or equal to operator

# After the special methods, we see a lot of string methods that we've already
# come across. This list gives the names of all the methods, but it doesn't tell
# us how we can use them. There's a different function to tell us that, which is
# called help. Let's give that one a go.

# We we use the help function on any variable or value, we're showing all
# the documentation for the corresponding class. In this case, we're looking at
# the documentation for the str class, the class of the string object. As before,
# it starts with the special method. If we scroll down, we reach the ones we've
# already seen. We can see the documentation for a bunch of methods, and it
# tells us the parameters that method receives and the type of return value. It
# also includes an explanation of what the method does. For the count
# method we can see that it receives the sub string that will be counted, and it
# has optional start and end arguments to indicate which slice of the string
# would be looked at. WE know they're optional because they're written
# between square brackets. In general, being able to read and understand a
# method's documentation is super important when you're writing your own
# code. Using the dir and help functions puts all the documentation right at
# your fingertips. This makes it so much easier to figure out how to use
# something for the first time. When you're done looking at documentation,
# you can just type q to quit.
