from listener import Listener
from speaker import Speaker
from processor import Processor


class VoiceAssistant:
    '''Class to run the voice assistant.'''
    def __init__(self) -> None:
        '''Initializes the listener, speaker and processor for the assistant.'''
        self.listener = Listener()
        self.speaker = Speaker()
        self.processor = Processor()

    def run(self):
        '''Runs the voice assistant.'''
        while True:
            print("Listening...")
            command, valid = self.listener.listen()

            # If the command is not valid or does not contain the word 'nova', ignore it.
            if not valid or 'nova' not in command.lower():
                continue

            # If the command contains the words 'quit' or 'exit', break the loop.
            if 'nova quit' in command.lower() or 'nova exit' in command.lower():
                break

            # Process the command, get the response and speak it.
            response = self.processor.process_command(command)
            self.speaker.say(response)


if __name__ == "__main__":
    assistant = VoiceAssistant()
    assistant.run()