import win32com.client


class Speaker:
    '''Class to speak the response.'''
    def __init__(self):
        '''Initializes the speaker.'''
        self.speaker = win32com.client.Dispatch("SAPI.SpVoice")

    def say(self, text: str):
        '''Speaks the text.'''
        self.speaker.Speak(text)