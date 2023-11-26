"""
This module contains a function that takes a user prompt and returns a Vim
command using the OpenAI API Chat Completion.
"""
import os
import sys
from openai import OpenAI

# Retrieve OpenAI API key from environment variable or set directly
api_key = os.getenv('OPENAI_API_KEY')

# Initialize OpenAI client
client = OpenAI(api_key=api_key)


def get_command(user_prompt):
    """
    This function takes a user prompt and returns a Vim command using the
    OpenAI API Chat Completion.
    """
    # Check if user prompt is provided
    if not user_prompt:
        raise ValueError("No user prompt provided")

    # Advanced examples as messages
    message_history = [
        {"role": "system", "content": "You are a helpful assistant knowledgeable in Vim commands."},
        {"role": "user", "content": "How to delete a line in Vim?"},
        {"role": "assistant", "content": "dd"},
        {"role": "user", "content": "How to save a file in Vim?"},
        {"role": "assistant", "content": ":w"},
        {"role": "user", "content": "How to replace 'foo' with 'bar' in the entire file?"},
        {"role": "assistant", "content": ":%s/foo/bar/g"},
        {"role": "user", "content": "How do I jump to the end of the file?"},
        {"role": "assistant", "content": "G"},
        {"role": "user", "content": "How to comment out a block of text?"},
        {"role": "assistant", "content": ":'<,'>s/^/# /"},
        {"role": "user", "content": "How to search and replace across multiple files?"},
        {"role": "assistant", "content": ":argdo %s/search/replace/gc | update"},
        {"role": "user", "content": "How to indent a code block?"},
        {"role": "assistant", "content": ">'}"},
        {"role": "user", "content": "How to fold all function definitions in a Python file?"},
        {"role": "assistant", "content": "set foldmethod=indent\nset foldlevel=99\nzf/%def\\s.*/"},
        {"role": "user", "content": "How do I merge lines 5 through 10 into a single line?"},
        {"role": "assistant", "content": ":5,10join"},
        {"role": "user", "content": "What's the command to move the current line up by 3 lines?"},
        {"role": "assistant", "content": ":m-4"},
        {"role": "user", "content": "How can I delete every third line starting from line 2?"},
        {"role": "assistant", "content": ":2,$g/^/+2d"},
        {"role": "user", "content": "How to encrypt the current file with a ROT13 cipher?"},
        {"role": "assistant", "content": ":%!tr 'A-Za-z' 'N-ZA-Mn-za-m'"},
        {"role": "user",
         "content":
         "How do I convert a list of comma-separated values into a vertical list in Vim?"},
        {"role": "assistant", "content": ":%s/,/\\r/g"},
        {"role": "user", "content": "How to highlight all occurrences of a word under the cursor?"},
        {"role": "assistant", "content": "set hlsearch\n/\\<\\w\\+\\>"},
        {"role": "user",
         "content": "How can I sort the lines in the current file in reverse order?"},
        {"role": "assistant", "content": ":%sort! r"},
        {"role": "user", "content": "How to automatically format a JSON file?"},
        {"role": "assistant", "content": ":%!python -m json.tool"},
        {"role": "user",
         "content": "What is the command to display all lines not containing the word 'error'?"},
        {"role": "assistant", "content": ":v/error/p"}
    ]

    # Add the current user request to the history
    message_history.append({"role": "user", "content": user_prompt})

    # Generate a response with Vim command using the OpenAI API Chat Completion
    chat_completion = client.chat.completions.create(model='gpt-3.5-turbo',
                                                     messages=message_history)

    # Extract the response from the completion
    vim_command_response = chat_completion.choices[0].message.content

    return vim_command_response

# Example usage
if __name__ == "__main__":
    USER_INPUT = ' '.join(sys.argv[1:])
    print(get_command(USER_INPUT))
