import os
import sys
from openai import OpenAI

# Retrieve OpenAI API key from environment variable
api_key = os.getenv('OPENAI_API_KEY')

if not api_key:
    raise ValueError("OPENAI_API_KEY is not set in environment variables")

client = OpenAI(api_key=api_key)


def get_command(user_prompt):
    # Check if user prompt is provided
    if not user_prompt:
        raise ValueError("No user prompt provided")
    print("User prompt: " + user_prompt)
    # Refine the user prompt using the OpenAI API
    prompt_for_refinement = (
        "Convert the user request into a precise command for Vim. Send only vim command and nothing more:\n"
        "User request: '{}'\n"
        "Vim command description:".format(user_prompt)
    )

    refined_prompt = client.completions.create(model='babbage',
                                               prompt=prompt_for_refinement
                                               ).choices[0].text.strip()
    print("Refined prompt: " + refined_prompt)
    # Generate a response with Vim commands using the OpenAI API
    vim_commands = client.completions.create(model='babbage',
                                             prompt=refined_prompt
                                             ).choices[0].text.strip()
    print("Suggested command: " + vim_commands)
    return vim_commands

