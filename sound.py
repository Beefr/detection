import pysine


class Sound(object):

    def __init__(self):
        frequency = 30000

        duration = 3


    def play(self):
        pysine.sine(frequency, duration)

