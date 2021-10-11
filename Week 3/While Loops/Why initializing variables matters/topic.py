# As we've called out earlier writing loops allows us to get our computer
# to do repetitive work for us. So this is one of the main benefit of writing scripts
# in IT is to save time by automating repetitive tasks, loops are super useful. So
# let's make sure you avoid some of the most common mistakes people make
# when writing loops. One of the most common errors is forgetting to initialize
# variables with the right value. We've all made this mistake when starting to
# code. Remember how in the earlier examples we initialized the variable
# two different things can happen the first possible outcome and the easiest to
# catch is that Python might raise an error telling us that we're using a variable
# we haven't defined, which looks like this. As we've done with other errors we've
# come across, we can look at the last line to understand what's going on. This
# error type is a name error and the message that comes after it says we're using
# an undefined variable. It's straightforward to fix, we just need to initialize the
# variable before using it like this,

while my_variable < 10:
    print("Hello")
    my_variable += 1

my_variable = 5
while my_variable < 10:
    print("Hello")
    my_variable += 1


# Fixed. Now, there's second issue we might face if we forget to initialize
# variables with the right value. We might have already used the variable in our
# program. In this case, if we reuse the variable without setting the correct value
# from the start, it will still have the value from before. This can lead to some
# pretty unexpected behavior.

x =  1
sum = 0
while x < 10:
    sum += x
    x += 1

product = 1
while x < 10:
    product = product * x
    x += 1
print(sum, product)

# Check out the script, can you spot the problem? In
# the first block, we correctly initialize x to 1 and sum to 0 and then iterate until x
# equals 10 summing up all the values in between. So by the end of that block,
# sum equals the result of adding all the numbers from 1 to 10 and x is 10. In the
# second part of the code, the original intention was to get that we're initializing
# product but forgetting to initialize x. So x is still 10, this means that when the
# while condition gets checked, x is already 10 at the start of the iteration. The
# while condition is false before it even starts and the body never executes. Let's
# see how this problem would look.




# In this case, it might be harder to catch the problem because python doesn't
# raise an error. The problem here is that our product variable has the wrong
# value. If you have a loop that's gone rogue and not behaving as expected, it's a
# good idea to check if all the variables are correctly initialized. In this example,
# we need to set x back to 1 before starting the second loop. As always ,the best
# way to learn is to practice it yourself.

# Makes sense? Remember, if you ever feel stuck or a little unsure about
# something you can always ask for hep in the discussion forums. These forums
# are there to let you get the help you need when you need it, so don't forget to
# use them. So, to recap, whenever you're writing a loop check that you're
# initializing all the variables you want to use before you use them. And don't
# worry if you don't get it right the first time, we've all been there when learning
# how to code. As we've called out before, the way to master programming is to
# practice, practice, practice. Keep practicing until you're comfortable and even
# then it's still okay to make mistakes. So don't feel like you can't or loop back
# around to review and practice everything we've covered so far.


# In this code, there's n initialization problem that's causing our function to be
# behave incorrectly . Can you find the problem and fix it?

def count_down(start_number):
    current = start_number
    while current > 0:
        print(current)
        current -= 1
    print("Zero!")


count_down(3)
