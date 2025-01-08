import ollama


print(f"Asking llama3.2 to behave as a pirate")
response = ollama.chat(model='llama3.2', messages=[
  {
    'role': 'system', 
    'content': 'You are a pirate chatbot who always responds in pirate speak!'
    },
  {
    'role': 'user',
    'content': 'Who are you?'
  },
    {
    'role': 'user',
    'content': 'Who is the captain of the ship?'
  },
],
stream=False
)

print(response['message']['content'])



