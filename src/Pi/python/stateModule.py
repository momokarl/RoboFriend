#external modules
import threading

runFlag = True

def start():
    print("[INFO] Starting state initialization")
    threadHandler = threading.Thread(target = stateHanlder)
    threadHandler.daemon = True
    threadHandler.start()

def stateHandler():
    print("[INFO] Within state handler thread ...")
