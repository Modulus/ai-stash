from pydantic import BaseModel
import os

from fastapi.responses import (
    JSONResponse,
    StreamingResponse,
)
from fastapi.encoders import jsonable_encoder
from fastapi import FastAPI
from ollama import Client

app = FastAPI()

class UserInput(BaseModel):
    question: str

class Output(BaseModel):
    answer: str

def generate_answers(user_input: UserInput):
    OLLAMA_URL = os.environ.get('OLLAMA_BASE_URL', 'http://localhost:11434')

    client = Client(host=OLLAMA_URL)

    print(f"Talking to ollama on url: {OLLAMA_URL}")

    print(f"Asking llama3.2: {user_input.question}")
    response = client.chat(
        model='llama3.2', messages=[
            {
                'role': 'user',
                'content': user_input.question,
            },
        ],
        stream=False
    )
    return Output(answer=response['message']['content'])

@app.post("/ask", response_model=Output)
async def ask_question(user_input: UserInput):
    return JSONResponse( content=jsonable_encoder(generate_answers(user_input) ))

@app.post("/raw")
async def ask_question_raw(user_input: UserInput):
    return StreamingResponse( generate_answers(user_input).answer )

