#!/usr/bin/python

import _thread
import time
import threading

# Define a function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print("{0}: {1}".format(threadName, time.ctime(time.time()) ) )

# Create two threads as follows
try:
   thread1 = _thread.start_new_thread( print_time, ("Thread-1", 2, ) )
   thread2 = _thread.start_new_thread( print_time, ("Thread-2", 4, ) )
except:
   print("Error: unable to start thread")


time.sleep(10)