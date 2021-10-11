# So far, we've been using the features that are baked into the Python
# language. The basic statements like if, for, while, or the definition of
# function or classes, are part of the language and ready for us to use
# whenever we need them. The same goes for integers, floats, strings, lists, and
# dictionaries. They're all part of the basic Python language because they're
# used so often. Of course, this isn't enough to get interesting things done.
# We'll need a lot of additional tools like being able to get interesting things done.
# network, read files from our machine, process images, or who knows what
# you might want to do to make your work more effective. To organize the
# code we need to perform tasks like these, Python provides an abstraction
# called a module. Modules can be used to organize functions, classes, and
# other data together in a structured way. Internally, modules are set up
# through separate files containing the necessary classes and functions.
# Python already comes with a bunch of ready-to-use modules. All these
# modules are contained in a group called the Python standard library. Let's
# see how we can use some of them. First, we'll use the import keyword to
# import the random module. This module is useful for generating random
# numbers or marking random choices.

# Now that we've imported the module, let's use a function provided by this
# module called randint.

# This function receives two parameters and generates a random number
# between the two parameters that we pass. In this case, we're generating a
# random number between 1 and 10. As you can see, this function returns
# different numbers each time it's called. Pretty fun, right? The syntax used for
# calling a function provided by a module is similar to calling a method
# provided by a class. It uses a dot to separate the name of the module and the
# function provided by that module. Let's try using a different module, the
# datetime module. We use this for handling dates and times.

# Now, let's get the current date.

# If you're wondering why we have a doubled datetime, it's because teh
# datetime module provides a datetime class, and the datetime class gives us a
# method called now. This mow method generates an instance of the datetime
# class for the current time. We can operate on this instance of datetime in a
# bunch of ways. Let's check out a couple of examples.

# When we call print with an instance of the datetime class, we see the date
# printed in a specfic format. Behind the scenes, the print function is calling
# the str method of the datetime class which formats it in the eway that we see
# here. We can also access the instance through its attributes and methods. For
# example, we can look at the individual parts of the date like the year, like
# this.

# The datetime module provides more classes than the datetime class. For
# example, we can use the timedelta class to calculate a date in the future or in
# the past. Let's try this out.

# In this case, we're creating an instance of the timedelta class with a value of
# 28 days, then we're adding it to the instance of the datetime class that we
# already had and printing out the result. There's a lot more things avaiable in
# the datime and random modules. If you're interested in learning more, you
# can read the whole reference, it's available online and we'll include a link in
# the next reading. This is just a sneak peek into what you could do with
# modules. You can also develop your own. We'll talk more about that in a later
# course. For now, just focus on using existing Python modules.
import random

random.randint(1, 10)

random.randint(1, 10)

random.randint(1, 10)

import datetime

now = datetime.datetime.now()
type(now)

print(now)
now.year
print(now + datetime.timedelta(days=28))
