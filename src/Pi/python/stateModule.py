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
                'face_audio_detection','gui_communicator',
                'webserver', 'low_battery']

        Machine.__init__(self, states = states, initial = 'init')

        # transition from init state to idle state
        self.add_transition(trigger = 'init_to_idle', source = 'init', dest = 'idle')


        ############### IDLE STATE ###############
        # transition from idle state to gui communicator
        #self.add_transition(trigger = 'idle_to_gui_communicator', source = 'idle', dest = 'gui_communicator')

        # transition from idle state to keyboard state
        #self.add_transition(trigger = 'idle_to_keyboard', source = 'idle', dest = 'keyboard')

        # transition from idle state to webserver state
        #self.add_transition(trigger = 'idle_to_webserver', source = 'idle', dest = 'webserver')

        # transition from idle state to face/audio deetction state
        #self.add_transition(trigger = 'idle_to_face_audio_detection', source = 'idle', dest = 'face_audio_detection')

        # transition from idle state to init state
        #self.add_transition(trigger = 'idle_to_low_battery', source = 'idle', dest = 'low_battery')

        # transition from gui communicator state to idle state
        self.add_transition(trigger = 'gui_communcation_to_idle', source = 'gui_communicator', dest = 'idle')

        # transition from every state to idle states
        self.add_transition(trigger = 'to_idle', source = '*', dest = 'idle')

        # transition from every state to gui communicator
        self.add_transition(trigger = 'to_gui_communicator', source = '*', dest = 'gui_communicator')

        # transition from every state to keyboard
        self.add_transition(trigger = 'to_keyboard', source = '*', dest = 'keyboard')

        # transition from every state to face/audio detection
        self.add_transition(trigger = 'to_face_audio_detection', source = '*', dest = 'face_audio_detection')

        # transition from every state to webserver
        self.add_transition(trigger = 'to_webserver', source = '*', dest = 'webserver')

        # transition from every state to low battery
        self.add_transition(trigger = 'to_low_battery', source = '*', dest = 'low_battery')



        # function call when leaving init states
        self.on_exit_init('leaving_init_state')

        # function call when entering idle state
        self.on_enter_idle('entering_idle_state')

        # function call when leaving idle states
        self.on_exit_idle('leaving_idle_state')

        # function call when entering gui communicator state
        self.on_enter_gui_communicator('entering_gui_communicator')

        # function call when leaving gui communicator state
        self.on_exit_gui_communicator('leaving_gui_communicator')


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

    # wird nicht gehen weil ich argumente übergeben muss deshalb bei transition
    # Methode when entering gui_communicator
    #def entering_gui_communicator(self):
        #print("[INFO] Entering gui commumication state")

    # Methode when leaving gui_communicator
    #def leaving_gui_communicator(self):
        #print("[INFO] Leaving gui communicator state")

# global variables
robostate = Robo()
runFlag = True
state_changer = {
    "idle" : to_idle,
    "gui_communicator" : to_gui_communicator,
    "keyboard" : to_keyboard,
    "face_audio_detection" : to_face_audio_detection,
    "webserver" : to_webserver,
    "low_battery" : to_low_battery
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
            if not received_message[0] in valid_transmitter:
                print("[INFO] Message from an invalid transmitter received!")
            else:
                print("[INFO] First Part of received message: {}, second Part: {}".format(received_message[0], received_message[1]))

                if actual_state == "idle":
                    state_changer[received_message[0]](received_message[1])
                elif actual_state == "gui_communicator":
                    #TODO: check if transition into received state is allowed
                    #TODO: Pass two arguments 1) from which state  2) command
                    #TODO:


                    # als letzter schritt wenn transition statfinden soll der übergang
                    # state_changer[received_message[0]](received_message[1])
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
    robostate.to_idle() # to trigger a transition to idle state

def to_gui_communicator(command):
    global robostate
    robostate.to_gui_communicator(command) # to trigger a transition to gui communicator state

def to_keyboard(command):
    global robostate
    robostate.to_keyboard() # to trigger a transition to keyboard state

def to_face_audio_detection():
    global robostate
    robostate.to_face_audio_detection() # to trigger a transition to face/audio detection state

def to_webserver():
    global robostate
    robostate.to_webserver() # to trigger a transition to webserver state

def to_low_battery():
    global robostate
    robostate.to_low_battery() # to trigger a transition to low battery state
