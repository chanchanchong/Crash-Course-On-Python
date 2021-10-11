# When we first came across the for loop, we called out that we
# can iterate over a string character by character. But what if we want to
# access just a specific character or characters? We might want to do this,
# for example, if we have a text that's too long to display and we want to
# show just a portion of it. Or if we want to make an acronym by taking
# the first letter of each word in a phrase. We can do that through an
# operation called string indexing. This operation lets us access teh
# character in a given position or index using square brackets and teh
# number of the position we want. Like this. This might seem confusing
# at first, like Python is acting up. We're asking for the first character, and
# it's giving us the second. What gives Python? Well, what's happening
# here it that Python starts counting indexes from 0 not 1. Just like it
# does with the range function. So if we want the first character, we need
# to access the one at index. Knowing that indexes start at 0, which one
# do you think will be the last index in the string? It'll always be one less
# than the length of the string. In this case, our string has six characters,
# so the last index will be 5. Let's try it out.

# We see that the character in position five is the last character of the
# string. And if we try to access index six, we get an index error telling us
# that it's out of range. We can only go up to length minus 1. What if you
# want to print the last character of a string but you don't know how long
# it is? You can do that using negative indexes. Let's see that in a different
# example.

# In this example, we don't know the length of the string, but it doesn't
# matter. Using negative indexes lets us access the positions in the string
# starting from the last. Nice, right?

# On top of accessing individual characters, we can also access a slice of
# a string. A slice is the portion of a string that can contain more than
# one character, also sometimes called a substring. We do that by
# creating a range using a colon as a separator. Let's see an example of
# this.

# The range we use when accessing a slice of a string works just like the
# one created by the range function. It includes the first number, but
# goes up to one less than the last number. In this case, we start with
# indexed one the second letter of the string and go up to index three,
# the fourth letter of the string. Another option for the range is to include
# only one of the two indexes. In that case, it's assumed that the other
# index is either 0 for hte first value or the length of the string for the
# second value. Check this out.

# Accessing the slice from nothing to 4 takes the first four characters of
# the string, indexes 0 to 3. Accessing the slice from 4 to nothing takes
# everything from index four onward. All of this indexing might seem
# confusing at first. Don't worry, we all took time to wrap our heads
# around it. Just like all the challenges we've come across so far, the key
# is to keep practicing until you master it. And there are a bunch of
# exercises ahead to help you with that. Now that we know how to select,
# slice, access the parts of the string we want, we're going to learn
# how to modify them. That's coming up next.



# Want to give it a go yourself? Be my guest! Modify the first_and_last function
# so that it returns True if the first letter of the string is the same as the last
# letter of the string, False if they're different. Remember that you can access
# characters using message[0] or message[-1].
# Be careful how you handle the empty string, which should return True since nothing
# is equal to nothing.

def first_and_last(message):
    if message == "":
        return True
    return True if message[0] == message[-1] else False

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))