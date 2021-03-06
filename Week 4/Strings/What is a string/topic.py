# By now, we've used strings in a lot of examples, but we haven't spend
# time looking at them in detail yet. Before we dive into the nitty-gritty
# though, let's go over what we've seen so far and add a few more
# points. First, a quick refresher. A string is a data type in Python that's
# used to represent a piece of text. It's written between quotes, either
# double quotes or single quotes, your choice. It doesn't matter which
# type of quotes you use as long they match. If we mix up double and
# single quotes, Python won't be too happy, and it'll return a syntax
# error, telling us it couldn't find the end of the string. A string can be as
# short as zero characters, usually called an empty string or really long.
# We also learned that we can use strings to build longer strings using
# the plus sign and action called concatenating. A less common
# operation is to multiply the string by a number, which multiplies the
# content of the string that many times like this. If we want to know how
# long a string is, we can use the len function which we saw in earlier
# videos. The len function tells us the number of characters contained in
# the string. We can use strings to represent a lot of different things.
# They can hold a username, the name of a machine, an email address,
# the name of a file, and any other text. A lot of the data that we'll
# interact with will be stored in strings, so it's important to know how to
# use them. There are tons of things we could do with strings in our
# scripts. For example, we can check if files are named a certain way by
# looking at the filename and seeing if they match our criteria, or we can
# create a list of emails by checking out the users of our system and
# concatenating our domain. I recently wrote a script that worked with a
# bunch of files and took different actions according to the name of each
# file. So the file ended in a certain extension say, .TXT, then my script
# would print it. If the file had a certain string and the name, say. test,
# then my script would ignore it and move on to the next thing and so
# on. The contents of a text file are also strings. A few months ago, I had
# to change the default values for a bunch of configuration options from
# true to false. So I wrote a function that would find the string true in a
# file and replace it with false. You can probably think of more examples
# where your code needs to handle strings, but to use strings effectively,
# we need to know what options are available to us in Python. In the next
# few videos, we'll cover some of the operations we can perform over
# strings, including how to access parts of them and modify them.

# Modify the double_word function so that it returns the same word repeated twice ,
# followed by the length of the new doubled word. For example, double_word("hello")
# should return hellohello10.

def double_word(word):
    return word * 2 + str(len(word * 2))


print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0