# By now, you've seen what a recursive function looks like, how to write a
# base case and the recursive case. You might be wondering why do we
# need recursive functions if I can just use a for or while loop? Well,l
# solutions to some specific problems are easier to write and understand
# when using recursive functions. A lot of math functions like the
# factorial or the sum of all the previous numbers are good examples of
# this. If a math function is already defined in recursive terms, it's
# straightforward to just write the code as a recursive function. But it's
# not just about math functions. Let's check out a couple of examples of
# how this could help an IT specialist trying to automate tasks. Let's say
# that you need to write a tool that goes through a bunch of directories
# in your computer and calculates how many files are contained in each.
# When listing the files inside a directory, you might find subdirectories
# in your computer and calculates how many files are contained in each.
# When listing the files inside a directory, you might find subdirectories as
# well. This is a great time to use recursion. The base case would be a
# directory with no subdirectories. For this case, the function would just
# return the amount of files. The recursive case would be calling the
# recursive function for each of the contained subdirectories. The return
# value of a given function call would be the sum of all the files in that
# directory plus all the files in the contained subdirectories. A directory of
# files that can contain other directories is an example of a recursive
# structure. Because directories can contain subdirectories that contain
# subdirectories that contain subdirectories, and so on. When operating
# than for or while loops. Another IT-focused example of a recursive
# structure is anything that deals with groups of users that can contain
# other groups. We see this situation a lot when using administrative
# tools like active directory or LDAP. Say your group management
# software allows you to create groups that have both users and other
# groups as their members. And you want to list all human users that are
# part of a given group. Here you would use a recursive function to go
# through the groups. The base case would be a group that only includes
# users listing all of them. The recursive case would mean going through
# all the groups contained listing all the users in them and then listing
# any users contained in the current group.

# It's important to call out that in some languages there's a maximum
# amount of recursive calls you can ues. In Python by default, you can
# call a recursive function 1,000 times until you reach the limit. That's fine
# for things like subdirectories or user groups that aren't thousands of
# levels deep. But it might not be enough for mathematical functions like
# the ones we saw in the last video. Let's go back to our factorial example
# from the last video and try to call it with n equals 1,000.

# Factorial(1000), See that error? It's telling us that we've reached the
# maximum limit for recursive calls you can use. So while you can use recursion in a
# bunch of different scenarios, we only recommend using it when you need
# need to go through a recursive structure that wno't reach a thousand
# nested levels. All right, we've just added recursing to your growing
# scripting tool box. They're ready for you whenever the situation calls
# for it.


