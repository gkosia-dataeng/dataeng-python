'''
    zip: receive a number of lists
         match the elements on the same position and return an iterator of tuples
'''
a = ["a", "b", "c", "d"]
b = ["1", "2", "3"]
c = ["1a", "2b", "3c"]


for a,b,c in zip(a,b,c):
    print(a,b,c)