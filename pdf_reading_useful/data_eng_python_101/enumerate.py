l = [1,2,3,4,5,6,7]

for x,y in enumerate(l):
    print(f"{x} - {y}")

# convert enumerate to list to add indexes (list of tuples)
print(list(enumerate(l)))
