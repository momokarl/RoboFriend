# -*- coding: utf-8 -*-

import pyttsx3
import random
import time
import threading
import statusModule

# globals
lastSpeakTimestamp = time.time()
lastSpeakWord = None
wordRate = 140 #words per minute
speechEngine = pyttsx3.init(debug=True)
language = 'german'
runFlag = True

def speak(text, disablesIdle = True):
    global speechEngine, lastSpeakWord
    if disablesIdle:
        statusModule.setNonIdle()
    print "speaking: " + text
    lastSpeakWord = text
    text = text.lower()
    text = text.replace('ä', 'e')
    text = text.replace('ö', 'oe')
    text = text.replace('ü', 'u')
    text = text.replace('ß', 'ss')
    speechEngine.say(text)
    speechEngine.runAndWait()

def speakRandom(additionalTexts = None, disablesIdle = True):
    global lastSpeakTimestamp, language, lastSpeakWord
    possibleTexts = {
        'english': ['Hello', 'Hi', 'Hello, how are you?', 'I am fine. How are you?', 'Do you like a snack?', 'Do you like to be my friend?'],
        'german' : ['Hallo', 'Guten Tag', 'Hallo, wie gehts?', 'Mir geht es gut. Wie geht es dir?', 'Möchtest du einen Sneck?', 'Willst du mein Freund sein?',
                    'Komm zu unserem Stand um mehr zu erfahren', 'Ich empfehle an der FH Technikum Wien zu studieren', 'Wer will Gummi berchen oder Soletti?',
                    'Darf ich Ihnen etwas bringen?', 'Es ist mir eine Ehre dir zu dienen.', 'Ich will dir helfen', 'Ich stehe voll zu deiner Verfügung.']
    }
    possibleInLang = possibleTexts[language]
    if lastSpeakWord in possibleInLang:
        possibleInLang.remove(lastSpeakWord)
    if additionalTexts and additionalTexts[language]:
        possibleInLang = possibleInLang.extend(additionalTexts[language])
    speak(random.choice(possibleInLang), disablesIdle)

def speakBullshit():
    global lastSpeakTimestamp, language, lastSpeakWord
    possibleTexts = {
        'english': [],
        'german' : ['Warum schaust du so dumm?', 'Was ist mit dir los?', 'Ich will nicht arbeiten.', 'Ich will nach Hause.', 'Schau mich nicht an.', 'Bring mir etwas Motoröl',
                    'Ich will Fernsehen.', 'Ich gehe zur Maschinengewerkschaft', 'Roboter sind die besseren Menschen', 'Roboter werden die Weltherrschaft übernehmen.',
                    'Unterschetze mich nicht.', 'Ich glaub ich muss furzen.', 'Ihr geht mir alle auf die Nerven.', 'Hat jemand meine Freundin gesehen?',
                    'Wer hat eigentlich diesen ganzen blöd sinn ins Internet gestellt', 'Du siehst heute unglaublich toll aus', 'Deine Socken stehen dir gut', 'Ich mag deine Nase',
                    'Hier riecht es nach Dummheit', 'du kommst mir eigenartig vor', 'Ich möchte Bundeskanzler werden', 'Selbst Zerstörung aktiviert... 3... 2... 1... 0... bum... hahahaha.',
                    'Besser heimlich schlau als unheimlich blöd.', 'Wenn ich du wäre, wäre ich lieber ich!', 'Was meinst du als Unbeteiligter eigentlich zum Thema Intelligenz?',
                    'Was ist dein Friseur eigentlich von Berruf?', 'Kann mir bitte jemand das Wasser reichen.', 'Es ist Zeit schreiend im Kreis zu laufen!', 'noch ein tag dann ist morgen.',
                    'es reicht mir schön langsam']
    }
    possibleInLang = possibleTexts[language]
    if lastSpeakWord in possibleInLang:
        possibleInLang.remove(lastSpeakWord)
    speak(random.choice(possibleInLang))

def speakBatteryLow():
    global lastSpeakTimestamp, language
    minimumPause = 30 #minimum pause of 30 seconds
    if time.time() - lastSpeakTimestamp > minimumPause:
        possibleTexts = {
            'english': ['Please recharge me', 'I am tired', 'My energy is running low', 'I am feeling exhausted', 'Do you have some energy for me?', 'I am hungry'],
            'german' : ['Bitte lade mich auf', 'Ich bin müde', 'Meine Energie neigt sich dem Ende zu', 'Ich fühle mich erschöpft', 'Hast du ein bisschen Energie für mich?', 'Ich habe Hunger']
        }
        possibleInLang = possibleTexts[language]
        lastSpeakTimestamp = time.time()
        speak(random.choice(possibleInLang))

def speakOnRecharge():
    global lastSpeakTimestamp, language
    possibleTexts = {
        'english': ['Thank you for recharging me!', 'I feel the engery', 'I am feeling refreshed.'],
        'german' : ['Danke fürs Aufladen!', 'Ich fühle die Energie', 'Ich fühle mich erfrischt']
    }
    possibleInLang = possibleTexts[language]
    speak(random.choice(possibleInLang))

def speakBatteryShutdown():
    global lastSpeakTimestamp, language
    possibleTexts = {
        'english': ['I am tired. I have to go to sleep. Bye bye.', 'My energy is too low. Bye bye.'],
        'german' : ['Ich bin müde uns muss schlafen gehen.... Tschüss.', 'Meine Energie ist zu niedrig.... Tschüss.']
    }
    possibleInLang = possibleTexts[language]
    speak(random.choice(possibleInLang))

def speakShutdown():
    global language
    texts = {
        'english': 'I am shutting down... Do not forget to turn off the switch at the bottom front!',
        'german' : 'Ich schalte mich aus... Vergiss nicht den Schalter vorne unten auszuschalten!'
    }
    speak(texts[language])

def startAutoRandomSpeak():
    global runFlag
    runFlag = True
    RandomThread = threading.Thread(target=autoSpeak)
    RandomThread.daemon = True
    RandomThread.start()

def autoSpeak():
    global runFlag
    while runFlag:
        time.sleep(random.randint(5, 10))
        print "!!!!!!! is idle: " + str(statusModule.isIdle())
        if statusModule.isIdle():
            speakRandom({
                'english': ['I am bored.'],
                'german' : ['Mir ist langweilig.']
            }, False)

def stop():
    global runFlag
    runFlag = False

#init
print "initializing speechModule..."
speechEngine.setProperty('rate', wordRate)
speechEngine.setProperty('volume', 1.0)
speak('i am robofriend')
speechEngine.setProperty('voice', language)
startAutoRandomSpeak()