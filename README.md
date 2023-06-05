
# Nova

Nova is an AI-based voice assistant designed to help with basic tasks. It uses the AI algorithms developed by OpenAI to understand and respond to user commands and queries in a conversational manner. This voice assistant aims to provide a convenient and efficient way to interact with your devices and perform various actions without the need for manual input.



## Features

- Voice commands to open websites
- Voice commands to start applications
- AI chatbot
- Saves AI responses to a text file


## Getting Started

1. Clone the VoiceAssistant-Nova repository to your local **Windows** machine.
2. Install the required modules listed in the '**requirements.txt**' file.
3. Add your OpenAI key and name to config.py file. API key can be generated [here](https://openai.com/blog/openai-api).
4. Add the websites and applications you wish to access using Nova to '**websites.json**' and '**applications.json**' respectively.
5. Run '**main.py**'.

## How to use Nova
- Each command must have '**Nova**' in it's sentence.
- Nova tries to keep track of chat history. Using voice commands such as "**Nova forget everything**", "**Nova clear chat**", and "**Nova reset chat**" periodically will help reduce memory usage.
- To open websites: "Nova open site YouTube", etc.
- To start applicatioins: "Nova start Chrome" or "Nova open chrome", etc.
- To get AI responses: "Nova give me an easy chocolate cake recipe", etc.
    
## License

VoiceAssistant-Nova is licensed under the [MIT License](https://choosealicense.com/licenses/mit/). See the '**LICENSE**' file for more details.


## Acknowledgements

Nova is built upon the powerful language model GPT-3 by OpenAI. I would like to express my gratitude to the entire team at OpenAI for their groundbreaking research and contributions to the field of artificial intelligence.


## Disclaimer

Nova is a personal project created for educational and demonstration purposes. While efforts have been made to ensure the accuracy and reliability of the information and functionalities provided, a guarantee of their completeness or suitability for any specific purpose cannot be granted.
