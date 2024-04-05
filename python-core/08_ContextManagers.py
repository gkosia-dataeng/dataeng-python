# To handle the context management, we are implementing the __enter__ and __exit__ methods of class

class ContextManagerClass:
    def __enter__(self):
        print('Object created and i am doing something')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print('Exiting the context and i am doing something')




with ContextManagerClass() as cm:
    print("Doing something with the object")