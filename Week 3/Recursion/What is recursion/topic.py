# Welcome back. How are you feeling after the last quiz? We're starting
# to learn some pretty cool things that we could do in our code. Who
# knew loops can be so fascinating? We've now discovered two looping
# techniques that we could use in Python: while loops and for loops. We
# use while when we want to do an operation repeatedly while a
# certain condition is true. We use for loops when we want to iterate over
# the elements of a sequence. Now, we're going to check out a third
# technique called recursion. But before we dive in, you may have
# noticed that this video is marked as optional. That's because while
# recursion is a very common technique used in software engineering,
# it's not used that much in automation. Still, we think it's valuable for
# you to know about recursion to have an idea of how to use it. You
# may see it in code written by others or you may face a problem where
# recursion is the best way to solve it. So while the next few videos are
# marked as optional and you won't be graded on their content, it's still
# super valuable stuff. Of course, feel free to skip them if you'd just
# rather focus on concepts you'll be graded on. Let's dive in. Recursion is
# the repeated application of the same procedure to a smaller problem.
# Have you ever played with a Russian nesting doll? They are a great
# visual example of recursion. Each doll has a smaller doll inside it. When
# you open up the doll to find the smaller one inside, you keep going
# until you reach the smallest doll which can't be opened. Recursion let's
# us tackle complex problems by reducing the program to a simpler one.
# Take our Russian nesting dolls, all nested inside each other. Imagine
# we want to find out how many dolls there are in total. We would need
# to open each doll one by one until we got to the last one and then
# count how many dolls we've opened. That's recursion in action. Here's
# another example with a more complex problem. Imagine you're in a
# line of people and you want to know how many people are in front of
# you, and let me tell you I can't stand long lines. Anyway, if the line is
# long, it might be hard to count the people without leaving the line and
# losing your place. Instead you can ask the person in front of you how
# many people are in front of them. Since this person will be in the same
# situation as you, they'll have to ask the same question to the person in
# front of them and so on and so on until the question reaches the first
# person in the line. This person can confidently reply that there are no
# people in front of them. Soo then the second person in line can reply
# one, the person behind them replies two, and so on until the answer
# reaches you. Okay, I know the chances are pretty small that all of those
# people would play along just so you can know where you are in line,
# but it's a useful way to visualize how recursion works. How does this
# translate into programming? Well, in programming, recursion is a way
# of doing a repetitive task by having a function call itself. A recursive
# function calls itself usually with a modified parameter until it reaches a
# specific condition. This condition is called the base case. In our earlier
# examples, the base case would be the smallest Russian doll or the
# person at the front of the queue. Let's check out an example of
# recursive function to understand what we're talking about. Here, we're
# defining a function called factorial. At the beginning of the function, we
# have a conditional block defining the base case, where n is smaller
# than 2. It simply returns the value 1. After the base case, we have a line
# where the factorial function is calling itself with n minus 1. This is called
# the recursive case. This creates a loop. Each time the function is
# executed, it calls itself with a smaller number until it reaches the base
# case. Once it reaches the base case, it returns the value 1. Then the
# previously called function multiplies that by two and the previously
# called function multiplies it by three and so on. This loop will keep
# going until the first factorial function called returns the desired result.
# It's a bit complex. Let's add a few print statements to see exactly how
# this works.

# So here we can see the function kept calling itself until it reached the
# base case. After that, each function returned the value of the previous
# function multiplied by n until the original function returned. Cool, huh?
# Next up, we're going to check out some more examples of when to use
# recursion and when it's best to avoid it.

def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n < 1:
        return 0

    # The recursive case is adding this number to
    # the sum of the numbers smaller than this one.
    return n + sum_positive_numbers(n - 1)

print(sum_positive_numbers(3))  # Should be 6
print(sum_positive_numbers(5))  # Should be 15