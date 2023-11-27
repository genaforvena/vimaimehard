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
        {
            "role": "user",
            "content": "What's the best way to compare two vertically split files in Vim?"
        },
        {
            "role": "assistant",
            "content": "To compare two files side by side in Vim, you can use the `:vsplit` "  +
            "command to open the files|" + \
            "in vertical splits and then use `:windo diffthis` to activate Vim's " +
            "diff mode on both windows."
        },
        {
            "role": "user",
            "content": "How to record and play a macro in Vim?"
        },
        {
            "role": "assistant",
            "content": "To record a macro, press `q` followed by a letter to store" +
            "the macro (e.g., `qa`). Then, perform the desired actions." +
            "Stop recording by pressing `q` again. To play the macro," +
            " press `@` followed by the letter where the macro is stored (e.g., `@a`)."
        },
        {
            "role": "user",
            "content": "Explain how to use Vim's global command to change text in multiple lines."
        },
        {
            "role": "assistant",
            "content": "The global command `:g` in Vim is powerful for " +
            "making changes in multiple lines. For example, `:g/foo/s//bar/g` " +
            "will find all lines containing 'foo' and replace 'foo' with 'bar' in those lines."
        },
        {
            "role": "user",
            "content": "How do I create a folding in Vim based on syntax?"
        },
        {
            "role": "assistant",
            "content": "To create folds based on syntax in Vim, use `:set foldmethod=syntax`. " +
            "Vim will automatically create folds according to the " +
            "syntax of the programming language of the file."
        },
        {
            "role": "user",
            "content": "Is there a way to use regular expressions for advanced search in Vim?"
        },
        {
            "role": "assistant",
            "content": "Yes, Vim supports using regular expressions for searching. " +
            "For example, `:/\\<foo\\>` searches for the word 'foo'. " +
            "You can use complex patterns like `:/\\d\\+` to search for one or more digits."
        }
    ]

    prompt_for_command = f"""
    Provide the top 5 Vim commands for the following request and explain how each command works:
    User request: '{user_prompt}'
    Vim commands and explanations:
    """

    # Add the current user request to the history
    message_history.append({"role": "user", "content": prompt_for_command})

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
