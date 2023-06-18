from decimal import Decimal

class Frange:
    def __init__(self, start, stop=None, step=1.0):
        if stop is None:
            start, stop = Decimal('0.0'), Decimal(str(start))
        self.start = Decimal(str(start))
        self.stop = Decimal(str(stop))
        self.step = Decimal(str(step))

    def __iter__(self):
        return self

    def __next__(self):
        if self.step > 0 and self.start >= self.stop:
            raise StopIteration
        elif self.step < 0 and self.start <= self.stop:
            raise StopIteration
        else:
            value = self.start
            self.start += self.step
            return value


# Тести
assert (list(Frange(5)) == [0, 1, 2, 3, 4])
assert (list(Frange(2, 5)) == [2, 3, 4])
assert (list(Frange(2, 10, 2)) == [2, 4, 6, 8])
assert (list(Frange(10, 2, -2)) == [10, 8, 6, 4])
assert (list(Frange(2, 5.5, 1.5)) == [2, 3.5, 5])
assert (list(Frange(1, 5)) == [1, 2, 3, 4])
assert (list(Frange(0, 5)) == [0, 1, 2, 3, 4])
assert (list(Frange(0, 0)) == [])
assert (list(Frange(100, 0)) == [])

print('SUCCESS!')
