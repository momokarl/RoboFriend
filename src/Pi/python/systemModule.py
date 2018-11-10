# external modules
import os
import time
import subprocess
import signal


# own modules
import speechModule

# globals
roscore_pid = 0

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
