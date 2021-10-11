# So how are you doing so far? Is everything making sense? Are all those apple
# examples making you hungry? Feel free to pause and grab a snack if that's
# what you need. We called out earlier that we use methods to get objects to
# do stuff. We've seen several methods in our example so far like lower for
# strings, append for lists or values for dictionaries. The key to understanding
# methods is this; methods are functions that operate on the attributes of a
# specific instance of a class. When we call the append method on a list, we're
# adding an element to the end of that specific list and not to any other lists.
# When we call the lower methods on the string, we're making the contents of
# that specific string lowercase. How exactly does this happen? Let's take a
# closer look by defining our own methods. First, we need to define a class
# and create an instance of it like we've done before. Nice, we've created a
# piglet class. While our new piglet might be cute, it can't do a whole lot now.
# What if we wanted to give it a voice? For objects to perform actions, they need
# methods and as we called out before, a method is a function that operates
# on a single instance of an object. Let's add a method to our class. You can see
# here that we start defining a method with the def keyword just like  we would
# for a function, and see how the line with the def keyword is indented to the
# right inside the Piglet class? That's how we define a function as a method of
# the class. This function is receiving a parameter called self. This parameter
# represents the instance that the method is being executed on. Let's try this
# out and see what happens.

# Hamlet equals piglet hamlet.speak and the piglet goes, oink oink. It sure
# does, but this makes the piglet say the same thing for all instances of the
# class. Boring? Let's make the method do something different depending on
# the attribute of the instance. This time we've studied the body of the class by
# defining an attribute called name with a default value of Piglet. We can
# change that value later but it's a good idea to set it now to make sure our
# variable is initialized. If you look closely at how we wrote the newspeak
# method, you'll see that it's using the value of self.name to know what name
# to print. This means that it's accessing the attribute name from the current
# instance of Piglet. Let's try this out.

# So set hamlet equals piglet. Then we can say hamlet.name, and we'll set the
# name to a string Hamlet, and then we can call hamlet.speak on hamlet. Meet hamlet
# our python pig. What? You didn't know pigs could talk? Well, they can in
# Python. In this example, the speak method printed the name Hamlet which
# was the name attribute that we set. What if we create a new instance of the
# same class but with a different name? It should generate a different output.
# Let's try this out. I think Hamlet needs a friend.

# We've now created two instances of the piglet class each of them with their
# own name. When calling this speak method each of them prints their name
# and not the other. Variables that have different values for different instances
# of the same class are called instance variables, just like the name variable in
# this example. Since methods are just functions that belong to a specific class,
# they can work as any other function. So they can receive more parameters
# and return values if needed. Let's check out what a method retuning a value
# looks like. In this case, we've created a method returns to change when we
# change the years attribute of our instance. Let's create an instance and check
# how this method works. Piggy is two-years-old and human years, how old is
# he and pig years?

# So as the value of the years attribute changes, the return value of the pig
# years method changes to. Coming up, we're going to learn about a few
# special types of methods including one in particular called constructor.


class Piglet:
    name = "piglet"
    def speak(self):
        print("Oink! I'm {}! Oink!".format(self.name))


hamlet = Piglet()
hamlet.name = "Hamlet"
hamlet.speak()

petunia = Piglet()
petunia.name = "Petunia"
petunia.speak()


class Piglet:
    years = 0
    def pig_years(self):
        return self.years * 18

piggy = Piglet()
print(piggy.pig_years())

piggy.years = 2
print(piggy.pig_years())


# OK, now it's your turn! Have a go at writing methods for a class.

# Create a Dog class with dog_years based on the Piglet class shown before
# (one human years is about 7 dog years).
class Dog:
    years = 0
    def dog_years(self):
        return self.years * 7

fido = Dog()
fido.years = 3
print(fido.dog_years())