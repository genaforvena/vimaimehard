import sys

def process_request(user_input):
    # Implement the logic to call OpenAI API and process the response
    # For demonstration, let's just return the input
    return "Processed: " + user_input

if __name__ == "__main__":
    user_input = ' '.join(sys.argv[1:])  # Combine all arguments into one string
    result = process_request(user_input)
    print(result)  # Print the result, which will be captured by Vim

