# You may remember by now that while loops use the condition to check when
# to exit. The body of the while loop needs to make sure that the condition begin
# checked will change. If it doesn't change, the loop may never finish and we get
# what's called an infinite loop, a loop that keeps executing and never stops.
# Check out this example. It uses the modulo operator that we saw a while back.
# This cycle will finish for positive and negative values of x. But what would
# happen if x was zero? The remainder of 0 divided by 2 is 0, so the condition
# would be true. The result of dividing 0 by 2 would also be zero, so the value of
# x wouldn't change. This loop would go on for ever, and so we'd get an infinite
# loop. If our code was called with x having the value of zero, the computer
# would just waster resources doing a division that would never lead to the loop
# stopping. The program would be stuck in an infinite loop circling background
# endlessly, and we don't want that. All that looping might make your computer
# dizzy. To avoid this, we need to think about what needs to be different than zero.
# So we could nest this while loop inside an if statement just like this. With this
# approach, the while loop is executed only when x is not zero. Alternatively, we
# could add the condition directly to the loop using a logical operator like in this
# example. This makes sure we only enter the body of the loop for values of x
# that are both different than zero and even. Talking about infinite loop reminds
# me of one of the first times I used while loops myself. I wrote a script that
# emailed me as a way of verifying that the code worked, and while some
# condition was true, I forgot to exit the loop. Turns out those e-mails get sent
# faster than once per second. As you can imagine, I got about 500 e-mails
# before I realized what was going on. Infinitely grateful for that little lesson.
# When you're done laughing at my story, remember, when you're writing loops,
# it's a good idea to take a moment to consider the different values a variable
# can take. This helps you make sure your loop won't get stuck, If you see that
# your program is running forever without finishing, have a second look at your
# loops to check there's no infinite loop hiding somewhere in the code. While
# you need to watch out for infinite loops, they are not always a bad thing.
# Sometimes you actually want your program to execute continuously until
# some external condition is met. If you've used the ping utility on Linux or
# macOS system, or ping-t on a Windows system, you've seen an infinite loop in
# action. This tool will keep sending packets and printing the results to the
# terminal unless you send it the interrupt signal, usually pressing Ctrl+C. If you
# were looking at the program source code you'll see that it uses an infinite loop
# to do hits with a block of code with instructions to keep sending the packets
# forever. One thing to call out is it should always be possible to break the loop
# by sending a certain signal. In the ping example, that signal is the user pressing
# Ctrl+C. In other cases, it could be that the user pressed the button on a
# graphical application, or that another program sent a specific signal, or even
# that a time limit was reached. In your code, you could have an infinite loop that
# looks something like this. In Python, we use the break keyword which you can
# see here to signal that the current loop should stop running. We can use it not
# only to stop infinite loops but also to stop a loop early if the code has already
# achieved what's needed. So quick refresh. How do you avoid the most
# common pitfalls when writing while loops? First, remember to initialize your
# variables, and second, check that your loops won't run forever. Wow, All this
# talk of loops is making me feel a little loopy. I'm going to have to go and lie
# down while you do the next practice quiz. Best of luck, and meet me over in
# the next video when you're done.

# The following code causes an infinite loop. Can you figure out what's missing
# and how to fix it?
def print_range(start, end):
    # Loop through the numbers from stand to end
    n = start
    while n <= end:
        print(n)
        n += 1


print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line)
