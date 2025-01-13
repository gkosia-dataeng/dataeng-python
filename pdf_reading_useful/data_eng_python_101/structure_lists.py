#flatten a list of lists
l = [[1,2], [3,4], [5]]
print([i for sublist in l for i in sublist ])