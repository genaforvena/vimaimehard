import sys
import command_converter

def process_request(user_input):
    command = command_converter.get_command(user_input)
    return command

if __name__ == "__main__":
    user_input = ' '.join(sys.argv[1:])  # Combine all arguments into one string
    result = process_request(user_input)
    print(result)  # Print the result, which will be captured by Vim

