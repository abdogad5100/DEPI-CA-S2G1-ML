import random
import json

with open("D:/DEPI/CA-S2-G1-AI/DEPI-CA-S2G1-ML/src/python/session-4/chatbot/data.json","r") as file:

    responses = json.load(file)
    
def get_response(user_input):
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])    