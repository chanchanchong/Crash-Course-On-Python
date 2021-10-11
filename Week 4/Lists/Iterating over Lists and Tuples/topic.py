# When we looked at for loops, we said they iterate over a sequence of elements. One of
# the examples we checked out was iterating over a list. Let's take a little trip to the zoo to
# see this in action. So we will make a list of animals, so animals equals, and since we're
# making a list, we'll start with a bracket, and we'll add lion, zebra, dolphin, and monkey
# and end the list with another bracket. Chars equals 0, and we'll start a loop: for animal
# in animals, two spaces, chars plus equals length of animals. Print total characters
# average length.format chars, chars length animals.

animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
chars = 0
for animal in animals:
    chars += len(animal)

print("Total characters: {}, Average length: {}".format(chars, chars / len(animals)))
# Total characters: 22, Average length: 5.5

# In this code, we're iterating over a list of strings. For each of the strings, we get its length
# and add it to the total amount of characters. At the end we print the total and the
# average which we get by dividing the total by the length of the list. You can see we're
# using the len function twice, once to get the length of the string and then again to get
# the amount of elements in the list. What if you wanted to know the index of an element
# while going through the list? You could use the range function and then use indexing to
# access the elements at the index that range returned. You could use a range function
# and then use indexing to access the elements at the index that range just returned or
# you could just use the enumerate function. Winners equals, we'll make a list, Ashley,
# Dylan, and Reese and close the list for index, person in enumerate winners

winners = ["Ashley", "Dylan", "Reese"]
for index, person in enumerate(winners):
    print("{} - {}".format(index + 1, person))

# 1 - Ashley
# 2 - Dylan
# 3 - Reese

# print curly brackets dash curly brackets.format index plus one person.

# The enumerate function returns a tuple for each element in the list. The first value in
# the tuple is the index of the element in the sequence. The second value in the tuple is
# the element in the sequence. You're the real winner with the enumerate function. It
# does all the work for you. Pretty useful, right? Let's use all of this now to solve a slightly
# more interesting problem. Say you have a list of tuples containing two strings each. The
# first string is an email address and the second is the full name of the person with that
# email address. You want to write a function that creates a new list containing one string
# per person including their name and the email address between angled brackets. the
# format usually used in emails like this. So what do we need to do?

# We'll start by defining a function that receives a list of people, def full_emails, takes the
# argument people.

def full_emails(people):  # people is a list of tuples
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result

# Remember, people is a list of tuples where the first element is the email address and
# the second one is the full name. So in our function, we'll first create the variable that
# we'll use as a return value which will be a list and we'll call it result. Result equals
# empty list. We'll then iterate over the list of people. We know this list contains tuples of
# two strings each. So we'll unpack the values directly when iterating in variables that
# we'll call email and name for email and name in people. Now, our result variable is a list
# and it should contain strings. So we'll append to the resulting string to the results list,
# result.append. The string that will append will be formatted in the way we want. To do
# that, we'll use the format method with the two variables of our iteration. So curly
# brackets, curly brackets.format, name, and email.

# Once we're done with the iteration, we'll return the list which should now contain all
# the necessary emails, return result.

print(full_emails([("alex@example.com", "Alex Diego"),
                   ("shay@example.com", "Shay Brandt")]))

# Will this work? What do you think? Let's try it out. Print full emails Alex@example.com,
# Alex Diego.

# Shay@example.com is the email and we'll cal Shay Brandt as the name.

# ['Alex Diego <alex@example.com>', 'Shay Brandt <shay@example.com>']

# Yes, this worked as expected. Before we move on, a quick word of caution about some
# common errors when dealing with lists in Python. Because we use the range function so
# much with for loops, you might be tempted to use it for iterating over indexes of a list
# and then to access the elements through indexing. You could be particularly inclined to
# do this if you're used to other programming languages before. Because in some
# languages, the only way to access an element of a list is by using indexes. Real talk, this
# works but looks ugly. It's more idiomatic in Python to iterate through the elements of
# the list directly or using enumerate when you need the indexes like we've done so far.
# There are some specific cases that do require us to iterate over the indexes, for
# example, when we're trying to modify the elements of the list we're iterating. By the
# way, if you're iterating through a list and you want to modify it at the same time, you
# need to be very careful. If you remove elements from the list while iterating, you're
# likely to end up with an unexpected result. In this case, it might be better to use a copy
# of the list instead. We've now seen a bunch of different things we can do with lists, and
# hopefully you're starting to see how they can be a very powerful tool in your IT
# specialist toolkit. Next up, we're going to learn a powerful technique for creating lists.


# Try out the enumerate function for yourself in this quick exercise. Complete the
# skip_elements function to return every other element from the list, this time
# using the enumerate function to check if an element is on even position
# or an odd position.

def skip_elements(elements):
    new_list = []
    for index, value in enumerate(elements):
        if index % 2 == 0:
            new_list.append(value)
    return new_list


print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))  # Should be ['a', 'c', 'e', 'g']
print(skip_elements(
    ['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))  # Should be ['Orange', 'Strawberry', 'Peach']
