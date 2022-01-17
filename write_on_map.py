from turtle import Turtle


class WriteOnMap:
    def __init__(self):
        self.states = []

    def write_new_state(self, x, y, name):
        writing = Turtle()
        writing.ht()
        writing.pu()
        writing.setpos(x, y)
        writing.write(name)
