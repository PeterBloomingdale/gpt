# Description: This file contains the code to call the GPT API
# Function takes a string as input and returns a string as output
import openai
import secrets

# Import API Key and Organization ID from secrets.py
openai.api_key = secrets.API_Key 
openai.organization = secrets.Organization_ID 

# Functions to call GPT API
# Input is a string (question = "What is the difference between a class and a function?")
class GPT:
    def __call__(self, question):
        model = "gpt-3.5-turbo" 

        response = openai.ChatCompletion.create( 
            model=model,
            messages=[
                {"role": "system", "content": "You are the worlds best software engineer."},
                {"role": "user", "content": question},
            ],
            temperature=0.9,
            max_tokens=500,
            top_p=0.9,
            n=1,
        )

        return response.choices[0].message.content

# Input is a .txt file (input.txt)
class GPTTXT:
    def __call__(self, input_file_path):
        with open(input_file_path, 'r') as f:
            input_string = f.read()

        model = "gpt-3.5-turbo"

        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are the worlds best software engineer."},
                {"role": "user", "content": input_string},
            ],
            temperature=0.9,
            max_tokens=300,
            top_p=0.9,
            n=1,
        )

        return response.choices[0].message.content

gpt = GPT()
gpttxt = GPTTXT()


