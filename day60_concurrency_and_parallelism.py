
import time 

#------------ Let’s first see a non-concurrent version:------------

# def download_file(file_name):
#     print(f"starting download of {file_name}")
#     time.sleep(3) # simulate 3-second file download
#     print(f"finished download of {file_name}")

# start_time = time.time()

# download_file("file1")
# download_file("file2")
# download_file("file3")

# end_time = time.time()

# print(f"total time taken: {end_time - start_time:.2f} second")


# --------------concurrent version--------------

import threading

def download_file(file_name):
    print(f"starting download of {file_name}")
    time.sleep(3) # simulate 3-second file download
    print(f"finished download of {file_name}")

start_time = time.time()

#creating threads

t1 = threading.Thread(target=download_file, args=("file1",))
t2 = threading.Thread(target=download_file, args=("file2",))
t3 = threading.Thread(target=download_file, args=("file3",))

# start all threads ( they run concurrently)
t1.start()
t2.start()
t3.start()

# wait for all thread to finish
t1.join()
t2.join()
t3.join()

end_time = time.time()

print(f"total taken time: {end_time - start_time:.2f}second")


# | Step | What Happens                                                                                                   |
# | ---- | -------------------------------------------------------------------------------------------------------------- |
#  1️⃣  | 3 threads (`t1`, `t2`, `t3`) are created.   
#                                                                    |
# 
#  2️⃣  | `t1.start()`, `t2.start()`, `t3.start()` start executing `download_file()` **concurrently**.                   |
# 
#  3️⃣  | Python switches between threads rapidly — while one thread is sleeping (simulating network delay), others run. |
# 
#  4️⃣  | `.join()` ensures the main program waits until all threads are done.                                           |
# 
#  5️⃣  | The total time equals the **longest single thread’s** time (≈3s), not the sum (9s).                            |




