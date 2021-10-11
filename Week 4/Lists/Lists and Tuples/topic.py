# As we called out before, there are a number of data types in Python that are all
# sequences. Strings are sequences of characters and are immutable. Lists are sequences
# of elements of any type and are mutable. A third data type that's a sequence and also
# closely related to lists is the tuple. Tuples are sequences of elements of any type that
# are immutable. We write tuples in parentheses instead of square brackets.

# Strings
# Sequences of characters, and are immutable.

# Lists
# Sequences of elements of any type, and are mutable.

# Tuples
# Sequences of elements of any type, that are immutable.

fullname = ('Grace', 'M', 'Hopper')

# The position of the element inside the tuples have meaning.

# You might be wondering, why do we even need another sequence type? Weren't lists
# great? Yes, lists are great. They can hold any number of elements and we can add,
# remove and modify their contents as much as we want, but there are cases when we
# want to make sure an element in a certain position or index refers to one specific thing
# and won't change. In these situations, lists won't help us. Thanks for nothing lists. In
# our example, we have a tuple that represents someone's full name. The first element of
# the tuple is the first-name. The second element is the middle initial, and the third
# element is the last-name. If we add another element somewhere in there, what would
# that element represent? It would just be confusing and our code wouldn't know what to
# do with it, and that's why modifying isn't allowed. In other words, when using tuples
# the position of the elements inside the tuple have meaning. Tuples are used for lots of
# different things in Python. One common example is the return value of functions. when
# a function returns more than one value, it's actually returning a tuple. Remember the
# function to convert seconds to hours, minutes, and seconds that we saw a while back?
# Here just to remind you. This function returns three values. In other words, it returns a
# tuple of three elements. Let's give it a try

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

result = convert_seconds(5000)

print(type(result))
# <class 'tuple'>
print(result)
# (1, 23, 20)


# We see the result is a tuple. What if we print it? We see that it has the three elements we
# expect it to have. Remember, since this is a tuple, the order matters. The first element
# represents the hours, the second one represents the minutes, and the third represents
# the seconds. One interesting thing we can do with tuples is unpack them. This means
# that we can turn a tuple of three elements into three separate variables. Because the
# order won't change, we know what those variables are present like this.

hours, minutes, seconds = result
print(hours, minutes, seconds)
# 1 23 20

# So now we've split the tuple into three separate values. We've seen before that we can
# also do this directly when calling the function without the intermediate result variable.

hours, minutes, seconds = convert_seconds(1000)
print(hours, minutes, seconds)
# 0 16 40

# In Python, it's really common to use tuples to represent data that has more than one
# value and that needs to be kept together. For example, you could use a tuple to have a
# filename and it's size, or you could store the name and email address of a person, or a
# date and time and the general health of the system at any point in time. Can you see
# how these different data types could help you automate some of your IT work? Pretty
# cool, right? Knowing when to use tuples and when to use lists can seem a little fuzzy at
# first, but don't worry, it'll get clearer as we tackle more examples.



# Let's use tuples to store information about a file: its name, its type and
# its size in bytes. Fill in the gaps in this code to return the size in
# kilobytes (a kilobyte is 1024 bytes) up to decimal places.

def file_size(file_info):
    name, type, size = file_info
    return ("{:.2f}".format(size / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21

