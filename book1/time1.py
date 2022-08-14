import time
from tracemalloc import start
start_time = time.time()

for i in range(0,100000):
    pass

end_time = time.time()
print(start_time)
print(end_time)
print(f"time: {end_time-start_time}")