class Apple:
    pass

class Apple:
    color = ""
    flavor = ""

jonagold = Apple()
jonagold.color = "red"
jonagold.flavor = "sweet"
print(jonagold.flavor)
print(jonagold.color)

golden = Apple()
golden.color = "Yellow"
golden.flavor = "Soft"

# We called out earlier that the point of object oriented programming is to
# help define a real-world concept in a way that the computer understands.
# Defining a real-world concept and code can be tricky. So let's look at how we
# might go about representing a concept in Python code. We'll take it step-by-
# step and keep it simple. Let's take our apple example from earlier. We could
# use this code to define a basic Apple class. Class Apple: pass. Sure, it doesn't
# look like much but with these two lines we've defined our first-class. Let's
# check out the syntax. In Python, we use the class reserved keyword to tell
# the computer that we're starting a new class. We follow this with the name
# of the class and a colon. The Python style guidelines recommend that class
# names should start with a capital letter. So we'll be using that convention. In
# this case, our class is called Apple. Class definitions follow the same pattern
# of other blocks we've seen before like functions, loops, or conditional
# branches. After the line with the class definition comes the body of the class,
# which is indented to the right. In this case, we haven't added anything to the
# body yet, so we use the pass keyword, to show the body is empty. We
# can also use the same keyword as a placeholder in any empty Python block.
# So how might expand our definition of the apple class? Well, it would
# probably have the same attributes that represent the information we want
# to associate with an apple like color and flavor. We can add that information
# like this. Class Apple: color, we'll set that to an empty string. Same with
# flavor. We'll set that to an empty string for now.

# So here we're defining two attributes: color and flavor. We define them as
# strings because that's what we expect these attributes to be. At the
# moment, they're empty strings, since we don't know what values these
# attributes will have. See how we don't need the pass keyword anymore now
# that we've got an actual body for the class. All right. Now that we've got an
# Apple class and some attributes, let see our Apple in action.

# Here, we're creating a new instance of our Apple class and assigning it to a
# variable called jonagold. Check out the syntax. To create a new instance of
# any class, we call the name of the class as if it were a function. Now that
# we've got our shiny new apple object, let's set the values of the attributes.

# All right. We've just set the color and the flavor as string values. To check
# that it worked, let's try retrieving them both and printing them to the
# screen.

# Print(jonagold.color). Print (jonagold.flavor). The syntax used to access the
# attributes is called dot notation because of the dot used in the expression.
# Dot notation lets you access any of the abilities that the object might have,
# called methods or information that it might store called attributes, like
# flavor. The attributes and methods of some objects can be other objects and
# can have attributes and methods of their own. For example. we could use
# the upper method to turn the string of the color attribute to uppercase. So
# print(jonagold.color.upper()).

# So far we've created one instance of the Apple class and set its attributes
# and checked that they are now correctly set. Now, we could create a new
# instance of the Apple class with different attributes. Golden equals Apple.
# Golder.color, we'll set that to yellow and golden.flavor equals soft. Both
# golden and jonagold are instances of the Apple class. They have the same
# attributes, color and flavor. But those attributes have different values.
# Congrats. You've learned how to create your own classes. Let's check that
# we've got all this down with a quick quiz. After that, we're going to learn
# how to define new method for a class.


# Want to give this a go? Fill in the blanks in the code to make it print a poem.
class Flower:
    color = "unknown"

rose = Flower()
rose.color = "red"

violet = Flower()
violet.color = "violet"

this_pun_is_for_you = "This poem is for you"

print("Roses are {}".format(rose.color))
print("violets are {}".format(violet.color))
print(this_pun_is_for_you)