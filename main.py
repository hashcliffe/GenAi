# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 02:18:01 2024

@author: Welcome
"""

from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

class ModelInput(BaseModel):
    question: str

class QaChainWrapper:
    def __init__(self, qa_chain):
        self.qa_chain = qa_chain

    def ask_question(self, question):
        return self.qa_chain["qa_function"]({"query": question})

# Load the model from model_data.json
with open('model_data.json', 'r') as file:
    model_data = json.load(file)
    #print(qa_chain_model)
    qa_chain_model = model_data['qa_chain']
    qa_chain_wrapper = QaChainWrapper(qa_chain_model)

@app.post('/rag_genai')
def rag_gen(input_parameters: ModelInput):
    question = input_parameters.question
    try:
        result = qa_chain_wrapper.ask_question(question)
        return result["result"]
    except Exception as e:
        return {"error": str(e)}
