#external modules
import threading
import time
from transitions import Machine

class Robo():
    pass

runFlag = True

def start():
    print("[INFO] Starting state initialization")
    threadHandler = threading.Thread(target = state_handler)
    threadHandler.daemon = True
    threadHandler.start()

def state_handler():
    print("[INFO] Within state handler thread ...")
    state_config()

def state_config():
    states = ['init', 'idle', 'keyboard', 'face_audio_detection',
              'gui_communicator', 'webserver', 'low_battery']
    robostate = Robo()
    stat = Machine(model = robostate, states = states, initial = 'init')
    while runFlag:
        #print(robostate.state)
        print("[INFO] We are in the state: {}".format(robostate.state))
        time.sleep(2)
