# We talked about how inheritance creates an ancestry for our objects. To
# check for this ancestry, we can use the is a rule. An apple is a fruit, a piglet is
# an animal. They inherit the attributes and methods of their parent class and
# so they allow us to reduce code duplication, but what if you have a
# relationship between classes, where one class isn't a child of the other?
# Sounds confusing? Let's check out an example to get a better idea of this. Say
# we have a package class that represents a software package which could be
# installed on every machine on our network. This class has a lot of
# information on the software, like the name, the version, the size, and more.
# We also have a repository class that represents all the packages that we have
# available for installation internally. In this call, we want to know how many
# packages there are and what's the total size of all the packages. In this case,
# the repository isn't a package and the package isn't a repository. Instead, the
# repository contains packages. To model this within our code, the repository
# class will have an attribute that could be a list or a dictionary, which will
# contain instances of the package class. So for this scenario, we'll make use of
# the code in the other classes by calling their methods. This is what's called
# composition. Let's see this in action. We'll first create a repository class that
# starts with an empty dictionary of packages when it's created. The dictionary
# will have the names of the packages as keys and the package objects as
# values.

# Nice, We have our class, which starts with an empty dictionary of packages.
# You might be wondering why we are adding the dictionary in the constructor
# instead of directly to the class. The answer to this might be a bit tricky to
# understand. So let's go back to our juicy apple example to help make sure
# this is clear. We defined earlier a class called apple and set some basic
# attributes for it, like color and flavor. All instances of the apple class will be
# initialized with the values that we preset for those attributes. If we change
# the color of one apple from red to golden, we substitute the old value with
# the new one. Super-important to remember, this action happens only for
# that particular instance. But what if this apple has worm in it? What if we
# wanted out apple class to also have a list of worms? If we created the list
# when constructing the class, then all instances of the apple class would have
# the same exact list. So if we added a worm to the list, it would get added to
# the one list that's shared by all instances. To avoid this, we need to create the
# list at the time of creating the instance, instead of when creating the class. By
# doing this, each instance will have its own list independent of the others.
# This happens with all attributes that are mutable, because when we modify
# immutable attribute, we're not replacing a value with another, we're
# changing the contents of the original attribute. In our repository case, the
# packages attribute is a dictionary, which is mutable. We'll be modifying its
# contents by adding and removing elements in it. If we created it at the class
# level, all instances of the repository class would use the same dictionary and
# items added or removed would affect all instaces at the same time. If that's
# still a bit confusing, don't worry. I was also confused the first time I came
# across it. Just take your time. Re-watch this video if you need and remember
# this rules of thumb, always initialize mutable attributes in the constructor. So
# great, we've got our dictioary, but how will we add packages to it? We'll
# create an add_package method.

# Now, we can add packages to the dictionary. We could also write a similar
# method to remove the packages, but I bet you can work that out without my
# help. Let's do something more interesting instead. We said that the packages
# had a size attribute that holds the size in bytes that the software package
# requires. So how could we calculate the size of the whole repository? We
# need to iterate over the packages contained in the dictionary, adding up all
# their sizes. I'd go something like this.

# We're going to add up all the sizes. So the first thing we need to do, is create
# a result variable that we'll use to sum up the values.

# Awesome. We have our result initialized. We now need to go through all the
# packages in the dictionary. Remember, the keys are the packages names adn
# the values are the package objects. For our calculation, we only care about
# the objects. So we'll retrieve them with the values dictionary method.

# Now, for each package, we want to add the size to the result varaible.

# Nice. We're almost done. We just need to return the result now.

# Take a look at the method we've just written. It's a method inside the
# repository class, that's making use of the values method in the dictionary
# class and it's accessing the size attribute in the package class. That is the
# power of composition. When we have other objects as attributes, we can use
# all their attributes and methods to get our own code to do what we want.
# Wow. that was pretty complex. Chances are, you won't get it the first time
# around. Most of us don't. So if you're worried you might have missed
# something, take your time to review the contents. We want you to feel
# confident before moving on. when you're ready, meet me in the next video,
# where we're going to talk about a different kind of code we use using Python
# modules.

class Repository:
    def __init__(self):
        # Always initialize mutable attributes in the constructor.
        self.packages = {}

    def add_package(self, package):
        self.packages[package.name] = package

    def total_size(self):
        result = 0
        for package in self.packages.values():
            result += package.size
        return result

# Let's expand a bit on our Clothing classes from the previous in-video
# question. Your mission: Finish the "Stock_by_Material" method and
# iterate over the amount of each item of a given material that is in stock.
# When you're finished, the script should add up to 10 cotton Polo shirts.


class Clothing:
    stock = {'name': [], 'material': [], 'amount': []}

    def __init__(self, name):
        material = ""
        self.name = name

    def add_item(self, name, material, amount):
        Clothing.stock['name'].append(self.name)
        Clothing.stock['material'].append(self.material)
        Clothing.stock['amount'].append(amount)

    def Stock_by_Material(self, material):
        count = 0
        n = 0
        for item in Clothing.stock['material']:
            if item == material:
                count += Clothing.stock['amount'][n]
                n += 1
        return count

class shirt(Clothing):
    material = "Cotton"

class pants(Clothing):
    material = "Cotton"

polo = shirt("Polo")
sweatpants = pants("Sweatpants")
polo.add_item(sweatpants.name, sweatpants.material, 4)
sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
current_stock = polo.Stock_by_Material("Cotton")
print(current_stock)