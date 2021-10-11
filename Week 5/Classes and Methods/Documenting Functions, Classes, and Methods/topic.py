# The world of classes and methods can be a little puzzling when you're still
# learning your way around, and that's why the help function can come in
# handy. You might remember that we can still use the Python function help to
# find documentation about classes and methods. We can also do this on our
# own classes, methods, and functions. Let's check this out. We'll start with the
# Apple class we used before, and now we'll ask for some help.

# See how when we asked for help on our class we got a list of the methods
# that are defined in the class? In this example, the defined methods are the
# constructor and the conversion to string. But this documentation is super
# short and to be honest, it doesn't explain a whole lot. So let's go back to the
# interpreter by typing Q.

# We want our methods, classes, and function to give us more information
# when we or someone else use the help function. We can do that by adding a
# docstring. A docstring is a brief text that explains what something does. Let's
# see how this works with a simple function. First off, we want to define the
# function. So def, we'll call it to_seconds and we'll give it the parameters
# hours, minutes, and seconds.

# Next, we write the code for our function,

# Return hours multiplied by 3600 plus minutes times 60 plus seconds.

# So there we have it, we have a function with a docstring in its body. Let's see
# how we can use the help function to see it. Help to_seconds.

# Success. The help function shows us the string we wrote.

# As we called out earlier, we can add docstrings to classes and methods too.
# Let's use our piglet class to set what this would look like. Now we've got a
# bunch of helpful information, we've added docstrings for our piglet class and
# for its methods. Remember that the docstring always has to be indented at
# the same level of the block it's documenting. Docstrings are super helpful for
# figuring out how to use a function you've never used before. Not only that, if
# you're reading a piece of code written by someone else, docstrings let us
# understand the code much better because the classes, methods, and
# functions are clearly documented. So when writing your code, add
# docstring to explain your functions, classes, and methods. It'll make a ton of
# difference to anyone who might use your code.


class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

    def __str__(self):
        return "This apple is {} and its flavor is {}".format(self.color, self.flavor)


# help(Apple)

def to_seconds(hours, minutes, seconds):
    """Return the amount of seconds in the given hours, minutes, seconds."""
    return hours * 3600 + minutes * 60 + seconds


class Piglet:
    """Represents a piglet that can say their name."""
    years = 0
    name = ""
    def speak(self):
        """Outputs a message including the name of the piglet."""
        print("Oink! I'm {}! Oink!".format(self.name))

    def pig_years(self):
        """Converts the current age to equivalent pig years."""
        return self.years * 18


# Remember our Person class from the last video? Let's add a docstring to the greeting
# method. How about "Outputs a message with the name of the person".

class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        """Outputs a message with the name of the person."""