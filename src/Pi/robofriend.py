#!/usr/bin/env python

# external modules
import signal
import time
import sys
import os

path = str(os.getcwd()) + "/python"
sys.path.append(path)

# own modules
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
import stateModule as stateModule


# globals
runFlag = True

def stop():
	global runFlag

	print("*** shutting down ... ***")
	rfidModule.stop()
	webserverModule.stop()
	statusModule.stop()
	gameCommunicator.stop()
	keyboardModule.stop()
	teensyCommunicator.stop()
	ioWarriorModule.stop()
	speechModule.stop()
	faceModule.close()
	runFlag = False
	print("*** graceful shutdown completed! ***")

def handler_stop_signals(signum, frame):
	stop()

def main():
	global runFlag

	stateModule.start()

	# create and initialize states
	# starting modules
	# enter Init State
	# start while and check queueu
	rfidModule.start()		# implement mechanism to stop executing thread
	webserverModule.start()
	statusModule.start()
	gameCommunicator.start()
	keyboardModule.start()
	faceModule.drawFace()
	facedetectionModule.listener()
	print("init done! register signal handlers...")

	# setting up signal handlers for shutdown
	signal.signal(signal.SIGINT, handler_stop_signals)
	signal.signal(signal.SIGTERM, handler_stop_signals)
	#print("*** startup completed! ***")

	# create thread

	while runFlag:
		time.sleep(0.5) # keep program running until stopped

if __name__ == '__main__':
	main()
