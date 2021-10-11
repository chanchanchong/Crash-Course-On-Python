# In the last video, we saw a very simple example of a while loop.
# We looked at a basic syntax of the loop and how it works. Let's now apply
# this knowledge to a similar example, but this time with a while loop inside
# a function. Can you work out what this function does? In this example we
# start out by initializing a variable called x. In this case, we initialize it with a
# value of 1. Then, we enter our while loop which checks to see if the value
# inside of the x variable is less than the parameter n that the function
# received. If that comparison evaluates to true, then the code inside the
# while block is executed. Say we pass a value of 5 as a parameter to this
# function. In the first pass through the loop, x is always equal to 1, so the
# comparison 2 smaller than or equal to 5 would be true and we then enter
# the body of the loop. In the body, we first print a message indicating that
# the current attempt number and then we increase the value of x by 1. To
# increment the number we're using a slightly different expression thn
# before. x += 1 is a shorthand version of x = x + 1. You can use either
# expression since they both mean the same thing. The process continues
# until the result of the comparison isn't true anymore, which happens when
# x is bigger than n. In our current example, this would be when the value fo
# x is 6. Let's see it in action.

# In these past examples, we've used the simple conditions of a number
# being smaller, or smaller or equal than another number. These are
# common conditions, but they're by no means the only conditions you can
# have in a while loop. It's common for example to call a separate function
# that evaluates the condition, like this. In this case, there's of lot of code
# hidden behind functions and it's doing stuff we don't see. There's a get
# username function that asks the user for a username and a
# valid_username function that validates that username. And all this is
# happening in just a handful of characters. As you can see, you can pack a
# lot of punch into just a short line of code. In this case, the body of the while
# loop will be executed until the user enters a valid username. The important
# thing to remember is that the condition used by the while loop needs to
# evaluate to true or false. It doesn't matter if this is done by using
# comparison operators or calling additional functions. The conditions used
# in while loops can also become more complex if we use the logical
# operators that we encountered when looking into branching, and, or, and
# not. This lets us combine the values of several expressions to get the result
# we want. Okay, we've now covered what a while loop is and learned its
# syntax and basic behavior. Some of this stuff can be a bit tricky and you're
# doing great, keep sticking with it. Next, we're going to do a rundown of
# some of the most common pitfalls that you may come across when writing
# your own loops. Head on over to the next video to get started.




# Can you work out what this function does? Try passing different parameters to the attemps
# function to see what it does.
def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")


attempts(5)