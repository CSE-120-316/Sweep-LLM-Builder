sudo apt-get install wget
sudo apt-get install git

git clone https://github.com/meta-llama/llama /app/llm-repos/

#! RUN THE LINES BELLOW TO INSTALL THE LLAMA MODEL, OTHERWISE PLACE IT IN THE VOLUME MANUALLY

# # Set environment variable values
# UNIQUE_LLAMA_URL=${UNIQUE_LLAMA_URL}
# MODEL="7B-chat"

# cd /app/llm-repos/llama
# download.sh "$UNIQUE_LLAMA_URL" "$MODEL"