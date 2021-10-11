# Up to now, we've been creating classes with empty or default values and
# their attributes and then setting the attribute values after we've created the
# object. This works, but it's not ideal. Working this way means we need to
# write a separate line for each attribute we want to set, and that makes it
# really easy to forget to set an important value. Us humans are pros at
# good idea to do things early to prevent from forgetting them later on. So let's
# set those values as we create the instance: This way, we know that our
# instance has all the important values in it from the moment is created and
# we don't have to worry about it. To do this, we need to use a special method
# called constructor. Lets go back to our apple example to see this in action.
# The constructor of the class is the method that's called when you call the
# name of the class. It's always named init. You might remember that all
# methods tht start and end with two underscores are special methods. Here,
# we've defined a constructor, one very important special method. This
# method on top of the self variable that represents the instance receives two
# more parameters: color and flavor. Then the method sets those values as the
# values of the current instance. Let's see how that works with the new
# instance of the apple class. Jonagold equals apple, and we'll give it red and
# sweet. Greet. Now, let's check that all the attributes are set correctly. Print
# jonagold.color. Perfect. So now by adding a constructor method that sets the
# attributes, we can create the class and have its values set right when it's
# created. Pretty handy, right? Constructors aren't the only special methods
# we can write. When we use the STR or print functions to convert an object to
# a string, we are using a super-useful special method. But before we go ahead
# and define one, let's see what happens when we don't define it.

# We just tried to print our apple instance, and we got a very weird message.
# We have the words apple and object in there, but what's the rest of it? Well,
# when we don't specify a way to print an object, Python uses the default
# method that prints the position where the object is stored in the computer's
# memory. This is definitely not what we wanted. If you every try and print
# something and Python prints a random string of numbers and letters, you'll
# know that it's likely using the default representation, which is the position of
# the object in the computer's memory. So how do we tell Python to print
# something that makes sense for us? We use the special STR method which
# returns the string that we want to print. Let's see what this looks like, By
# defining the special STR method, we've telling Python that we want to
# display when the print function is called with an instance of our class. Check
# it out. Jonagold equals apple. We'll give it red and sweet. Print jonagold. So
# the STR method lets us print a friendly message instead of a bunch of
# numbers. In general, it's a good idea to think ahead and define the STR
# method when creating objects that you want to print. There are a lot of other
# special methods. We're not going to look at the rest of them here, but you
# can find pointers to learn more about them in the official documentation.
# You'll find the link to that in the nex treading. These concepts are new and
# not to easy. So don't worry if you're still trying to figure out the difference
# between a method and a function. We've all been there. The best way to feel
# confident is to keep practicing until it's clear. You're doing great. So keep at
# it.
class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor


jonagold = Apple("red", "sweet")
print(jonagold.color)


# Want to see this in action?

# In this code, there's a Person class that has an attribute name, which gets set
# constructing the object. Fill in the blanks so that 1) when an instance  of the class is
# created, the attribute gets set correctly, and 2) when the greeting() method is called,
# the greeting states the assigned value.
class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return f"hi, my name is {self.name}"


# Create a new instance with a name of your choice
some_person = Person("Yay")
# Cal lthe greeting method
print(some_person.greeting())

print(jonagold)


class Apple:

    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

    def __str__(self):
        return "This apple is {} and its flavor is {}".format(self.color, self.flavor)

jonagold = Apple("red", "sweet")
print(jonagold)