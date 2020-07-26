'''
 * ************************************************************
 *      Program: Google Translator Engine
 *      Type: Python
 *      Author: David Velasco Garcia @davidvelascogarcia
 * ************************************************************
 *
 * | INPUT PORT                           | CONTENT                                                 |
 * |--------------------------------------|---------------------------------------------------------|
 * | /googleTranslatorEngine/data:i       | Input data text to translate                            |
 *
 * | OUTPUT PORT                          | CONTENT                                                 |
 * |--------------------------------------|---------------------------------------------------------|
 * | /googleTranslatorEngine/data:o       | Output translated text                                  |
 *
'''

# Libraries
import configparser
import datetime
import os
from googletrans import Translator
import platform
import time
import yarp

print("**************************************************************************")
print("**************************************************************************")
print("                  Program: Google Translator Engine                       ")
print("                     Author: David Velasco Garcia                         ")
print("                             @davidvelascogarcia                          ")
print("**************************************************************************")
print("**************************************************************************")

print("")
print("Starting system ...")
print("")

print("")
print("Loading Google Translator Engine module ...")
print("")

print("")
print("Detecting system and release version ...")
print("")
systemPlatform = platform.system()
systemRelease = platform.release()

print("")
print("**************************************************************************")
print("Configuration detected:")
print("**************************************************************************")
print("")
print("Platform:")
print(systemPlatform)
print("Release:")
print(systemRelease)

print("")
print("**************************************************************************")
print("Initializing googleTranslatorEngine:")
print("**************************************************************************")
print("")
print("[INFO] Initializing googleTranslatorEngine at " + str(datetime.datetime.now()) + " ...")
print("")

print("")
print("[INFO] Google Translator Engine initialized correctly.")
print("")

print("")
print("**************************************************************************")
print("YARP configuration:")
print("**************************************************************************")
print("")
print("Initializing YARP network ...")
print("")

# Init YARP Network
yarp.Network.init()

print("")
print("[INFO] Opening data input port with name /googleTranslatorEngine/data:i ...")
print("")

# Open input googleTranslatorEngine data port
googleTranslatorEngine_inputPort = yarp.BufferedPortBottle()
googleTranslatorEngine_inputPortName = '/googleTranslatorEngine/data:i'
googleTranslatorEngine_inputPort.open(googleTranslatorEngine_inputPortName)


print("")
print("[INFO] Opening data output port with name /googleTranslatorEngine/data:o ...")
print("")

# Open output googleTranslatorEngine data port
googleTranslatorEngine_outputPort = yarp.Port()
googleTranslatorEngine_outputPortName = '/googleTranslatorEngine/data:o'
googleTranslatorEngine_outputPort.open(googleTranslatorEngine_outputPortName)

# Create googleTranslatorEngine output data bottle
googleTranslatorEngineOutputBottle = yarp.Bottle()

print("")
print("[INFO] YARP configured correctly.")
print("")

print("")
print("**************************************************************************")
print("Translator configuration:")
print("**************************************************************************")
print("")

# Control loop file exist
loopControlFileExist = 0

while int(loopControlFileExist) == 0:

    try:
        # Get languages data
        print("")
        print("Getting languages data ...")
        languagesData = configparser.ConfigParser()
        languagesData.read('../config/languages.ini')
        languagesData.sections()

        # Extract language input
        inputLanguage = languagesData['Languages']['language-input']

        # Exit loop
        loopControlFileExist = 1

    except:
        print("")
        print("**************************************************************************")
        print("Error file not founded:")
        print("**************************************************************************")
        print("")

        # File not exist
        print("")
        print("[ERROR] Error, languages.ini not founded, i will check again in 4 seconds ...")
        print("")
        time.sleep(4)

print("")
print("[INFO] Data obtained correctly.")
print("")

print("")
print("Input language: " + str(inputLanguage))
print("Output language: Selected by user in real time sending language to translate in message text")
print("")

print("")
print("**************************************************************************")
print("Google Translator client:")
print("**************************************************************************")
print("")
print("Configuring Google Translator client at " + str(datetime.datetime.now()) + " ...")
print("")

googleTranslatorEngineClient = Translator()

print("")
print("[INFO] Client configuration done.")
print("")


# Variable to control loopControlTranslate
loopControlTranslate = 0

print("")
print("**************************************************************************")
print("Waiting for text to translate:")
print("**************************************************************************")
print("")
print("[INFO] Waiting for input text to translate at " + str(datetime.datetime.now()) + " ...")
print("")

while int(loopControlTranslate) == 0:

    print("")
    print("**************************************************************************")
    print("Processing translate request:")
    print("**************************************************************************")
    print("")
    print("[INFO] Processing translate requests at " + str(datetime.datetime.now()) + " ...")
    print("")

    # Receive text to translate
    googleTranslatorEngineInputBottle = googleTranslatorEngine_inputPort.read()

    # Extract text to translate
    dataToTranslate = googleTranslatorEngineInputBottle.get(1).asString()

    # Clear string to remove ""
    dataToTranslate = str(dataToTranslate)
    dataToTranslate = dataToTranslate.replace('"','')

    # Extract language to translate
    outputLanguage = googleTranslatorEngineInputBottle.get(3).asString()

    # Clear string to remove ""
    outputLanguage = str(outputLanguage)
    outputLanguage = outputLanguage.replace('"','')


    print("")
    print("[RECEIVED] Data received: " + str(dataToTranslate) + ", translate to " + str(outputLanguage) + " at " + str(datetime.datetime.now()))
    print("")


    try:
        # Sending request to Google Translator API
        print("")
        print("**************************************************************************")
        print("Connecting with Google Translator server:")
        print("**************************************************************************")
        print("")
        print("[INFO] Connecting with Google Translator server ...")
        print("")

        print("")
        print("[INFO] Translating from " + str(inputLanguage) + " to " + str(outputLanguage) + " at " + str(datetime.datetime.now()) + " ...")
        print("")

        # Translating
        dataTranslated = googleTranslatorEngineClient.translate(str(dataToTranslate), dest=str(outputLanguage), src=str(inputLanguage))
        dataTranslated = dataTranslated.text

        print("")
        print("[INFO] Text translated at " + str(datetime.datetime.now()) + ".")
        print("")

        # Show results
        print("")
        print("**************************************************************************")
        print("Results:")
        print("**************************************************************************")
        print("")
        print("[RESULTS] Input text in " + str(inputLanguage) + " language: "+ str(dataToTranslate))
        print("")
        print("[RESULTS] Output text in " + str(outputLanguage) +" language: " + str(dataTranslated))
        print("")

    except:
        print("")
        print("[ERROR] Sorry, i could´t resolve your request.")
        print("")


    # Send output results
    googleTranslatorEngineOutputBottle.clear()
    googleTranslatorEngineOutputBottle.addString("TRANSLATION:")
    googleTranslatorEngineOutputBottle.addString(str(dataTranslated))
    googleTranslatorEngineOutputBottle.addString("DATE:")
    googleTranslatorEngineOutputBottle.addString(str(datetime.datetime.now()))
    googleTranslatorEngine_outputPort.write(googleTranslatorEngineOutputBottle)

# Close YARP ports
print("[INFO] Closing YARP ports ...")
googleTranslatorEngine_inputPort.close()
googleTranslatorEngine_outputPort.close()

print("")
print("**************************************************************************")
print("Program finished")
print("**************************************************************************")
print("")
print("googleTranslatorEngine program finished correctly.")
print("")
