from enum import Enum, unique

@unique
class Notes(Enum):
    C = 1
    Db = 2
    D = 3
    Eb = 4
    E = 5
    F = 6
    Gb = 7
    G = 8
    Ab = 9
    A = 10
    Bb = 11
    B = 12

    def __add__(self, other):
        sum_ = self.value + other

        if sum_ > 12:
            sum_ = (sum_ % 12)

        return Notes(sum_)