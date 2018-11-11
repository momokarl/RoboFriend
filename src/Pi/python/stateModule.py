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


# global variables
runFlag = True


class Robo(Machine):
    def __init__(self):
        states = [
                'init', 'idle', 'keyboard',
                'face_audio_detection','gui_communication',
                'webserver', 'low_battery']

        Machine.__init__(self, states = states, initial = 'init')

        # transition from init state to idle state
        self.add_transition(trigger = 'init_to_idle', source = 'init', dest = 'idle')

        # transition from idle state to init state
        self.add_transition(trigger = 'idle_to_gui_communication', source = 'idle', dest = 'gui_communication')

        # transition from gui communication state to idle state
        self.add_transition(trigger = 'gui_communcation_to_idle', source = 'gui_communication', dest = 'idle')


        # function call when leaving init states
        self.on_exit_init('leaving_init_state')

        # function call when entering idle state
        self.on_enter_idle('entering_idle_state')

        # function call when leaving idle states
        self.on_exit_idle('leaving_idle_state')

        # function call when entering gui communication state
        self.on_enter_gui_communication('entering_gui_communication')

        # function call when leaving gui communication state
        self.on_exit_gui_communication('leaving_gui_communication')

    # While leaving the init state all threads of each module are startet
    def leaving_init_state(self):
        rfidModule.start()
        webserverModule.start()
        statusModule.start()
        gameCommunicator.start()
        keyboardModule.start()
        faceModule.drawFace()
        print("[INFO] Leaving init state after modules initialized")

    def entering_init_state(self):
        print("[INFO] Init state entered")

    # Methode when entering the idle state
    def entering_idle_state(self):
        print("[INFO] Idle state entered")
        # start autoSpeak
        speechModule.startAutoRandomSpeak()

    # Methode when idle state is leaved
    def leaving_idle_state(self):
        # stop autoSpeak
        speechModule.stop()
        print("[INFO] Leaving idle state")

    # Methode when entering gui_communication
    def entering_gui_communication(self):
        print("[INFO] Entering gui commumication state")

    # Methode when leaving gui_communicator
    def leaving_gui_communication(self):
        print("[INFO] Leaving gui communication state")


def start():
    print("[INFO] Starting state initialization")
    threadHandler = threading.Thread(target = state_handler)
    threadHandler.daemon = True
    threadHandler.start()

def state_handler():
    print("[INFO] State thread started")
    robostate = Robo()
    robostate.init_to_idle()  # to leave init state and enter idle state

    while runFlag:
         #print("[INFO] We are in the state: {}".format(robostate.state))
         time.sleep(2)
