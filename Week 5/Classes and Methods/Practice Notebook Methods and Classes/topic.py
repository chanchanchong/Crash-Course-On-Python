# Practice Notebook: Methods and Classes
# The code below defines an Elevator class. The elevator has a current
# floor, it also has a top and bottom floor that are the minimum and
# maximum floors it can go to. Fill in the blanks to make the elevator go
# through the floors requested.

class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom = bottom
        self.top = top
        self.current = current
    def __str__(self):
        """Prints the current floor."""
        return "Current floor: {}".format(self.current)

    def up(self):
        """Makes the elevator go up one floor."""
        if self.top == self.current:
            return
        else:
            self.current += 1

    def down(self):
        """Makes the elevator go down one floor."""
        if self.bottom == self.current:
            return
        else:
            self.current -= 1

    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        self.current = floor


elevator = Elevator(-1, 10, 0)

# Go to the top floor. Try to go up, it should stay. Then go down.
elevator.go_to(10)
elevator.up()
elevator.down()
print(elevator)  # should be 9
# Go to the bottom floor. Try to go down, it should stay. Then go up.
elevator.go_to(-1)
elevator.down()
elevator.down()
elevator.up()
elevator.up()
print(elevator)  # should be 1
