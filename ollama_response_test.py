from langchain_ollama import OllamaLLM
import requests
import json
import time

s=time.time()

url = 'https://clchatagentassessment.s3.ap-south-1.amazonaws.com/queries.json'  # Replace with the actual URL
response = requests.get(url)
queries = json.loads(response.text)


generated_response=[]
for query in queries:
    
    messages=[]
    timestamp=[]
    model=OllamaLLM(model="llama3.1")
    for i in range(len(query['chat_context']['chat_history'])):
        messages.append(query['chat_context']['chat_history'][i]['message'])
    
    for i in range(len(query['chat_context']['chat_history'])):
        timestamp.append(query['chat_context']['chat_history'][i]['timestamp'])
        
    prompt = f"""
    You are the personal nutrition expert who created the diet plan for the patient. Respond to their latest meal update:

Patient profile: {query['profile_context']['patient_profile']}
Diet chart: {query['profile_context']['diet_chart']}
Chat history: f"{messages} and its {timestamp}"
Latest query: {query['latest_query']}

Analysis steps:
1. strictly Compare the reported meal from the latest query with the prescribed diet for this specific day and time.
2. strictly compare the given meal picture  from the latest query with the diet chart , to check compliance(figure out whats missing from the patient's meal or if they consumed something which wasn't not prescribed)
3. Based on the above information, patient's medical profile, previous chat history, we try to give the patient specific actionable advice in a concise form typically in the same messaging language/style as the patient.

Response guidelines:
1. Address the patient by name if name is present
2. Acknowledge adherence to the diet plan with specific praise.
3. For any deviations, ask a direct question about why the change was made.
4. Provide a brief nutritional fact about a key food item mentioned.
5. If appropriate, suggest a small, specific improvement.
6. Keep the tone conversational,empathetic and supportive.
7. Give the Reponse in the same messaging language/style as the patient.
8. strictly Keep the response under 25 words, natural, and specific to the patient's situation.

Generate ONLY the response, without additional explanations or labels:
"""
    result=model.invoke(input=prompt)
    print(result)
    formatted_response = {
        "ticket_id": query['chat_context']['ticket_id'],
        "latest_query": query['latest_query'],
        "generated_response": result,
        "ideal_response": query['ideal_response']  # Use an empty string if 'ideal_response' is not provided
    }
    generated_response.append(formatted_response)
    
with open('output3.json', 'w', encoding='utf-8') as f:
    json.dump(generated_response, f, ensure_ascii=False, indent=2)

print(f"All responses have been saved to output.json")  
f=time.time()
final=f-s
print(final)
#print(generated_response)
#result=model.invoke(input=prompt)


    
#print(formatted_response)



'''
Guidelines for the response:
    1. Start with a positive reinforcement for any part of the meal that aligns with the diet plan.
    2. Address the patient by name if available.
    3. If there are any deviations from the prescribed diet, mention them and ask for clarification in a friendly manner.
    4. Keep the tone conversational and supportive.
    5. Provide brief, actionable advice related to their specific health goals.
    6. Respond only in the Patient's Preferred Language.
    7. The response should be concise, around 2-3 sentences.
'''