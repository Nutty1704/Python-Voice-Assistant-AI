import json
import webbrowser
import os
from config import openai_key
import openai


class Processor:
    '''Class to process the command given by the user.'''

    def __init__(self) -> None:
        '''Initializes the processor.'''
        self.websites_src = "websites.json"
        self.applications_src = "applications.json"
        self.chat_history = ""


    def process_command(self, command: str) -> str:
        '''Processes the command and returns the response.
        
        Parameters:
            command (str): The command given by the user.
            
        Returns:
            str: The response to the command.
        '''

        # If the command contains the word 'open site', open the website.
        if 'open site' in command.lower():
            return self.open_website(command)
        
        # If the command contains the word 'open' or 'start', open the application.
        elif 'open' in command.lower() or 'start' in command.lower():
            return self.open_application(command)
        
        # If the command contains the word 'using ai', use the AI to generate a response.
        elif 'using ai' in command.lower():
            return self.ai_response(command)
        
        # If the command is to erase the chat history, clear the chat history.
        elif 'reset chat' in command.lower() or 'clear chat' in command.lower() or 'forget everything' in command.lower():
            self.chat_history = ""
            return "Chat history cleared."
    
        # else, pass the command to the chat bot.
        else:
            return self.chat(command)

    
    def chat(self, query: str):
        '''Uses the chat bot to generate a response.
        
        Parameters:
            query (str): The query given by the user.
            
        Returns:
            str: The response to the query.
        '''
        openai.api_key = openai_key

        # creating prompt for the chat bot using the chat history and the query
        prompt = self.chat_history + f"Abhi: {query}\n Nova: "

        # generating response using the prompt, using gpt-3
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )

        # extracting the response from the response object
        try:
            response_text = response["choices"][0]["text"].lstrip("\n")
        # if the response is empty, return an error message
        except Exception as e:
            print(f"Query: {query}\nError: {e}")
            return "I'm sorry, I couldn't generate a response using AI."
        else:
            # splitting the response into sentences
            sentences = response_text.split("\n")
            # if the response has more than 5 sentences, read first 5 sentences and save the response to a file
            if len(sentences) > 5:
                speech_text = ". ".join(sentences[:5])
                self.save_ai_response(response_text, query)
                speech_text += f".\nI have saved the rest of the response to ai_responses folder in a file named {query}.txt"

            # if the response has less than 5 sentences, read the whole response
            else:
                speech_text = response_text

        # updating the chat history
        self.chat_history += prompt + speech_text + "\n"
        return speech_text
        
    
    def open_website(self, command: str) -> str:
        '''Opens the website given by the user.
        
        Parameters:
            command (str): The command given by the user.
            
        Returns:
            str: The response to the command.
        '''
        # opening the websites.json file
        file = open(self.websites_src, "r")
        data = file.read()

        obj = json.loads(data)
        
        # searching for the website in the json file
        for key in obj:
            if key in command.lower():
                link = obj[key]
                webbrowser.open(link)
                return f"Opening {key}"
            
        # if the website is not found, return an error message
        file.close()
        return "I'm sorry, I couldn't find that website."
    

    def open_application(self, command: str) -> str:
        '''Opens the application given by the user.
        
        Parameters:
            command (str): The command given by the user.
            
        Returns:
            str: The response to the command.
        '''
        file = open(self.applications_src, "r")
        data = file.read()

        obj = json.loads(data)

        # searching for the application in the json file
        for key in obj:
            if key in command.lower():
                app_location = obj[key]
                app_location.replace('\\\\', '\\')
                os.startfile(app_location)
                return f"Starting {key}"
            
        # if the application is not found, return an error message
        file.close()
        return "I'm sorry, I couldn't find that application."

    
    def ai_response(self, command: str) -> str:
        '''Generates ai response and saves it to a file when the user does not want to chat.
        
        Parameters:
            command (str): The command given by the user.
            
        Returns:
            str: The response to the command.
        '''
        # This part of code is from OpenAI's API documentation (Playground)
        openai.api_key = openai_key

        # generating response using the prompt, using gpt-3
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=command,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )

        # extracting the response from the response object
        try:
            response_text = response["choices"][0]["text"]
        # if the response is empty, return an error message
        except Exception as e:
            print(f"Command: {command}\nError: {e}")
            return "I'm sorry, I couldn't generate a response using AI."
        
        # saving the response to a file
        file_name = command.lstrip("using ai")
        self.save_ai_response(response_text, file_name)
        return f"Generated response using AI. Saved to ai_responses folder under {file_name}.txt"
    
    
    def save_ai_response(self, response: str, file_name: str) -> str:
        '''Saves the response generated by the AI to a text file.
        
        Parameters:
            response (str): The response generated by the AI.
            file_name (str): The name of the file to save the response to.
            
        Returns:
            str: The response to the command.
        '''
        # creates a folder named ai_responses if it does not exist
        if not os.path.exists("ai_responses"):
            os.mkdir("ai_responses")

        # saves the response to a file
        with open(f"ai_responses/{file_name}.txt", "w") as f:
            f.write(response)
