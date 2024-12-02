# Ollama directly
ollama ls
ollama run llama3.2

# Custom models
ollama create -f modelfile-mario mario
ollama run mario
Do you know of any good mushrooms?
Who do you fear the most?
# API
curl -XPOST -H "Content-Type: application/json" http://localhost:11434/v1/chat/completions -d '{"model": "llama3.2", "messages": [{"role": "users", "content": "How are you today?"}]}'
curl http://localhost:11434/api/generate -d '{
  "model": "llama3.2",
  "prompt": "Why is the sky blue?",
  "stream": false
}'


# modelfiles for ollama
ollama create mario -f modelfile.mario
ollama run mario

# Python api 
https://github.com/ollama/ollama-python

main.py -> Direct
api.py -> Direct with fastapi on top

## Fast api
fastapi dev api.py

curl --header "Content-Type: application/json" -X POST -d '{"question": "how much is the fish?"}' http://localhost:8000/ask



## Open webui


### bru test api
bru run api.bru -o test.json

## Web search using searchxng
add this to openwebui: http://<searxng.local>/search?q=<query>

# Open webui docs
https://docs.openwebui.com/features/web_search/

# Open webui sso: 
https://docs.openwebui.com/features/sso