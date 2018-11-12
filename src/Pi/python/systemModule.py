# external modules
import os
import time
import subprocess
import signal
import queue


# own modules
import speechModule

# globals
roscore_pid = 0
queue = queue.Queue()

def shutdown():
    speechModule.speakShutdown()
    time.sleep(3)
    os.system('sudo init 0')

def roscore_start():
    global roscore_pid

    roscore = subprocess.Popen('roscore')
    roscore_pid = roscore.pid
    #print("[INFO] Roscore pid: {}".format(roscore.pid))
    print("[INFO] Roscore started!")

def roscore_shutdown():
    global roscore_pid

    if roscore_pid != 0:
        os.kill(roscore_pid, signal.SIGTERM)
        print("[INFO] Roscore terminated!")
    else:
        pass

def queue_put(item):
    if queue.full() != True:
        queue.put(item)
        return True
    else:
        print("[INFO] Queue is full!")
        return False

def queue_get():
    return queue.get()
