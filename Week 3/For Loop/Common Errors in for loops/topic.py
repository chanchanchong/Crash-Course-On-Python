# We've now seen how to write for loops, combine them with functions,
# nest a for loop inside a different loop, and even combine a nested loop
# with conditionals. Nice job, you're chugging right along. But before
# we're done with for loops, let's check out some common mistakes you
# may come across while trying this yourself. As we've called out are
# ready, for loops iterate over sequences. The interpreter will refuse to
# iterate over a single element. As you see here, for x in 25, print(x), in
# this example, we're trying to iterate over the number 25. Python prints
# a type error telling us that integers are not iterable. There are two
# solutions to this problem, depending on what we're trying to do. If we
# want to go from zero to 25, then we use the range function, so for x in
# range(25), print(x), but if we're trying to iterate over a list that has 25 as
# the only element, then it needs to be a list and that means writing it
# between square brackets, for x in

# list[25], print(x). You might be wondering why you'd ever want to
# iterate over a list of one element and that's a good question. Well, this
# kind of issue usually happens when you have a function with a for loop
# inside it, which is iterating over the elements of a list received by
# parameter. Say for example, you have a function that fixes the
# permissions of a list of files received by parameter, and you want to
# call this function to fix the permissions of just one specific file. To do
# that, you need to pass the file as the single element of a list. Let's check
# this out with some code we're familiar with, our friendliest of Python
# examples, hi, friends. We're going to modify it to have the greetings
# inside a function. We've defined a greet friends function, that receives a
# list by parameter and iterates over that list, greeting each friend. But
# what if we only want to greet one friend instead of four? Well, we still
# need to define a list, but with only one element. But first, let's see what
# would happen if we don't do that, greet_friends("Barry"),

# not what we expected, right? Well, what's going on here? This happens
# because strings are iterable, the for loop will go over each letter of the
# string and do the operation we asked it to do, which in this case, print a
# greeting. Depending on what you're trying to do, you may actually want
# to iterate through the letters of a string. But in this case, we don't. So to
# sum it up, if you get an error that a certain type isn't iterable, you need
# to make sure that for loop is using a sequence of elements and not just
# one, and if you find your code iterating through each letter of a string
# when you want it to do it for the whole string, you probably want to
# have that string be a part of a list. We've now learned how to write
# while loops and for loops. You might remember, for loops are best
# when you want to iterate over a known sequence of elements but
# when you want to operate while a certain condition is true, while loops
# are the best choice. Next up, we've got a super useful cheat sheet for
# you that puts all this into one handy resource. After that, head over to
# the practice quiz to test your knowledge and check in on how you're
# doing.

# The validate_users function is used by the system to check if a list of
# valid users is valid or invalid. A valid user is one that is at least
# 3 characters long. For example, ['taylor','luisa', 'jamaal'] are all valid
# users. When calling it like in this example, something is not right. Can
# you figure it out what to fix?

def validate_users(users):
    for user in users:
        if len(user) > 3:
            print(users + " is valid")
        else:
            print(users + " is invalid")

validate_users("purplecat")