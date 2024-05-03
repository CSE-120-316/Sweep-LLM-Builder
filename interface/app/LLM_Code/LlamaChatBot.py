# Rohit Rao
# Llama2 Chatbot Object.
# 4/12/2024

import os   
import torch
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, TrainingArguments, pipeline, logging
from peft import LoraConfig, AutoPeftModelForCausalLM
from trl import SFTTrainer
import gc
from huggingface_hub import login


class LlamaChatBot:
    def __init__ (self, newModel = ""):
        self.newModel = newModel

        gc.collect()

        login(token='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') # my token to for access to meta llama 2 if needed
        compute_dtype = getattr(torch, "float16")
        quant_config = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4", bnb_4bit_compute_dtype=compute_dtype, bnb_4bit_use_double_quant=False)


        # Load model with 4-bit precision
        self.model = AutoPeftModelForCausalLM.from_pretrained(self.newModel, quantization_config=quant_config, device_map={"": 0})
        self.model.config.use_cache = False
        self.model.config.pretraining_tp = 1


        # Load tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(self.newModel, trust_remote_code=True)
        self.tokenizer.pad_token = self.tokenizer.eos_token
        self.tokenizer.padding_side = "right"


        # Force clean the pytorch cache
        gc.collect()
        torch.cuda.empty_cache()

    def respond(self, prompt=""):
        logging.set_verbosity(logging.CRITICAL)
        pipe = pipeline(task="text-generation", model=self.model, tokenizer=self.tokenizer, max_length=100)
        result = pipe(f" <s>[INST] {prompt} [/INST]")
        return(result[0]['generated_text'],"\n")

if __name__ == "__main__":
    ChatBotObj = LlamaChatBot("")
    print(ChatBotObj.respond("Hello does this work?"))