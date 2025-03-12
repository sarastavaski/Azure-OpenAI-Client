# Azure-OpenAI-Client
Fourth Wing AI Companion
 
Welcome to the Fourth Wing AI Companion, your personal AI-powered assistant inspired by the world of Fourth Wing. This app allows users to ask questions and receive wise answers from a dragon AI, perfect for fans of the fantasy genre!
 

Features
 

Dragon Image and Chat Interface: Interact with a dragon-themed UI that feels immersive.
AI-Powered Responses: Submit your questions about Fourth Wing, and the AI will provide thoughtful and helpful responses.
Responsive Design: The app works on various screen sizes and devices.
 

Getting Started
 
Follow these steps to set up and run the app locally or on a server.

Prerequisites
 
Ensure you have the following installed:

Python 3.x: The app uses Python as its backend.
Flask: A lightweight web framework for Python.
Git: For cloning the repository.
A modern web browser (e.g., Chrome, Firefox, Edge).
 

Installation
 

Clone the Repository:

git clone https://github.com/your-repo-name/fourth-wing-ai-companion.git  
cd fourth-wing-ai-companion  
 
2. Set Up a Python Virtual Environment (Optional but recommended):


python -m venv venv  
source venv/bin/activate  # On Windows: venv\Scripts\activate  
 
3. Install Dependencies:
Install the required Python packages listed in requirements.txt.


pip install -r requirements.txt  
 
4. Run the App:
Start the Flask development server.


python app.py  
Once the server starts, you'll see output similar to:

* Running on all addresses (0.0.0.0)  
* Running on http://127.0.0.1:5000  
* Running on http://<your-ip>:5000  
 
5. Access the App:
Open your browser and visit http://127.0.0.1:5000 or your machine's IP.
 

Deployment
 
To make the app accessible to others, you can deploy it to a hosting service like Heroku, AWS, or Google Cloud.

Example Deployment on Heroku:
 

Install the Heroku CLI:

npm install -g heroku  
 
2. Log in to Heroku:


heroku login  
 
3. Create a new Heroku app:


heroku create fourth-wing-ai-companion  
 
4. Push the code to Heroku:


git add .  
git commit -m "Deploy app"  
git push heroku master  
 
5. Open the app:


heroku open  
 
 

File Structure
 


fourth-wing-ai-companion/  
│  
├── static/  
│   └── dragon.png             # Dragon image used in the app  
│  
├── templates/  
│   └── index.html             # Main HTML file for the app  
│  
├── app.py                     # Flask app script  
├── requirements.txt           # Python dependencies  
├── README.md                  # Documentation for the repo  
└── .gitignore                 # Files to ignore in version control  
 