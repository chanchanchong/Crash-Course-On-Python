# We've seen how we can pass values into a function as parameters by
# passing values like the name or department in the example earlier. But
# what about getting values out of a function? This is where the concept of
# return values comes to play. The work that functions do can produce new
# results. Sure, we can print the results on the screen, but what if we wanted
# to use those results later in our script or didn't want to print them at all>
# We can do this by returning values from the functions we defined
# ourselves. Let's go back to calculating the area of a triangle. Do you
# remember our triangle example from our earlier exercise? The area of the
# triangle is calculated as base times height divided by 2. Imagine we need
# to calculate this value several times in our code. It would be useful to have
# a function that does this for us. Check out how this would look. We use the
# keyword return the tell Python that this is the return value of a function.
# When we call the function, we store that value in a variable. Let's say we
# have the two triangles and we want to add up the sum of both areas.
# Here's what we would do. First, we calculate the two areas separately.

# Then, we add the sum of both areas together. Finally, we print the result
# converting it to a string.

# As you can see in this example, the area of the triangle function returns a
# value which is not surprisingly the area of the triangle. We store that value
# in a different variable for each call to the function. In this case, area_a and
# area_b. Then we operate with those values adding them into the variable
# called sum and only printing this final result. This shows the power of the
# return statement. It allows us to combine calls to functions and to more
# complex operations which us to combine calls to functions and to more
# complex operations which makes your code more reusable. Return
# statements in Python are even more interesting because we can use them
# to return more than one value. Let's say you have a duration of time in
# seconds and you want to convert that to the equivalent number of ours,
# minutes, and seconds. Here's how to do that in Python. Did you spot the
# new operator in this function? That double slash operator is called floor
# division. A floor division divides a number and takes the integer part of the
# division as the result. For example, five slash slash two is two instead of
# 2.5. In our example, the first operation is calculating how many seconds
# remain after subtracting minutes. We end up with three numbers as a
# result. So the function returns all three of them. Let's see what this looks
# like when we're calling a function.

# Because we know that the function returns three values, we assign the
# result of the function to three different variables. There's one last thing we
# should call out about returning values. It is possible to return nothing and
# that's perfectly okay. Let's look at an example an earlier video. Here
# the function just printed a message and didn't return anything. What do
# you think would happen if we try to assign the value of this function to a
# variable? Let's try it out and see.

# Here when we call the function it printed a message just like we expected.
# We stored the return value in the result variable, but there was no return
# statement in the function. So the value of results is none. None is a very
# special data type in Python used to indicate that things are empty or that
# they return nothing. Wow, That was a lot to learn about functions and the
# return values. Remember that the key to getting this right is to practice
# writing the code you've just learned as many times as you need. Functions
# and return values can be tricky concepts to master, but they let us do a
# bunch of cool stuff. So put the time and effort into learning for some really
# valuable returns.



# Use the get_seconds function to work out the amount of seconds in 2 hours and 30 minutes,
# the add this number to the amount of seconds in 45 minutes and 15 seconds. Then print the result.

def get_seconds(hours, minutes, second):
    return 3600 * hours + 60 * minutes + second

# print(sum(amount_a, amount_b))
amount_a = get_seconds(2, 30, 0)
amount_b = get_seconds(0, 45, 15)
result = amount_a + amount_b
print(result)

