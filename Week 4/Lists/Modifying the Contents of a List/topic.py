# One of the ways that lists and strings are different is that lists are mutable. Which is
# another fancy word to say that they can change. This means we can add, remove, or
# modify elements in a list. Let's go back to our example of thinking of a list as a long box.
# Changing the list means we keep the same box and we add, remove, or change the
# elements inside that box. We'll now go through the methods that let us modify the list
# one by one. If all these details seem a little overwhelming, that's okay. As usual, there
# will be a cheat sheet at the end and you'll have lots of chances to practice each of these
# methods as we go along. You don't need to learn all those by heart, and of course you
# can always review anything that isn't clear. So don't worry, we got your back. We'll start
# with the simplest change; adding an element to a list using the append method. Let's
# check this out in the tastiest example yet.

# The append method adds a new element at the end of the list. It doesn't matter how
# long the list is. The element always get added to the end. You could start with an
# empty list and add all of its items using append. If you want to insert an element in a
# different position, instead of at the end, you can use the insert method.

fruits = ['Pineapple', 'Banana', 'Apple', 'Melon']
fruits.append('Kiwi')
print(fruits)
# ['Pineapple, 'Banana', 'Apple', 'Melon', 'Kiwi']
fruits.insert(0, "Orange")
print(fruits)
# ['Orange', 'Pineapple', 'Banana', 'Apple', 'Melon', 'Kiwi']

# The insert method takes an index as the first parameter and an element as the second
# parameter. It adds the element at the index in the list. To add it as the first element, we
# use the index zero and we can use any other number. What happens if we use a number
# larger than the length of the list?

fruits.insert(25, "Peach")
print(fruits)

# No errors. You can say that it even worked just peachy. If we use an index higher than
# the current length, the element just gets added to the end. You can pass any number to
# insert but usually, you either add at the beginning using insert at the zero index or at
# the end using append. We can also remove elements from the list. We can do it using
# the value of the element we want to remove. Can you guess what method we would
# use? You got it, use the remove method.


# ['Orange', 'Pineapple', 'Banana', 'Apple', 'Melon', 'Kiwi', 'Peach']
fruits.remove("Melon")
# ['Orange', 'Pineapple', 'Banana', 'Apple', 'Kiwi', 'Peach']

# The remove method removes from the list the first occurrence of the element we pass
# to it. What happens if the element is not in the list?

fruits.remove("Pear")
# ValueError: list.remove(x): x not in list

# That went pear-shaped. We got a value error, telling us the element isn't in the list.
# Another way we can remove elements is by using the pop method, which receives an
# index.

fruits.pop(3)
# 'Apple'
print(fruits)
# ['Orange', 'Pineapple, 'Banana', 'Kiwi', 'Peach']

# The pop method returns the element that was removed at the index that was passed. In
# the last way to modify the contents of a list is to change an item by assigning something
# else to that position, like this.

fruits[2] = "Strawberry"
print(fruits)
# ['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']

# Wow, the contents of ours fruits variable have changed a lot since we started this video.
# But it's always the same variable, the same box. We've just modified what's inside.
# Modifying the contents of lists will come up in tons of scripts as we operate with them. If
# the list contains hosts on a network, you could add or remove hosts as they come
# online or offline. If the list contains users authorized to run a certain process, you could
# add or remove users when permissions are granted or removed and so on. You've now
# seen a number of methods that let us modify the contents of a list, adding, removing,
# and changing the elements that are stored inside the list. Whenever you need to write a
# program that'll handle a variable amount of elements, you'll use a list. What if you need
# a sequence of a fixed amount of elements? That's coming up in our next video.


# The skip_elements function returns a list containing every other elements from a input
# list, starting with the first element. Complete this function to do that using the for
# loop to iterate through the input list.

def skip_elements(elements):
    # Initialize variables
    new_list = []
    i = 0

    # Iterate through the list
    for e in elements:
        # Does this element belong in the resulting list?
        if elements.index(e) % 2 == 0:
            # Add this element to the resulting list
            new_list.append(e)
        # Increment i
        i += 1

    return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []























