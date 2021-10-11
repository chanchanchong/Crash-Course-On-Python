# In an earlier video, we saw how we can't use the plus operator between an
# integer and a string because they're different data types. But what
# happens when we try to operate with an integer and a float instead, let's
# find out.

# Error-free, Python has no problem performing this operation. But what's
# up with that, aren't integer and a float two different data types? They sure
# are but there's a lot happening under the hood here. Behind the scenes
# the computer is busy automatically converting our integer seven into a
# float seven. This lets Python then add together the values to return results
# that is also a float. We call this process, implicit conversion. The interpreter
# automatically converts one data type in to another. We've called this out
# before, but it's worth highlighting again that Python operations aren't just
# restricted to numbers. You can also use the plus operator to add together
# strings. This lets you do things like create sentences from individual words.
# Just don't forget to add spaces to each words. Otherwise, the computer
# wiil run them all together. So what if you really want to combine a string
# and a number, is it possible? It sure is but only with an explicit conversion.
# In Python, to convert between one data type and another, we call a
# function with the name of the type we're converting to. Let's see how this
# works. Now, things are getting a little bit more complex. Let's take a
# moment to unpack this to make sure it all makes sense. In this script,
# we're first calculating the are of a triangle, and when printing it we're
# adding it to a string. To do this, we need to call the STR function to convert
# a number into a string. Let's execute it and check out what happens. Our
# number got converted to a string and print it together with the message.

# We've learned a little bit about variables, values, expressions, adn
# conversions. Next up, we've got a practice quiz to help you solidify your
# knowledge. As always, take your time and review the content if you need.
# You've totally got this. I'll see you in the next video once you're finished.



total = 2048 + 4357 + 97658 + 125 + 8
files = 5
average = total / files
print("The average size is: " + str(average))