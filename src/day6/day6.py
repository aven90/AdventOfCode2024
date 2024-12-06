"""
We have to check the patrol route of a guard

arrows: ^ < > v indicate the way the guard is facing
#:  indicates objects

The guards follow a strict protocol:
If there is something directly in front of you, turn right 90 degrees.

Otherwise, take a step forward.

example map:
....#.....
....^....#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#...

every place the guard has visited (including starting) changes to X, marking it is part of the path
....#.....
....XXXXX#
....X...X.
..#.X...X.
..XXXXX#X.
..X.X.X.X.
.#XXXXXXX.
.XXXXXXX#.
#XXXXXXX..
......#X..
"""


# Part 1
"""
Assignment:  sum of all places in the path of the guard (sum of X) before leaving the place

Flow:
- import data as list of lists
- Determine starting position and direction
    postion (row, col)

Move the guard:
    ^ row - 1
    > col + 1
    v row + 1
    < col -1

if next_val != '#'
    replace next val with direction
    replace current with X
else:
    replace current with new direction

"""




