from __future__ import annotations

from datetime import datetime
import speech_recognition as sr 
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from UIController import UIController

# Initialize the speech recognition 
r = sr.Recognizer() 

# Create a function that will be called when the command is given  
def record_speech(UIController: UIController): 
	date = datetime.now().strftime("%H %M")
    date = date.split(" ")
	# Record the command from the microphone 
	with sr.Microphone() as source: 
		print("Listening...") 
		r.pause_threshold = 1
		audio = r.listen(source) 
	
	try: 
		# Use the Google Speech Recognition API 
		command = r.recognize_google(audio).lower() 
		navigateMenu(UIController, command)
		print("You said: " + command + "\n") 
	
	# Error handling 
	except sr.UnknownValueError: 
		print("I couldn't understand you. Please try again.") 
	
	return command 

def navigateMenu(UIController, voiceStr):
	if 'scan' in voiceStr:
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