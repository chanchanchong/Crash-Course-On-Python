# You're doing great getting your head around all these loops. I think
# you're ready for something a little bit more complex. We're going to
# explore what happens when you get loops inside of loops. Does that
# make your head spin? Don't worry, we're about to break it down for
# you with a couple of example. Have you ever played dominoes
# before? There's a bunch of fun games you can play with these tiles. In
# case you're not familiar, each Domino Tiles has two numbers
# represented by a collection of dots carved on each half of the tile. The
# numbers go from zero to six. Tiles can be rotated so that each
# combination of numbers is represented only once in a set of Domino
# Tiles. In other words, the two three tile is the same as the three two tile,
# and there's only one per set. Now, imagine we wanted to write a
# program that prints each Domino Tile in a set. If we take all of the tiles
# that have zero on the left, we can print tiles with numbers from zero to
# six on the right. That should be easy to do with a four loop. But what
# about tiles that have one on the left? Well, we need to skip the one zero
# tile, because that one was already printed as zero one. So we can print
# a list of tiles with one on the left and numbers one to six on the
# right. When we look at two, we would need to skip both zero and one,
# and s on. Are you following along? How you think we'd write the code
# for this? Turning this into code means that we'd need to write two for
# loops, one inside the other. This is what we call nested for loops. Check
# out how this looks on Python code. For left in range seven,

# for right in range left seven, print left bracket plus STR left plus pipe
# plus STR right plus close bracket end equals space, and print.

# In this code, we're using a new parameter that we passed to the print
# function. This parameter is called End. Normally, once print has taken
# the content we passed and written it to the screen, then it writes a
# special character that creates a new line called the newline character. If
# we want print to wrote something else instead of the newline character,
# we use the end parameter, like we see in this example. Notice how the
# second for loop iterates over a different number of elements each time
# it's called as the value of left changes. Depending on what you want to
# achieve with your nested loops, you may want both loops to always go
# through the same number of elements. Or you might want the second
# loop to connect to the first one. Let's look at a different example. Let's
# say you run a local girl's basketball league in your town. You have four
# teams that will play against each other in the league, both at home nd
# away. You've stored the names of the teams in a list, like this. We want
# to write a script that will output all possible team pairings. For this, the
# order of the names matters because for each game, the first name will
# be the home team and the second name is the away team. Of course,
# what we don't want to do is have a team playing against itself. So what
# statement do we need to use to avoid that? To do this, we need to use
# a conditional that makes sure we only print the pairing when the
# names are different. Check out what this looks like. For home team in
# teams, for away team in team.s If home team not equal to away team,
# print home team.

# versus away team. Success! As you can see, nested loops are super
# useful for solving certain problems, like pairing teams. What it doesn't
# solve is the question, who would win in a face-off between dragons and
# unicorns? If only there were some code for that. Anyway, we've seen
# that nested loops are a handy tool, but we need to be careful not to
# just blindly apply them to any problem. Why? Well, because the longer
# the list your code needs to iterate through, the longer it takes your
# computer to complete the task. Let's say your manager asks you to do
# an operation that will run through a list of 10,000 elements. If the
# operations takes one millisecond per element, the whole loop would
# take one millisecond times 10,00 to complete, which is 10 seconds.
# Now, imagine we add a nested loop that has to go over the same
# 10,000 elements. This means that each iteration of the outside loop
# would do a full iteration of the inside loop, which again, would take ten
# seconds to go through the whole list. So now, the whole iteration takes
# 10,00 times 10 seconds, which is a 100,00 seconds, that's over 27
# hours. I have the patience of a gnat, so that would definitely not work
# for me. This doesn't mean we shouldn't use nested loops. They are a
# useful tool when solving problems that require them, but we need to
# be careful of where and how we use them. Throughout this course,
# and one is coming up, we'll look at a lot of techniques that can help us
# pick the right tool to use for each type of problem. Up next, we'll look
# into some common errors that you might come across when writing
# your for loops and what to do about them.


for left in range(7):
    for right in range(left, 7):
        print("[", left, "+", right, "]", end=' ')
    print()

# Given the following code:
teams = ['Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team, "vs", away_team)