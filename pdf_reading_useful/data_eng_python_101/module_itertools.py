from itertools import cycle

colors = ['r', 'g', 'b']

# infinite loop over a list
colors_itr = cycle(colors)

for i in range(10):
    print(next(colors_itr))

