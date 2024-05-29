class MyContextManager:
    def __init__(self, filepath) -> None:
        self.filepath = filepath

    def __enter__(self):
        self.file  = open(self.filepath, 'r')
        print("calling __enter__")
        return self.file
    
    def __exit__ (self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        print("calling __exit__")


    
with MyContextManager('./00_assert.py') as f:
    print(f.readline())