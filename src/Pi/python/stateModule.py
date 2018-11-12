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
import systemModule as SystemModule

class Robo(Machine):
    def __init__(self):
        states = [
                'init', 'idle', 'keyboard',
                'face_audio_detection','gui_communication',
                'webserver', 'low_battery']

        Machine.__init__(self, states = states, initial = 'init')

        # transition from init state to idle state
        self.add_transition(trigger = 'init_to_idle', source = 'init', dest = 'idle')


        ############### IDLE STATE ###############
        # transition from idle state to init state
        self.add_transition(trigger = 'idle_to_gui_communication', source = 'idle', dest = 'gui_communication')

        # transition from idle state to keyboard state
        self.add_transition(trigger = 'idle_to_keyboard', source = 'idle', dest = 'keyboard')

        # transition from idle state to webserver state
        self.add_transition(trigger = 'idle_to_webserver', source = 'idle', dest = 'webserver')

        # transition from idle state to face/audio deetction state
        self.add_transition(trigger = 'idle_to_face_audio_detection', source = 'idle', dest = 'face_audio_detection')

        # transition from idle state to init state
        self.add_transition(trigger = 'idle_to_low_battery', source = 'idle', dest = 'low_battery')



        # transition from gui communication state to idle state
        self.add_transition(trigger = 'gui_communcation_to_idle', source = 'gui_communication', dest = 'idle')


        # transitions from every state to idle states
        self.add_transition(trigger = 'to_idle', source = '*', dest = 'idle')


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

# global variables
robostate = Robo()
runFlag = True
state_change = {
    "idle" : to_idle,
    "gui_communicator" : to_gui_communicator,
    "keyboard" : to_keyboard,
    "face_audio_detection" : to_face_audio_detection,
    "webserver" : to_webserver,
    "low_battery" : to_lowbattery
}

def start():
    print("[INFO] Starting state initialization")
    threadHandler = threading.Thread(target = state_handler)
    threadHandler.daemon = True
    threadHandler.start()

def state_handler():
    global robostate
    print("[INFO] State thread started")
    actual_state = ""
    valid_transmitter = ["gui_communicator"]

    robostate.init_to_idle()  # to leave init state and enter idle state
    actual_state = robostate.state

    if (actual_state  != "idle"):
        print("[INFO] Error state initialization!")
    else:
        while runFlag:
            received_message = SystemModule.queue_get()
            print("[INFO] Message received!!!")
            print("[INFO] Received Message: {}".format(received_message))
            if not received_message[1] in valid_transmitter:
                print("[INFO] Message from an invalid transmitter received!")
            else:
                print("[INFO] First Part of received message: {}, second Part: {}".format(received_message[0], received_message[1]))

                if actual_state == "idle":
                    # TODO: check if received value is valid the trigger taransition
                elif actual_state == "gui_communicator":
                    #TODO: Pass two arguments 1) from which state  2) command
                    #TODO:
                elif actual_state == "keyboard":
                    #TODO:
                elif actual_state == "webserver":
                    #TODO:
                elif actual_state == face_audio_detection:
                    #TODO:
                elif actual_state == low_battery:
                    #TODO:
                else:
                    pass
def to_idle():
    global robostate
    robostate.to_idle()

def to_gui_communicator():
    global robostate
