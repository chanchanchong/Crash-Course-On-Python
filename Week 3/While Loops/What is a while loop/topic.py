# First off, we're going to talk about while loops. While loops
# instruct your computer to continuously execute your code based on the
# value of a condition. This works in a similar way to branching if statements.
# The difference here is that the body of the block can be executed multiple
# times instead of just once. Check out this program. Can you guess what it
# does? Before we execute it to find out, let's go through it together line by
# line. In the first line we're assigning the value of 0 to the variable x. We call
# this action initializing, to give an initial value to a variable. In the line after
# that, we're starting the while loop. We're setting a condition for this loop
# that x needs to be smaller than 5. Right now we know that x is 0 since
# we've just initialized it, so this condition is currently true. On the next two
# lines, we have a block that's indented to the right. Here, we cn use what
# we learned about functions and conditionals to identify that this is the
# while loop's body. There are two lines in the body of the loop. In the first
# line, we print a message followed by the current value of x. In the second
# line, we increment the value of x. We do this by adding 1 to its current
# value and assigning it back to x. So after the first execution of the body of
# the loop, x will be 1 instead of 0. Because this is a loop. the computer
# doesn't just continue executing with the next line in the script. Instead, it
# loops back around to re-evaluate the condition for the while loop. And
# because 1 here is still smaller than 5, it executes the body of the loop
# again. It then prints the message and once more increments x by 1. So the
# x is now 2. The computer will keep doing this until the condition isn't true
# anymore. In this example, the condition will be false when x is no longer
# smaller than 5. Once the condition is false, the loop finishes, and the next
# line is executed. And finally, the last line of our code prints the last value of
# x. So now that this code makes a bit more sense, what do you think will
# happen when we execute it? Ready to find out? Let's execute the code and
# see what happens.

# So we had five lines with the message. Not there yet, and then at the end
# of the script the value of x was 5. This was a simple example of how a while
# loop behaves. As we've said before, we're learning the building blocks of
# programming. Once you know those building blocks, you can combine
# them to create more complex expressions. As an IT specialist, while loops
# can be super helpful. You can use them to keep asking for a username if
# the one provided isn't valid, or maybe try an operation until it succeeds.
# Knowing how to construct these expressions can help you get your
# computer to do a whole lot with only a little bit of code. It's pretty powerful
# stuff we're learning here. Now that you've got an idea of how a while loop
# works, let's spice it up with another example.



x = 0
while x < 5:
    print("Not there yet, x=" + str(x))
    x = x + 1
print("x=" + str(x))