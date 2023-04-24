from gpt import gpt

# Set the initial prompt
prompt = "Hi, I would like to have a discussion. What should we talk about?"

# Loop to make the two LLMs have a conversation
for i in range(5):
    # Bot 1 responds to the prompt
    response1 = gpt(prompt)

    # Bot 2 responds to Bot 1's response
    response2 = gpt(response1)

    # Print the conversation
    print(f"Bot 1: {response1}")
    print(f"Bot 2: {response2}")

    # Set the next prompt to be Bot 2's response
    prompt = response2