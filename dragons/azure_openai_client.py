import os  
from flask import Flask, request, jsonify, render_template  
from openai import AzureOpenAI  
  
# Azure OpenAI Configuration  
api_key = os.environ["AZURE_OPENAI_API_KEY"]  
azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"]  
deployment_name = "gpt-4o-mini"  # Replace with your model deployment name  
  
  
class AzureOpenAIClient:  
    """Azure OpenAI Client to interact with the Azure OpenAI API."""  
  
    def __init__(self):  
        """Creates an Azure OpenAI client."""  
        self.client = AzureOpenAI(  
            api_key=api_key,  
            api_version="2024-02-01",  
            azure_endpoint=azure_endpoint,  
        )  
  
    def create_completion(  
        self,  
        user_prompt: str,  
        system_prompt: str = "You are a wise dragon at Basgiath War College.",  
    ) -> str:  
        """Generates a response to a single prompt."""  
        response = self.client.chat.completions.create(  
            model=deployment_name,  
            messages=[  
                {"role": "system", "content": system_prompt},  
                {"role": "user", "content": user_prompt},  
            ],  
        )  
        completion = response.choices[0].message.content  
        return completion  
  
  
# Initialize Flask app and Azure OpenAI client  
app = Flask(__name__)  
openai_client = AzureOpenAIClient()  
  
  
@app.route("/")  
def home():  
    """Renders the homepage with an input form."""  
    return render_template("index.html")  
  
  
@app.route("/ask-dragon", methods=["POST"])  
def ask_dragon():  
    """Handles user input, generates a response from the Azure OpenAI API, and returns it."""  
    user_input = request.json.get("question", "")  
  
    if not user_input:  
        return jsonify({"error": "Question cannot be empty"}), 400  
  
    try:  
        # Generate a response using the Azure OpenAI client  
        dragon_response = openai_client.create_completion(user_prompt=user_input)  
        return jsonify({"response": dragon_response})  
    except Exception as e:  
        return jsonify({"error": str(e)}), 500  
  
  
if __name__ == "__main__":  
    app.run(host="0.0.0.0", port=5000)  
