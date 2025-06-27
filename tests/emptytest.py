import random
import time
while True:
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    random.seed(time.time())
    print(random.randint(1,4),random.randint(5,8))
    time.sleep(2)