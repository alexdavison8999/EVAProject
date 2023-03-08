import speech_recognition as sr 

# Initialize the speech recognition 
r = sr.Recognizer() 

# Create a function that will be called when the command is given  
def record_speech(): 
	# Record the command from the microphone 
	with sr.Microphone(device_index=1) as source: 
		print("Listening...") 
		r.pause_threshold = 1
		audio = r.listen(source) 
	
	try: 
		# Use the Google Speech Recognition API 
		command = r.recognize_google(audio).lower() 
		print("You said: " + command + "\n") 
	
	# Error handling 
	except sr.UnknownValueError: 
		print("I couldn't understand you. Please try again.") 
	
	return command 

# Call the function 
# command()