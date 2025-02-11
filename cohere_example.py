import cohere

# Initialize the Cohere client with your API key
cohere_api_key = 'YOUR_COHERE_API_KEY'  # Replace with your actual API key
co = cohere.ClientV2(cohere_api_key)

# Sample flight cancellation policy
flight_cancellation_policy = """
If your flight is canceled, you may be entitled to a full refund or a rebooking on the next available flight. 
Please contact our customer service for assistance. 
In the case of severe weather or other extraordinary circumstances, we may not be able to provide compensation. 
Make sure to check your email for updates regarding your flight status.
"""

# Print the flight cancellation policy
print("Flight Cancellation Policy:")
print(flight_cancellation_policy)

# Use the Cohere API to generate a response based on the policy
response = co.chat(
    model="command-r-plus",
    messages=[
        {"role": "user", "content": "If your flight is canceled, you can get a refund or rebook. Check your email for updates. Summarize the cancellation policy."}
    ],
    max_tokens=20  # Limit output to 20 tokens
)


# Print the entire response to inspect its structure
print("\nFull Response:")
print(response)  # Highlighted: Added this line to inspect the full response structure

# Access the generated response content correctly
if 'messages' in response and len(response['messages']) > 0:  # Highlighted: Check for 'messages' key
    generated_response = response['messages'][-1]['content']  # Highlighted: Access the content of the last message
    
    # Extract the text content from the response
    response_text = generated_response[0]['text'] if isinstance(generated_response, list) else generated_response

    # Format the response into paragraphs for readability
    print("\nFormatted Response:")
    print(response_text.replace("\n\n", "\n\n"))  # Ensure double newlines are preserved for paragraph breaks
else:
    print("No response messages found.")
