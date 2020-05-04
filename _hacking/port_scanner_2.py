import socket
from datetime import datetime
import threading
from queue import Queue

# to prevent multiple threads scan the same port
print_lock = threading.Lock()

# enter the host to scan
host = input("Enter host address to scan: ")
ip = socket.gethostbyname(host)
# starting time
t1 = datetime.now()
# port scanning
def scan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print("\n %d is open  \t\t" %(port) )
            sock.close()
    except:
        pass

# creating threader function
def threader():
    while True:
        worker = q.get() # get a worker
        scan(worker)
        q.task_done() # complete with the job
# create a queue
q = Queue()
# for loop for number of threads to allow
for x in range(100):
    t = threading.Thread(target=threader)
    t.daemon=True
    t.start()

for worker in range(1, 100):
    q.put(worker)
q.put(8080)
q.put(3000)
q.put(443)
# thread will join after thread termination
q.join()

# end time
t2 = datetime.now()
total = t2 - t1
print("Total scanning time: ", total)