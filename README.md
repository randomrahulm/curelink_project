

# Curelink Project

This project utilizes the `OllamaLLM` model to generate personalized, concise responses for patients based on their dietary history, diet chart, and latest meal updates. The responses are intended to provide specific, actionable advice that aligns with the patient's health goals while maintaining a conversational and empathetic tone.

## Project Overview

### Functionality

1. **Fetch Queries**: Retrieves a set of queries in JSON format from a specified URL.
2. **Process Each Query**:
   - Extracts key information including the patient's profile, diet chart, chat history, and latest meal query.
   - Constructs a detailed prompt that incorporates the patient's context and instructions for generating a response.
   - Uses the `OllamaLLM` model to generate a response.
3. **Store Responses**: Saves the generated responses along with their corresponding queries in a JSON file (`output.json`).

### Prerequisites

- **Python 3.7+**: Ensure Python is installed on your system.
- **Required Python Libraries**:
  ```bash
  pip install requests json langchain_ollama ollama
  ```

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/randomrahulm/curelink_project.git
cd curelink_project
pip install -r requirements.txt
```

### 2. Run the Script

```bash
python ollama_reponse_test.py
```

### 3. View the Output

The generated responses will be saved in `output.json` in the root directory of the project.

## Detailed Documentation

### Script Breakdown

1. **Importing Required Libraries**:
   - `requests`: For fetching the JSON data from the URL.
   - `json`: For parsing and handling JSON data.
   - `time`: For measuring the execution time of the script.
   - `OllamaLLM` from `langchain_ollama`: The model used to generate responses.

2. **Fetching and Parsing Data**:
   - The script sends a GET request to the provided URL to fetch the queries in JSON format.
   - It then parses the JSON data into a Python dictionary for further processing.

3. **Processing Each Query**:
   - **Extracting Information**: The script loops through each query to extract the patient's profile, diet chart, chat history, and the latest query.
   - **Constructing the Prompt**: A detailed prompt is created that includes all relevant patient information and instructions for the model on how to generate the response.
   - **Generating the Response**: The prompt is fed into the `OllamaLLM` model, which generates a response based on the provided context.
   - **Formatting the Response**: The generated response is formatted and stored along with the original query data.

4. **Saving the Responses**:
   - The formatted responses are saved in `output.json` for easy access and review.

### Example Query Structure

Each query is expected to follow a specific JSON structure:

```json
{
  "profile_context": {
    "patient_profile": "Patient details here",
    "diet_chart": "Diet chart details here"
  },
  "chat_context": {
    "ticket_id": "unique_ticket_id",
    "chat_history": [
      {
        "message": "Previous message from patient",
        "timestamp": "timestamp_here"
      }
    ]
  },
  "latest_query": "Patient's latest query here",
  "ideal_response": "Expected ideal response here (optional)"
}
```

### Response Guidelines

The generated response follows these guidelines:

1. **Positive Reinforcement**: Praise any part of the meal that aligns with the diet plan.
2. **Personalization**: Address the patient by name if available.
3. **Deviation Handling**: Mention any deviations from the prescribed diet and ask for clarification in a friendly manner.
4. **Nutritional Advice**: Provide a brief, actionable piece of advice related to the patient's health goals.
5. **Tone and Style**: Keep the tone conversational, empathetic, and supportive. Match the patient's language/style.
6. **Conciseness**: Keep the response under 25 words.

## Execution Time

The script prints the total execution time, allowing you to gauge the performance.

