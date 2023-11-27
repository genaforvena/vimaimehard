"""
This module contains a function that takes a Vim command history in JSON
format and returns optimized command suggestions using the OpenAI API.
"""
import os
import sys
import json
from openai import OpenAI

# Retrieve OpenAI API key from environment variable or set directly
api_key = os.getenv('OPENAI_API_KEY')

# Initialize OpenAI client
client = OpenAI(api_key=api_key)


def get_command(json_history):
    """
    This function takes a Vim command history in JSON format and returns
    optimized command suggestions using the OpenAI API.
    """
    # Deserialize the JSON string to a Python list
    history = json.loads(json_history)

    # Construct a prompt for the OpenAI model
    prompt = "Here is a list of Vim commands performed by a user:\n"
    # Add each command to the prompt
    for command in history:
        prompt += command + "\n"
    # Add a prompt for the OpenAI model to analyze the commands
    prompt += "Analyze these commands and provide a more "
    prompt += "efficient way to achieve the same results:\n"
    # Add the current user request to the history
    message_history = []
    message_history.append({"role": "user", "content": prompt})

    # Generate a response with Vim command using the OpenAI API Chat Completion
    chat_completion = client.chat.completions.create(model='gpt-3.5-turbo',
                                                     messages=message_history)

    # Extract the response from the completion
    vim_command_response = chat_completion.choices[0].message.content

    return vim_command_response


# Example usage
if __name__ == "__main__":
    history_json = sys.argv[1]
    optimized_commands = get_command(history_json)
    print(optimized_commands)
