'''
    lambda are small anonimus functions
    lambda functions are restricted to single expressions (cannot use statements or annotations or return statement)
'''


added = lambda x, y: x+y

print(added(2,3))

''' Funcation expressions '''

print((lambda x,y: x+y)(3,4))