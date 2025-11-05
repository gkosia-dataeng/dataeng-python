from contextlib import contextmanager


@contextmanager
def manage_file(filepath):
    try:
        f = open(filepath, 'r')
        print("opening file..")
        yield f
    finally:
        f.close()
        print("closing file..")


with manage_file('./00_assert.py') as file:
    print(file.readline())
