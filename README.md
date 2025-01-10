## ML VS AI
ML is the training of machine learning models
AI is a spesific subset of technologies in ML
- Image recognition
- Text Generation
- Audio to audio
- Text to Audio
- Image to Video
- etci

# AI models
An ai model is basicly a 
- Large compressed file file 
- containg a large collection of extremely large vectors (tensors) and metadata
  - context window size (metadata)
  - model based on (metadata)
  - name and dimensions of tensor ( actual data)
  - etc

 NB! Remeber to show bruno direct connection to ollama API where you will se the context (input) as a vector

# Huggingface
Show llama3.2 and 3.3 and code example

https://huggingface.co/docs/transformers/conversations

- Not hard but still some hoops to jump through
- No API
- Code duplication



# Ollama
- Wrapper around running models
- Same flow as docker
- exposes an API by default
- Can be run inside docker as well
- Portable
- Easy for anyone to test any model
  - both available on ollama's hub 
  - GGUF files, more work but not hard
https://huggingface.co/docs/hub/en/gguf
# Ollama directly
ollama ls
ollama run llama3.2

# Custom models
ollama create -f modelfile-mario mario
ollama run mario
Do you know of any good mushrooms?
Who do you fear the most?
What is your favorite thing to do?

# GGUF models
https://huggingface.co/docs/hub/en/ollama
ollama run hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF

# API

curl http://localhost:11434/api/chat -d '{
  "model": "llama3.2",
  "messages": [
    {
      "role": "user",
      "content": "How are you today?"
    }
  ]
}'




curl http://localhost:11434/api/generate -d '{
  "model": "llama3.2:3b",
  "prompt": "Why is the sky blue?",
  "stream": false
}'


# modelfiles for ollama
ollama create mario -f modelfile.mario
ollama run mario

# Python api 
https://github.com/ollama/ollama-python

pirate.py -> Direct
main.py -> Direct -> Skip this maybe?
api.py -> Direct with fastapi on top

## Fast api
fastapi dev api.py

curl --header "Content-Type: application/json" -X POST -d '{"question": "how much is the fish?"}' http://localhost:8000/ask

### bru test api
bru run api.bru -o test.json

## Open webui


## Web search using searchxng
add this to openwebui: http://<searxng.local>/search?q=<query>

# Open webui docs
https://docs.openwebui.com/features/web_search/

# Open webui sso: 
https://docs.openwebui.com/features/sso
