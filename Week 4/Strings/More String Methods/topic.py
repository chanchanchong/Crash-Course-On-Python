# We said earlier that we had a lot of new exciting concepts coming up. Well, I'm
# not going to string you along anymore. We're going to tie up our lessons on
# strings with a bunch of fun methods for transforming our string text. I know, I
# know, my jokes are pretty terrible, so let's get back to the good stuff. So far, we've
# seen ways you can access portions of strings using the indexing technique, create
# new strings by slicing and concatenating, find characters and strings using the
# index method, and even test if one string contains another. On top of all this
# string processing power, the string class provides a bunch of other methods for
# working with text. Now, we'll show you how to use some of these methods.
# Remember, the goal is not for you to memorize all of this. Instead, we want to
# give you an idea of what you can do with strings in Python. Some string methods
# let you perform transformations or formatting on the string text, like upper and
# it's opposite, lower. These methods are really useful when you're handling user
# input. Let's say you wanted to check if the user answered yes to a question. How
# would you know if the user typed it using upper or lower case? You don't need to,
# you just transform the answer to the case you want. Like this example.

# Another useful method when dealing with user input is the strip method. This
# method will get rid of surrounding spaces in the string. If we ask the user for an
# answer, we usually don't care about any surrounding spaces. So it's a good idea
# to use the strip method to get rid of any white space. This means that strip
# doesn't just remove spaces, it also removes tabs and new line characters, which
# are all characters we don't usually want in user-provided strings. There are two
# more versions of this method, lstrip rstrip, to get rid of the whitespace characters
# just to the left or to the right of the string instead of both sides.

# Other methods give you information about the string itself. The method count
# returns how many times a given substring appears within a string.

# The method endswith returns whether the string ends with a certain substring.

# The method isnumeric returns whether the string's made up of just numbers.
# Adding to that, if we have a string is numeric, we can use the int function to
# convert it to an actual number.

# In earlier videos, we showed that we can concatenate strings using the plus sign.
# The join method can be also be used for concatenating.

# To use the join method, we have to call it on the string that'll be used for joining.
# In this case, we're using a string with a space in it. The method receives a list of
# strings and returns one string with each of the strings joined by the initial string.
# Let's check out another example.

# Finally, we can also split a string into a list of strings.

# The split method returns a list of all the words in the initial string and it
# automatically splits by any whitespace. It can optionally take a parameter and
# split the strings by another character, like a comma or a dot. Are you starting to
# see how these string methods could be useful in your IT job?

# Okay, so we've just learned a bunch of new methods. But there are tons more
# that you can use on strings. We've included a list with the ones we talked about,
# and some new ones in the next cheat sheet. You'll also find a link to the full
# Python documentation there, which gives you all the info on the each available
# method. As we've said before, don't worry about trying to memorize everything.
# You'll pick these concepts up with practice, and the documentation is alwasy
# there if you need it. All right, last up in our string of string videos, we're going to
# check out how to format strings.


# Want to try some string methods yourself? Give it a go!

# Fill in the gaps in the the initials function so that it returns the initials of the words
# contained in the phrase received. in the upper case. For example: "Universal Serial Bus"
# should return "USB"; "local area network" should return "LAN".
"Mountain".lower()
# mountain
"Mountain".upper()
# MOUNTAIN
answer = "Yes"
if answer.lower() == "yes":
    print("Use said yes")
# User said yes

" yes ".strip()
# 'yes'

" yes ".lstrip()
# 'yes '
' yes '.rstrip()
# ' yes'

"The number of times e occurs in this string is 4".count("e")
# 4

"Forest".endswith("rest")
# True

"Forest".isnumeric()
# False

"12345".isnumeric()
# True

int("12345") + int("12345")
# 66666

" ".join(["This", "is", "a", "phrase", "joined", "by", "spaces"])
# 'this is a phrase joined by spaces'
"...".join(["This", "is", "a", "phrase", "joined", "by", "spaces"])
# 'This...is...a...phrase...joined...by...spaces

"This is another example".split()
# ["This", "is", "another", "example"]
def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0]
    return result.upper()

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network"))  # Should be: LAN
print(initials("Operating system"))  # Should be: OS