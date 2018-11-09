#external modules
import threading
import time
from transitions import Machine

#own modules
import faceModule as faceModule
import rfidModule as rfidModule
import webserverModule as webserverModule
import statusModule as statusModule
import gameCommunicator as gameCommunicator
import keyboardModule as keyboardModule
import teensyCommunicator as teensyCommunicator
import ioWarriorModule as ioWarriorModule
import speechModule as speechModule
import facedetectionModule as facedetectionModule

class Robo(Machine):
    def __init__(self):
        states = [
                'init', 'idle', 'keyboard',
                'face_audio_detection','gui_communicator',
                'webserver', 'low_battery']

        Machine.__init__(self, states = states, initial = 'init')

        self.add_transition(trigger = 'leave_init', source = 'init', dest = 'idle',
                         before = 'start_modules', after = 'say_hello')

    def start_modules(self):
        rfidModule.start()
        webserverModule.start()
        statusModule.start()
        gameCommunicator.start()
        keyboardModule.start()
        faceModule.drawFace()
        print("[INFO] Leaving init state")

    def say_hello(self):
        print("[INFO] entering idle state")

runFlag = True

def start():
    print("[INFO] Starting state initialization")
    threadHandler = threading.Thread(target = state_handler)
    threadHandler.daemon = True
    threadHandler.start()

def state_handler():
    robostate = Robo()
    robostate.leave_init()  # to leave init state and enter idle state

    while runFlag:
         #print("[INFO] We are in the state: {}".format(robostate.state))
         time.sleep(2)
