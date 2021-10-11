# In the last video, we saw how to access certain characters
# inside a string. Now, what if we wanted to change them? Imagine you
# have a string with a character that's wrong and you want to fix it, like
# this one. Taking into account what you learned about string indexing,
# you might be tempted to fix it by accessing the corresponding index
# and changing the character. Let's see what happens if we try that.

# These pesky type errors, right? In this case, we're told that strings don't
# support item assignment. This means that we can't change individual
# characters because strings in Python are immutable, which is just a
# fancy word, meaning they can't be modified. What we can do is create
# a new string based on the old one, like this.

# Nice, we fixed the typo. But does this mean the message variable can
# never change? Not really. We can assign a new value to the same
# variable. Let's do that a couple of times to see how it works.

# What we're doing here, is giving the message variable a whole new
# value. We're not changing the underlying string that was assigned to it
# before. We're assigning a whole new string with different content. If
# this seems a bit complex, that's okay. You don't need to worry about
# this right now. We'll call this out whenever it's relevant for the
# programmer writing. So, we figured out how to create a new message
# from the old one. But how are we supposed to know which character
# to change? Let's try something different.

# In this case, we're using a method to get the index of a certain
# character. A method is a function associated with a specific class. We';;
# talk a lot more about classes and methods later. For now, what you
# need to know is that this is a function that applies to a variable. And we
# can call it by following the variable with a dot. Let's try this a few more
# times.

# So the index method returns the index of the given substring, inside
# the string. The substring that we pass, can be as long or as short as we
# want. What if there's more than one of the substring?

# Here, we know there are two s characters, but we only get one value.
# That's because the index method returns just the first position that
# matches. And what happens if the string doesn't have the substring
# we're looking for?



message = "A kong string with a silly typo"
message[2] = "l"
new_message = message[0:2] +  "l" + message[3:]

message = "This is another message"
message = "Another message"

pets = "Cats & Dogs"
pets.index("&")

pets.index('C')
pets.index("Dogs")

pets.index("s")

pets.index("x")  # ValueError

"Dragons" in pets
"Cats" in pets


def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email

# Try using the index method yourself now!

# Using the index method, find out the position of "x" in "supercalifragilisticexpialidocious".
word = "supercalifragilisticexpialidocious"
print(word.index("x"))