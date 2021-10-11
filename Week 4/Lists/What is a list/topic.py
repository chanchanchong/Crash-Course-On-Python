# As you know by now, Python comes with a lot of ready-to-use data types. We've seen
# integers, floats, Boolean, and strings in detail. But those data types can only tke you
# so far. Eventually in your scripts, you want to develop code that manipulates collections
# of items like a list of strings representing all the file names in a directory or a list of
# integers representing the size of network packets. This is where the list data type comes
# in handy. You can think of lists as long boxes with the space inside the box divided up
# into different slots. Each slot can contain a different value. Like we mentioned earlier
# when we first came across the list, in Python, we use square brackets to indicate where
# the list starts and ends. Let's check out an example.

x = ['Now', 'we', 'are', 'cooking!']
print(type(x))
# <class 'list'>
print(x)
# ['Now', 'we, 'are', 'cooking!']
print(len(x))
# 4


# Here, we've created a new variable called x and set its contents to be a list of strings. We
# can check the type of x using the type function we saw a little while ago. Nice, Python
# tells us this is a list. In the same way, we've done with other variables, we can show the
# contents of the whole list using the print function. The length of the list is how many
# elements it has. To get that value, we'll use the same len function we used for strings.
# That's right. Out list has four elements. When calling Len for the list, it doesn't matter
# how long each string is on its own. What matters is how many elements the list has. To
# check if a list contains a certain element, you can use the keyword "in" like in these
# examples.

print("are" in x)
# True
print('Today' in x)
# False

# Again, like when we use this with strings, the result of this check is a Boolean, which we
# can use as a condition for branching or looping. We can also use indexing to access
# individual elements depending on their position in the list. To do that, we use the
# tells us this is a list. In the same way, we've done with other variables, we can show the
# contents of the whole list using the print function. The length of the list is how many
# element it has. To get that value, we'll use the same len function we used for strings.
# That's right. Our list has four elements. When calling Len for the list, it doesn't matter
# how long each string is on its own. What matters is how many elements the list has. To
# check if a list contains a certain element, you can use the keyword "in" like in these
# examples.

print(x[0])
# Now
print(x[3])
# cooking!

# Again, like when we use this with strings, the result of this check is a Boolean, which we
# can use as a condition for branching or looping. We can also use indexing to access
# individual elements depending on their position in the list. To do that, we use the
# square brackets and the index we want to access, exactly like we did with strings.
# Remember that the first element is given the index zero. This means the last index of
# the list will be the length of the list minus one. What happens if we try to access an
# element after the end of the list?

# print(x[4])
# IndexError: list index out of range
print(x[1:3])
# ['we, 'are']
print(x[:2])
# ['Now', 'we']
print(x[2:])
# ['are', 'cooking!']

# You might have seen this coming. We get an index error. We can't go over the end of the
# list. Remember that because list indexes start at zero, accessing the item at index four
# means we're trying to access the fifth element in the list. There are only four elements.
# So we're out of range if we try to access the index number four. Does this seem a bit
# confusing? If it does, this visualization might help you out. As you can see, index four
# doesn't point at anything since there's no slot four in our list. As with strings, we can
# also use indexes to create a slice of the list. For this, we use ranges of two numbers
# separated by a colon. Again, the second element isn't included in the slice. So the range
# goes to the second index minus one. Here, we start at index one and go up to one less
# than three, which is two. We can also leve out one of the range indexes empty. The
# first value defaults to zero and the second value to the length of the list. Makes sense? If
# all this sounds really familiar to what we said about strings, then this course is working
# as intended. That's because strings and lists are very similar data types. In Python,
# strings and lists are both examples of sequences. There are other sequences too, and
# they all share a bunch of operations like iterating over them using for-loops, indexing
# using the len function to know the length of the sequence, using plus to concatenate
# two sequences and using in to verify if the sequence contains an element. So this i s
# great news. While understanding indexing is hard, once you know it for one data type,
# you've pretty much mastered it for every data type. So you actually know way more
# than you thought. Wow, now, we're really cooking. Next up, we're going to look at some
# more list operations. This time, actually specific to lists.

# Using the "split" string method from the preceding lesson, complete the get_word
# function to return the {n}th word from a passed sentence. For example, get_word(
# "This is a lesson about list", 4) should return "lesson", which is the 4th word
# in this sentence. Hint: remember that list indexes start at 0, not 1.
def get_word(sentence, n):
    # Only proceed if n is positive
    if n > 0:
        words = sentence.split()
        # Only proceed if n is not more than the number of words
        if n <= len(words):
            return words[n - 1]
    return("")

print(get_word("This is a lesson about lists", 4)) # Should print: lesson
print(get_word("This is a lesson about lists", -4)) # Nothing
print(get_word("Now we are cooking!", 1)) # Should print: Now
print(get_word("Now we are cooking!", 5)) # Nothing
