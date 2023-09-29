import pysine


class Sound(object):

    def __init__(self):
        self._frequency = 30000

        self._duration = 3


    def play(self):
        pysine.sine(self._frequency, self._duration)

