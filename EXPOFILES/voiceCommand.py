from __future__ import annotations

from datetime import datetime
import speech_recognition as sr 
from typing import TYPE_CHECKING
import functools
from drugInfo import individualDrug
from confirmations import individualConfirm
from reports import individualReport
from scanBottle import individualEdit

if TYPE_CHECKING:
    from UIController import UIController

# Initialize the speech recognition 
r = sr.Recognizer() 

# Create a function that will be called when the command is given  
def record_speech(UIController: UIController, medications): 
	# Record the command from the microphone 
	with sr.Microphone() as source: 
		print("Listening...") 
		r.pause_threshold = 1
		audio = r.listen(source) 
	
	try: 
		# Use the Google Speech Recognition API 
		command = r.recognize_google(audio).lower() 
		navigateMenu(UIController, command, medications)
		print("You said: " + command + "\n") 
	
	# Error handling 
	except sr.UnknownValueError: 
		print("I couldn't understand you. Please try again.") 
	
	return command 

def navigateMenu(UIController, voiceStr, medications = None):
	date = datetime.now().strftime("%H %M")
	date = date.split(" ")
	if UIController.currentLocation == "Report":
		if medications != None:
			for index, med in enumerate(medications):
				if f'{med.medName}' in voiceStr:
					individualReport.individualReport(UIController, med.medName)
	elif UIController.currentLocation == "Confirm":
		if medications != None:
			for index, med in enumerate(medications):
				if f'{med.medName}' in voiceStr:
					individualConfirm.individualConfirm(UIController, med.medName, med)
	elif UIController.currentLocation == "DrugInfo":
		if medications != None:
			for index, med in enumerate(medications):
				if f'{med.medName}' in voiceStr:
					individualDrug.individualDrug(UIController, med.medName)
	elif UIController.currentLocation == "ScanBottle":
		if medications != None:
			for index, med in enumerate(medications):
				if f'{med.medName}' in voiceStr:
					individualEdit.individualEdit(UIController, med.medName, None)
	if 'add' in voiceStr:
		UIController.goToScanBottle()
		UIController.openBottleScanner()
	elif 'edit' in voiceStr:
		UIController.goToScanBottle()
		UIController.editBottleInfo()
	elif 'scan' in voiceStr:
		UIController.goToScanBottle()
	elif 'drug' in voiceStr:
		UIController.goToDrugInfo()
	elif 'confirmation' in voiceStr:
		UIController.goToConfirm(hour=date[0],minute=date[1])
	elif 'report' in voiceStr:
		UIController.goToReport()
	else:
		print("try again")
# Call the function 
# command()