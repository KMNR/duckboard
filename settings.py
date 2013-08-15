# DIMENSIONS AREN'T CHANGING ANY TIME SOON! NEITHER ARE THE COLORS.
COLORS = [
    ['black', 'black',],     # colors[0][0], colors[0][1]
    ['black', 'black',],
    ['black', 'black',],
    ['black', 'black',],
    ['black', 'black',],
    ['cyan', 'cyan',],
    ['cyan', 'cyan',],
    ['cyan', 'cyan',],
    ['cyan', 'cyan',],
    ['cyan', 'cyan',],
    ['yellow', 'yellow',],
    ['yellow', 'yellow',],
    ['yellow', 'yellow',],
    ['yellow', 'yellow',],
    ['yellow', 'yellow',],   # colors[14][0], colors[14][1]
]

KEYS = [
    ['q', 'w'],
    ['a', 's'],
    ['z', 'x'],
    ['e', 'r'],
    ['d', 'f'],
    ['c', 'v'],
    ['t', 'y'],
    ['g', 'h'],
    ['b', 'n'],
    ['u', 'i'],
    ['j', 'k'],
    ['m', ','],
    ['o', 'p'],
    ['l', ';'],
    ['.', '/'],
]


# DO NOT MODIFY BELOW THIS LINE.
ascii2coords = {}
rows = len(KEYS)
cols = len(KEYS[0])
for r in xrange(rows):
    for c in xrange(cols):
        ascii2coords[ord(KEYS[r][c])] = (r, c)

