'''
 * ************************************************************
 *      Program: Google Translator Engine
 *      Type: Python
 *      Author: David Velasco Garcia @davidvelascogarcia
 * ************************************************************
 */

/*
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
print("Starting system...")

print("")
print("Loading Google Translator engine...")

print("")
print("")
print("**************************************************************************")
print("YARP configuration:")
print("**************************************************************************")
print("")
print("Initializing YARP network...")

# Init YARP Network
yarp.Network.init()


print("")
print("Opening data input port with name /googleTranslatorEngine/data:i ...")

# Open input data port
googleTranslatorEngine_inputPort = yarp.Port()
googleTranslatorEngine_inputPortName = '/googleTranslatorEngine/data:i'
googleTranslatorEngine_inputPort.open(googleTranslatorEngine_inputPortName)

# Create input data bottle
inputBottle=yarp.Bottle()

print("")
print("Opening data output port with name /googleTranslatorEngine/data:o ...")

# Open output data port
googleTranslatorEngine_outputPort = yarp.Port()
googleTranslatorEngine_outputPortName = '/googleTranslatorEngine/data:o'
googleTranslatorEngine_outputPort.open(googleTranslatorEngine_outputPortName)

# Create output data bottle
outputBottle=yarp.Bottle()


print("")
print("Initializing googleTranslator engine...")

# Get system configuration
print("")
print("Detecting system and release version...")
systemPlatform = platform.system()
systemRelease = platform.release()

print("")
print("")
print("**************************************************************************")
print("Configuration detected:")
print("**************************************************************************")
print("Platform:")
print(systemPlatform)
print("Release:")
print(systemRelease)

print("")
print("")
print("**************************************************************************")
print("Translator configuration:")
print("**************************************************************************")

loopControlIniExist = 0

while int(loopControlIniExist)==0:

    try:
        # Get languages data
        print("")
        print("Getting languages data ...")
        languagesData = configparser.ConfigParser()
        languagesData.read('../config/languages.ini')
        languagesData.sections()

        inputLanguage = languagesData['Languages']['language-input']
        outputLanguage = languagesData['Languages']['language-output']
        loopControlIniExist = 1
    except:
        print("")
        print("**************************************************************************")
        print("Error file not founded:")
        print("**************************************************************************")
        # File not exist
        print("")
        print("Error, languages.ini not founded, i will check again in 4 seconds ...")
        print("Waiting 4 seconds to next check ...")
        print("")
        time.sleep(4)

print("Data obtained correctly.")
print("")
print("Input language: "+ str(inputLanguage))
print("Output language: "+ str(outputLanguage))

print("")
print("")
print("**************************************************************************")
print("Google Translator client:")
print("**************************************************************************")
print("")
print("Configuring Google Translator client ...")

googleTranslatorEngineClient = Translator()

print("Client configuration done.")


while True:

    # Waiting to input data
    print("")
    print("Waiting for input data ...")

    googleTranslatorEngine_inputPort.read(inputBottle)
    dataToTranslate = inputBottle.toString()
    dataToTranslate = dataToTranslate.replace('"','')

    print("Data received: "+str(dataToTranslate))

    print("")
    print("")
    print("**************************************************************************")
    print("Processing:")
    print("**************************************************************************")

    try:
        # Sending request to Google Translator API
        print("")
        print("Connecting with Google Translator server ...")

        print("")
        print("Translating from "+str(inputLanguage)+ " to "+ str(outputLanguage)+" ...")

        dataTranslated = googleTranslatorEngineClient.translate(str(dataToTranslate),dest=str(outputLanguage), src=str(inputLanguage))
        dataTranslated = dataTranslated.text
        print("")
        print("Text translated.")

        print("")
        print("Server response done.")

        print("")
        print("")
        print("**************************************************************************")
        print("Results:")
        print("**************************************************************************")
        print("")
        print("Input text in "+str(inputLanguage)+" language: "+ str(dataToTranslate))
        print("")
        print("Output text in "+str(outputLanguage)+" language: "+ str(dataTranslated))

    except:
        print("")
        print("Sorry, i could´t resolve your request.")


    # Send output results
    outputBottle.clear()
    outputBottle.addString(str(dataTranslated))

    googleTranslatorEngine_outputPort.write(outputBottle)

# Close YARP ports
print("Closing YARP ports...")
googleTranslatorEngine_inputPort.close()
googleTranslatorEngine_outputPort.close()

print("")
print("")
print("**************************************************************************")
print("Program finished")
print("**************************************************************************")
