
# Assignment A7:
# 1a) Show a context manager for my_file handling that automatically opens and closes a my_file.
# b) Shows a context manager for managing a database conn.
# c) Show a multithreading and multiprocessing  that allows us to run the function for different amounts of time.




#a) Show a context manager for my_file handling that automatically opens and closes a my_file.

#  my_file management using
# context manager

class FileManager():
    def __init__(self, my_file_name, my_file_mode):
        self.my_file_name = my_file_name
        self.my_file_mode = my_file_mode
        self.my_file = None

    def __enter__(self):
        self.my_file = open(self.my_file_name, self.my_file_mode)
        return self.my_file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.my_file.close()


# loading a my_file
with FileManager('test.txt', 'w') as f:
    f.write('My my_file using context manger')

print(f"It is {f.closed} that my_file was opened and closed successfully")
print("--------------------------------")






#b) Shows a context manager for managing a database conn.

import sqlite3

class MyDatabase:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

   #The __exit__ method takes care of closing the connection on exiting the with block
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()


with MyDatabase("school.db") as conn:
    cursor = conn.cursor()
    
    # Create table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS student (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER
        )
    """)
    
    # Insert data into the table
    cursor.execute("INSERT INTO student (name, age) VALUES ('Abraham', 25)")
    cursor.execute("INSERT INTO student (name, age) VALUES ('Atong', 30)")
    conn.commit()
    
    # Retrieve and print data from the table
    cursor.execute("SELECT * FROM student")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
print("--------------------------------")






# c) Show a multithreading and multiprocessing  that allows us to run the function for different amounts of time.

import multiprocessing
import threading
import os
import time


def task_sleep(sleep_duration, task_number):
    time.sleep(sleep_duration)
    print(f"Task {task_number} done (slept for {sleep_duration}s)! "
           f"Main thread: {threading.main_thread().name}, "
          f"Current thread: {threading.current_thread().name}, "
          f"Process ID: {os.getpid()}")


if __name__ == "__main__":
    time_start = time.time()

    # Create process
    p1 = multiprocessing.Process(target=task_sleep, args=(3, 1))
    p2 = multiprocessing.Process(target=task_sleep, args=(5, 2))
 # Start task execution for processing
    p1.start()
    p2.start()
 # Wait for process to complete execution
    p1.join()
    p2.join()

     # Create thread
    t1 = threading.Thread(target=task_sleep, args=(3, 1))
    t2 = threading.Thread(target=task_sleep, args=(5, 2))

    # Start task execution for thread
    t1.start()
    t2.start()

     # Wait for thread to complete execution
    t1.join()
    t2.join()



    time_end = time.time()
    print(f"Time elapsed: {round(time_end - time_start, 2)}s")








    """
    # Day7 Notes
# Remaining concepts in Advanceed python Topics

# Context Manager
# Multithreading and multiprocessing

# Context manager- Is an object that defines temporary context for a block of code

# Example1: Demonstrate a context manager to open a my_file and returns a context manager instance

import threading
import multiprocessing
import time


def open_my_file(my_file_name):

    # Open a my_file and return a context manager instance
    my_file = open(my_file_name, 'r')

    def __enter__():
        return my_file

    def __exit__(self, exc_type, exc_val, exc_tb):
        my_file.close()

        return __enter__.__exit__
    with open_my_file('my_my_file.txt') as f:
        contents = f.read()


# Example2: Demonstrate a context manager to open a my_file and returns a context manager using time series


class Timer:
    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_val, traceback):
        end_time = time.time()
        execute_time = end_time - self.start_time

        print(f"The time for this excution {execute_time} seconds elapsed")
        print("----------------------------------------------------------------")


with Timer():
    # measure execution time
    time.sleep(2)

    # Multithreading and multiprocessing


#tecchnique that can be used to improve performance of a python program

    # Multithreading is a technique where multiple threads are created within a single process
    # Multiprocessing is a technique where multiple processes(threads) are created within a single machine

    # Example3 of multithreading

    import threading

    def task(name):
        print(f"Running task {name}")

    # Create multiple threads
    threads = []
    for i in range(5):
        t = threading.Thread(target=task, args=(f"Thread {i}",))
        threads.append(t)
        t.start()

    # Wait for threads to finish
    for t in threads:
        t.join()


# Example4: Demonstrate use of multiprocessing


def process_task(name):
    print(f"Running task {name}")


# Create a pool of threads
pool = multiprocessing.Pool(processes=5)

# submit mutliple tasks to pool
for i in range(6):
    pool.apply_async(process_task, args=(f"Process {i}",))

# Close the pool and wait for all process to finish
pool.close()
pool.join()


# Example5: demonstrate use of multithreaading and multiprocessing


def task(name):
    print(
        f"Running task {name} on thread {threading.current_thread().name} with process {multiprocessing.current_process().name}")


# Create multiple threads
threads = []
for i in range(4):
    t = threading.Thread(target=task, args=(f"Thread {i}",))
    threads.append(t)
    t.start()

# Wait for threads to finish
for t in threads:
    t.join()

    """