# Inheritance

# Wow, we've covered a bunch of new stuff in these last few videos.
# You're doing great, We've learned all about object-oriented programming,
# and how to define our own classes and methods, including special methods
# like constructors or string conversions. We;ve also learned how to document
# them all. We're now going to talk about another aspect of objet-oriented
# programming called inheritance. Just like people have parents,
# grandparents, and so on, objects have ancestry. The principle of
# inheritance let's a programming build relationships between concepts and
# group them together. In particular, this allows us to reduce code duplication
# by generalizing our code. For example, how could we develop our apple
# representation to include other types of fruit, too? Well, one thing we know
# about an apple is that it's fruit. So we could define separate fruit class. We
# also know that all fruits have a color and taste. So what if we moved our
# color and flavor attributes into the fruit class? Here, we have a fruit class with
# a constructor for the color and flavor attributes. Now, we can rewrite our
# apple class and easily add another fruit into the mix, too.

# In Python, we use parentheses in the class declaration to show an
# inheritance relationship. For our new fruit classes, we've used that syntax to
# tell our computer that both the apple and the grape classes inherit from the
# fruit class. Because of this, they automatically have the same constructor,
# which sets teh color and flavor attributes. You can think of the fruit class as
# the parent class, and the apple and grape classes as siblings. Let's see this in
# action. First, we create an instance of the apple class.

# Granny_smith equals Apple. And we'll give it two parameters, green as the
# colro and tart as the flavor.

# And now, an instance of the grape class.

# Then, to check that this actually worked, let's print the attributes values.

# With the inheritance technique, we can use the fruit class to store
# information that apples to all kinds of fruit, and keep apple or grape specific
# attributes in their own classes. For example, we could have an attribute to
# track how much of an apple is left after it's partially eaten. Of course, this
# applies to both attributes and methods. If a class has an attribute or a
# method defined i it, inheriting classes will have the same attributes and
# methods defined in them. But we can also get them to behave differently
# depending on what we change. To explore this, let's go back to our piglet
# example and change it so that there's a base animal class. In this code, we've
# defined a general class called animal, which has an attribute to store the
# sound that the animal makes. The constructor of the class takes the name
# that will be assigned to the instance when it's created. There's also a speak
# method that prints the name of the animal together with the sound the
# animal makes. Then, we have a piglet class that inherits from the animal
# class. We set the value of the sound attribute to oink in the piglet class, and
# that's the only thing we've modified from the original. Everything else is
# inherited. Let's see this in action.

# Let's define a new class that also inherits from animal. How about a cow
# class?

# Cool, and to finish, let's create an instance of this class to make it speak.

# So you can see that we can easily define new classes that inherit from the
# base animal class and use both the attributes and methods that the animal
# class provides. Pretty cool, right?

# Let's think of a different example, something closer to what you might be
# doing at your day-to-day job. In a system that handles the employees at your
# company, you may have a class called employee, which could have the
# attributes for things like full name of the person, the username used in
# company systems, the groups the employee belongs to, and so on. The
# employee class cold have methods to do a bunch of things, like check if an
# employee belongs to a certain group, or create an email address based on
# the name and username attributes. The system could also have a manager
# class. A manager is an employee that reports to a specific manager. Are you starting
# to get an idea of the power of inheritance? Inheritance lets you reused code
# written for one class in other classes. Next up, we're going to talk about a
# different way of reusing code.


class Fruit:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

class Apple(Fruit):
    pass

class Grape(Fruit):
    pass

granny_smith = Apple("green", "tart")
carnelian = Grape("purple", "sweet")
print(granny_smith.flavor)
print(carnelian.color)

class Animal:
    sound = ""
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("{sound} I'm {name}! {sound}".format(
            name=self.name, sound=self.sound))

class Piglet(Animal):
    sound = "Oink!"

hamlet = Piglet("Hamlet")
hamlet.speak()

class Cow(Animal):
    sound = "Moooo"

milky = Cow("Milky White")
milky.speak()

class Clothing:
    material = ""
    def __init__(self, name):
        self.name = name

    def checkmaterial(self):
        print("This {} is made of {}".format(self.name, self.material))

class Shirt(Clothing):
    material="Cotton"

polo = Shirt("Polo")
polo.checkmaterial()

