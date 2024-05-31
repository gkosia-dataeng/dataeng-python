# check if object is of specific type
if isinstance(5.5, int):
    print("Its an int") 
else:   
    print("its not int")


# % measure the time 
import time

start_time  = time.time()
time.sleep(10)
print("--- %s seconds ---" % (time.time() - start_time))

# get ascii of char
print(ord("A")) #65


# format numbers
print("{:,}".format(1000000))