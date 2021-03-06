import array
from math import floor

sum = 0
file = open("ItsNicoleKing-aoc-19/inputs/input_day1.txt", "r")

# part 1
# for line in file:
#   sum = sum + floor(int(line) / 3) - 2

# print("part 1: " + str(sum))


# part 2
def lineSum(mass):
  fuel = (floor(mass / 3) - 2)
  if fuel <= 0:
    return 0
  return fuel + lineSum(fuel)

for line in file:
  sum += lineSum(int(line))

print("part 2: " + str(sum))
