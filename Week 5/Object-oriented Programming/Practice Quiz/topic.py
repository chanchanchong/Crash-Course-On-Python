# Practice Quiz: Object-oriented programming

# 1. Let's test your knowledge of using dot notation to access methods
#    and attributes in an object. Let's say we have a class called Birds.
#    Birds has two attributes: color and number. Birds also has a
#    method called count() that counts the number of birds (adds a
#    value to number). Which of the following lines of code will correctly
#    print the number of birds? Keep in mind, the number of birds is 0
#    until they are counted!

# 2. Creating new instances of class objects can be a great way to keep
#    track of values using attributes associated with the object. The
#    values of these attributes can be easily changed at the object level.
#    The following code illustrates a famous quote by George Bernard
#    Shaw, using objects to represent people. Fill in the blanks to make
#    the code satisfy the behavior described in the quote.

# "If you have an apple and I have an apple and we exchanged these apples then
# you and I will still each have one apple. But if you have an idea and I have
# an idea and we exchanged these ideas, then each of us will have two ideas."
# Geo Bernard Shaw

class Person:
    apples = 0
    ideas = 0


johanna = Person()
johanna.apples = 1
johanna.ideas = 1

martin = Person()
martin.apples = 2
martin.ideas = 1


def exchanges_apples(you, me):
    # Here, despite G.B Shaw's quote, our characters have started with  # different amount of apples so we can better observe the results.
    # We're going to have Martin and Johanna exchange All their apples with # one another.
    # Hint: how would you switch values of variables.
    # so that "you" and "me" will exchange ALL their apples with one another?
    # Do you need a temporary variable to store one of the values?
    # You may need more than one line of code to do that, which is OK.
    temp = you.apples
    you.apples = me.apples
    me.apples = temp
    return you.apples, me.apples


def exchange_ideas(you, me):
    # "you" and "me" will share our ideas with one another.
    # What operations need to be performed, so that each object receives
    # the shared number of ideas?
    # Hint: how would you assign the total number of of ideas to
    # each idea attribute? Do you need a temporary variable to store
    # the sum of ideas, or can you find another way?
    # Use as many lines of code as you need here.
    temp = you.ideas
    you.ideas = me.ideas
    me.ideas = temp
    return you.ideas, me.ideas


johanna.apples, martin.apples = exchanges_apples(johanna, martin)
print("Johanna has {} apples and Martin has {} apples".format(johanna.apples, martin.apples))
ohanna.ideas, martin.ideas = exchange_ideas(johanna, martin)
print("Johanna has {} ideas and Martin has {} ideas".format(johanna.ideas, martin.ideas))


# 3. The City class has the following attributes: name, country (where the city is located)
#    elevation (measured in meters) and population (approximate, according to recent statistics).
#    Fill in the blanks of the max_elevation_city function to return the name of the city and its
#    country (separated by a comma). When comparing the 3 defined instances for a specified
#    minimal population. For example, calling the function of a minimum population of 1 million:
#    max_elevation_city(1000000) should return "Sofia, Bulgaria".

# define a basic city class
class City:
    name = ""
    country = ""
    elevation = 0
    population = 0


# create a new instance of the City class and
# define each attribute
City1 = City()
City1.name = "Cusco"
City1.country = "Peru"
City1.elevation = 3399
City1.population = 358052

# create a new instance of the City class adnd
# define each attribute
City2 = City()
City2.name = "Sofia"
City2.country = "Bulgaria"
City2.elevation = 2290
City2.population = 1241675

# create a new instance of the City class and
# define each attribute

City3 = City()
City3.name = "Seoul"
City3.country = "South Korea"
City3.elevation = 38
City3.population = 9733509


def max_elevation_city(min_population):
    # Initialize the variable that will hold
    # the information of the city with
    # the highest elevation
    return_city = City()

    # Evaluate the 1st instance to meet the requirements:
    # does city #1 have at least min_population and
    # is its elevation the highest so far?
    if min_population < City1.population and City1.elevation > return_city.elevation:
        return_city = City1
    # Evaluate the 1st instance to meet the requirements:
    # does city #1 have at least min_population and
    # is its elevation the highest so far?
    if min_population < City2.population and City2.elevation > return_city.elevation:
        return_city = City2
    # Evaluate the 1st instance to meet the requirements:
    # does city #1 have at least min_population and
    # is its elevation the highest so far?
    if min_population < City3.population and City3.elevation > return_city.elevation:
        return_city = City3

    # Format the return string
    if return_city.name:
        return f"{return_city.name}, {return_city.country}"
    else:
        return ""


print(max_elevation_city(100000))  # Should print "Cusco, Peru"
print(max_elevation_city(1000000))  # Should print "Sofia, Bulgaria"
print(max_elevation_city(10000000))  # Should print ""


# 5. We have two pieces of furniture: a brown wood table and red leather couch. Fill in the
# blanks creation of each Furniture class instance, so that describe_furniture function can
# format a sentence that describes these pieces as follows: "This piece of furniture is made
# of {color} {material}

class Furniture:
    color = ""
    material = ""


table = Furniture()
table.color = "brown"
table.material = "wood"

couch = Furniture()
couch.color = "red"
couch.material = "leather"


def describe_furniture(piece):
    return ("This piece of furniture is made of {} {}".format(piece.color, piece.material))


print(describe_furniture(table))
# Should be "This piece of furniture is made of brown wood"
print(describe_furniture(couch))
# Should be "This piece of furniture is made of red leather"
