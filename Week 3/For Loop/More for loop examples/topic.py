# More for loop examples

# In the last video, we talked about the range function, and how ot
# generates a sequence of numbers starting with zero. Sometimes,
# though, we don't want to start with zero. For these situations, the
# range function also allows us to specify the first element of the list to
# generate. We do that by passing two parameters to the function
# instead of one, like in the next example. Product equals 1 for n in range
# calculating the products of all numbers from 1 to 10. For this operation,
# it's important  that we start with one and not with zero. If we'd started
# with zero, the whole product would be zero. Additionally, we can
# specify a third parameter to change the size of each step. This means
# that instead of going oen by one, we could have a larger difference
# between the elements. Let's check out this example when you might
# want to do something like this. First, we're defining a function that
# converts a temperature value from Fahrenheit to Celsius, and we're
# simply using a conversion formula to do that. Then we have a for loop
# that starts at zero, and goes up to 100 in steps of 10. Notice that we're
# using 101 for the upper limit instead of 100. We're doing this because
# the range never includes the last element, and we want to include 100
# in our range. The body of the for-loop prints the value in Fahrenheit
# and the value in Celsius creating a conversion table. Let's see this in
# action.

# That example got you feeling the heat. Don't worry, there's a quick
# rundown of what we've learned. The range function can receive one,
# two or three paramaters. If it receives one parameter, it will create a
# sequence one by one from zero until one less than the parameter
# received. If it receives two parameters, it will create a sequence one by
# one from the first parameter until one less than the second parameter.
# Finally, if it receives three parameters, it will create a sequence starting
# from the first number and moving towards the second number. But
# this time, the jumps between the numbers will be the size of the third
# number, and again. it will stop before the second number. Sound like a
# lot to remember, but don't panic. As we've said before, you don't have
# to try to memorize it all, just keep practicing. It'll soon become second
# nature. To help you practice, we've included all of this in a handy cheat
# sheet to refer to whenever you need it. You'll find that in the next
# reading.

# In math, the factorial of a number is defined as the product of an integer
# and all the integers below it. For example, the factorial of four (4!) is
# equal to 1*2*3*4 = 24. Fill in the blanks to make the factorial function
# return the right number.

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(4))  # should return 24
print(factorial(5))  # should return 120