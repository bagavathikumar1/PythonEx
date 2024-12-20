import threading
import time

def print_name(name, *args):
    print(name, *args)

name = "Tutorialspoint..."

# Create and start threads
thread1 = threading.Thread(target=print_name, args=(name, 1))
thread2 = threading.Thread(target=print_name, args=(name, 1, 2))

thread1.start()
thread2.start()

# Wait for threads to complete
thread1.join()
thread2.join()

print("Threads are finished...exiting")