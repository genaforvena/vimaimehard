import os
import sys
from openai import OpenAI

# Retrieve OpenAI API key from environment variable
api_key = os.getenv('OPENAI_KEY')

if not api_key:
    raise ValueError("OpenAI API key not set in environment variables")

client = OpenAI(api_key=api_key)


def get_command(user_prompt):
    # Check if user prompt is provided
    if not user_prompt:
        raise ValueError("No user prompt provided")
    # Refine the user prompt using the OpenAI API
    prompt_for_refinement = (
        "Convert the following user request into a precise command for Vim:\n"
        "User request: '{}'\n"
        "Vim command description:".format(user_prompt)
    )

    refined_prompt = client.completions.create(model='text-davinci-003',
                                               prompt=prompt_for_refinement
                                               ).choices[0].text.strip()

    # Generate a response with Vim commands using the OpenAI API
    vim_commands = client.completions.create(model='text-davinci-003',
                                             prompt=refined_prompt
                                             ).choices[0].text.strip()

    return vim_commands
