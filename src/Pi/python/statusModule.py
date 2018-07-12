# external modules
import time
import threading

#own modules
import teensyCommunicator
import gameCommunicator

# globals
currentStatus = None
StatusThread = None
refreshIntervalMs = 1000
keyBat = 'batVolt'
keyIrL = 'irLeft'
keyIrM = 'irMiddle'
keyIrR = 'irRight'
runFlag = True

def getStatus():
    return currentStatus

def getBatteryVoltage():
    global currentStatus, keyBat
    return currentStatus[keyBat]

def getIRLeft():
    global currentStatus, keyIrL
    return currentStatus[keyIrL]

def getIRMiddle():
    global currentStatus, keyIrM
    return currentStatus[keyIrM]

def getIRRight():
    global currentStatus, keyIrR
    return currentStatus[keyIrR]

# This function is used as Thread to periodically update the battery information
def StatusInfo():
    global currentStatus, refreshIntervalMs, keyBat, keyIrL, keyIrM, keyIrR, runFlag
    while runFlag:
        rawStatus = teensyCommunicator.getRawStatus()
        currentStatus = parseRawStatus(rawStatus)
        gameCommunicator.sendtogui("battery;"+str(getBatteryVoltage()))

        print ("Battery= " + str(getBatteryVoltage()) + " Volt)")
        if getBatteryVoltage() < 31.5:
            print ("LOW BATTERY !! - Please Recharge!!")
        print ("IRSensors="+str(getIRLeft())+"/"+str(getIRMiddle())+"/"+str(getIRRight()))
        time.sleep(refreshIntervalMs / 1000.0)

def parseRawStatus(rawStatus):
    global keyBat, keyIrL, keyIrM, keyIrR

    batVolt = -1
    irSensorLeft = -1
    irSensorMiddle = -1
    irSensorRight = -1
    try:
        statusArray = rawStatus.split(',')
        if (statusArray[0] == "Sensors"):
            batVolt = int(statusArray[1]) / 20
            irSensorLeft = int(statusArray[2])
            irSensorMiddle = int(statusArray[3])
            irSensorRight = int(statusArray[4])
    except:
        print("error parsing status values: " + rawStatus)

    return {keyBat: batVolt, keyIrL: irSensorLeft, keyIrM: irSensorMiddle, keyIrR: irSensorRight}

def start():
    global StatusThread

    print "starting statusModule..."
    StatusThread = threading.Thread(target=StatusInfo)
    StatusThread.daemon = True
    StatusThread.start()

def stop():
    global runFlag
    print "stopping statusModule..."
    runFlag = False