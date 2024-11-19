import itertools
import random

iter_zeros_ones = itertools.cycle([0, 1])

iter_days = itertools.cycle(range(7))

iter_random = (random.choice(["N", "E", "S", "W"]) for _ in iter(int, 1))

print("Test (0, 1, 0, 1, ...):")
print([next(iter_zeros_ones) for _ in range(10)])

print("\nTest (0, 1, 2, ..., 6, 0, ...):")
print([next(iter_days) for _ in range(15)])

print("\nTest (random directions N, E, S, W):")
print([next(iter_random) for _ in range(10)])