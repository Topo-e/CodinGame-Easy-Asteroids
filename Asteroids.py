import sys
import math
from collections import defaultdict

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

w, h, t1, t2, t3 = [int(i) for i in input().split()]
first_picture, second_picture = [], []
coordinates = defaultdict(list)

for i in range(h):
    first_picture_row, second_picture_row = input().split()
    first_picture.append(first_picture_row)
    second_picture.append(second_picture_row)

# We find each asteroids represented by different letters

list_letters = [i for i in ''.join(first_picture) if i.isalpha() ]


# We create an empty sky like a reference

empty_sky = [''.join(['.'] * w )] * h

# We find coordinates of asteroids in position at t1 and t2

for asteroid in sorted(list_letters, reverse = True):
    for picture in [first_picture, second_picture]:
        for row in range(w):
            for col in range(h):
                if picture[row][col] == asteroid:
                    coordinates[asteroid].append([row, col])

# We calculate new positions of each asteroids

for letter in coordinates.items():
    first_coordinate = math.floor(((letter[1][1][0] - letter[1][0][0]) / (t2 - t1)) * (t3 - t2))
    second_coordinate = math.floor(((letter[1][1][1] - letter[1][0][1]) / (t2 - t1)) * (t3 - t2))

    final_coordinate = letter[1][1][0] + first_coordinate, letter[1][1][1] + second_coordinate

    if final_coordinate[0] < 0 or final_coordinate[1] < 0 or final_coordinate[0] >= h or final_coordinate[1] >= h : pass
    else:
        # We want to replace the new position for each asteroids
        x = [i for i in empty_sky[final_coordinate[0]]]
        x[final_coordinate[1]] = letter[0]
        empty_sky[final_coordinate[0]] = ''.join(x)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

for i in empty_sky:
    print(i)
