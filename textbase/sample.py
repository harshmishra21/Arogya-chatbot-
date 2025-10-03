import ollama

# Generate a response
response = ollama.chat(
    model="meditron",
    messages=[
        {"role": "system", "content": """You are chatting with a Medical Assistant. 
I can provide information on medical topics and answer health-related questions. 
Please remember that I'm not a substitute for professional medical advice. 
If you have a medical emergency, please call emergency services immediately."""},
        {"role": "user", "content": "What medication would be prescribed for a headache?"}
    ]
)

print(response['message']['content'])
