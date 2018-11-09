#external modules
import threading
import time
from transitions import Machine

class Robo(Machine):
    def __init__(self):
        states = [
                'init', 'idle', 'keyboard',
                'face_audio_detection','gui_communicator',
                'webserver', 'low_battery']
        Machine.__init__(self, states = states, initial = 'init')
        #self.add_transition(trigger : 'leave_init', source : 'init', dest : 'idle', before = 'say_goodbye')
        self.add_transition('leave_init', 'init', 'idle',
                         before='say_goodbye',after = 'say_hello')

    def say_goodbye(self):
        print("[INFO] Goodbye init state")

    def say_hello(self):
        print("[INFO] Hello idle state")

runFlag = True

def start():
    print("[INFO] Starting state initialization")
    threadHandler = threading.Thread(target = state_handler)
    threadHandler.daemon = True
    threadHandler.start()

def state_handler():
    print("[INFO] Within state handler thread ...")
    robostate = Robo()
    #robostate.leave_init()
    print("[INFO] Actual state {}".format(robostate.state))
    robostate.leave_init()
    print("[INFO] Actual state {}".format(robostate.state))


    # while runFlag:
    #     print("[INFO] We are in the state: {}".format(robostate.state))
    #     time.sleep(2)
