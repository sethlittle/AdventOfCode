'''
The five types of rocks have the following peculiar shapes, where # is rock and . is empty space:

####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##

input is the jet pattern
>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>
'''

#(x, y)
pieces = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)],
    [(0, 2), (1, 2), (2, 2), (2, 1), (2, 0)],
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (0, 1), (1, 0), (1, 1)]
]
widths = [4, 3, 3, 1, 2]
heights = [1, 3, 3, 4, 2]

def solve(num_pieces):
    i = 0
    while i < num_pieces:
        piece = i % 5
        height = heights[piece]
        width = widths[piece]
        parts = pieces[piece]

print("Part One Answer:", solve(2022))