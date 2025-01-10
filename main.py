import ollama
import random

question = random.choice([
    "Why is the sky blue?",
    "How many of the letter r, are there in the word 'Strawberry'?",
    "Can you tell me a joke?",
    "Can you write java code to print the 10 first fibonacci numbers?",
    "Can you write python code to print the 10 first fibonacci numbers?",
    "What is a common dish people eat a lot in Norway",
    "What is the capital of France?",
    "What is the capital of Norway, and what is the population of Norway?",
    "What are the four bigget cities in Norway?",
    "Outside of Norway, what city in another country has the most similiar climate to Bergen?"
])

print(f"Asking llama3.2: {question}")

result = ollama.generate(model="llama3.2", prompt=question)


print(result)
print("===========")
print(result["response"])

