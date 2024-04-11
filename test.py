# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 03:26:51 2024

@author: Welcome
"""

import requests

# Define the API endpoint URL
api_url = "http://127.0.0.1:8000/rag_genai"

# Define the input data
input_data = {"question": "Tell me about crm"}

# Send a POST request to the API endpoint
response = requests.post(api_url, json=input_data)

# Print the response
print(response.json())