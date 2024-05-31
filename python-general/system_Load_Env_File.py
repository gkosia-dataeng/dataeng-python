import os
from dotenv import load_dotenv

load_dotenv('./resources/.env')

testenv = os.getenv('TESTENV')
print(testenv)