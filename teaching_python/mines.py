"""
Dwarven Mines
-------------

An ancient dwarven chant goes like this:

    gold gold gold gold
    gold gold gold gold
    gold gold gold gold
    mine mine mine mine

Although the richness of the dwarven language suffered a bit from the translation
(they have at least 27 words for the shiny metal),
the meaning of the last verse is clear. It refers to:

    1. the place
    2. what the dwarf does there
    3. the owner
    4. the security measures

Let's take a closer look at a map of the mines.
"""

import numpy as np

# create a dwarven mine
mines = np.random.choice([' ', '*'], size=(10, 10), p=[0.7, 0.3])
print(mines)

# count the total number of mines
mine_present = mines == '*'
print(mine_present)
print(mine_present.sum())

# to be safe, we need to know how many mines
# are neighboring any given spot
neighbors = mines[2:5, 2:5]
print(neighbors)

# for all positions
count = np.zeros(mines.shape, np.uint8)

count[1:, 1:] += mine_present[:-1, :-1]
count[1:, :] += mine_present[:-1, :]
count[1:, :-1] += mine_present[:-1, 1:]
count[:, 1:] += mine_present[:, :-1]
count[:, :-1] += mine_present[:, 1:]
count[:-1, 1:] += mine_present[1:, :-1]
count[:-1, :] += mine_present[1:, :]
count[:-1, :-1] += mine_present[1:, 1:]

print(count)

# add count to the map of the mine
nomines = mines != '*'
mines[nomines] = count[nomines].astype(str)
print(mines)

# now it is safe to start mining!
