import os
from openai import OpenAI

# Retrieve OpenAI API key from environment variable or set directly
api_key = os.getenv('OPENAI_API_KEY')

# Initialize OpenAI client
client = OpenAI(api_key=api_key)


def get_command(user_prompt):
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
        {"role": "assistant", "content": ">'}"}
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
    user_input = ' '.join(sys.argv[1:])
    print(get_command(user_input))

