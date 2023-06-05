import speech_recognition as sr


class Listener:
    '''Class to listen to the user's commands.'''
    
    def __init__(self) -> None:
        '''Initializes the speech recognizer.'''
        self.r = sr.Recognizer()
        # adjusting for ambient noise
        self.r.pause_threshold = 0.5
        self.r.energy_threshold = 500


    def listen(self) -> tuple[str, bool]:
        with sr.Microphone() as source:
            audio = self.r.listen(source)
            try:
                query = self.r.recognize_google(audio, language='en')
            except Exception as e:
                return "", False
            
            print(query)
            return query, True
        