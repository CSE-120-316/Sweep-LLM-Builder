# Chat-Cats

## Commands

Start up docker containers:
    docker-compose up

Shut down docker containers:
    docker-compose down

Connect to the database:
    psql -h localhost -p 5432 -U user -d mydb

# Commands for LLM setup
cd LLM_Code

python -m venv LLAMA

source LLAMA/bin/activate

pip install -r llm_requirements.txt

python hf_finetune.py
