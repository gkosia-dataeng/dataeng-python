def foo(reuired, *args, **kwargs):
    print("Starting foo instance of execution...")
    print(reuired)

    '''
        args becasue is * will create positional arguments as a tuple
    '''
    if args:
        print(args)

        # we can modify the args and forwart them to next function
        new_args = args + (2,)
        zoo(new_args)
    '''
        kwargs becasue is ** will create keyword arguments as a dictioinary
        Canot have positional arguments after keyword arguments
    '''
    if kwargs:
        print(kwargs)
        # we can append kwarg and forward it to he next function
        kwargs['new_kwarg'] = "i am a kwarg from foo"
        zoo(kwargs)




def zoo(*args, **kwargs):
    print("Starting zoo instance of execution...")
    if args:
        print(args)

    if kwargs:
        print(kwargs)


foo(1)

foo(1,2,3)

foo(1,k=11, z=12)

foo(1,2,k=11, z=12)