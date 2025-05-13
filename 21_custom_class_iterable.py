"""Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object
iterable in a for-loop, counting down to 0."""

class Countdown:
    def __init__(self, start):
        self.current = start  # Starting point of countdown

    def __iter__(self):
        return self  # Return the iterator object itself

    def __next__(self):
        if self.current < 0:
            raise StopIteration  # Stop when countdown goes below 0
        value = self.current
        self.current -= 1  # Go one step down
        return value

# Using the Countdown class in a for loop
for num in Countdown(8):
    print(num)
