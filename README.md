🤖 Chatbot API (Django + OpenRouter)

A simple FAQ Chatbot built with Django REST Framework and powered by OpenRouter AI models.
Users can ask questions via a REST API or through a minimal web interface, and the bot generates AI-powered answers.
All questions & answers are stored in a PostgreSQL database.



🚀 Features

REST API endpoint for asking questions (/api/faq/).

Simple frontend (/) to chat with the bot.

Stores all Q&A in the database.

Powered by OpenRouter (supports GPT, Claude, Mistral, LLaMA, etc).

Docker-ready for deployment.



🛠️ Tech Stack

Backend: Django 4.2, Django REST Framework

Database: PostgreSQL (default: faq_db)

AI Integration: OpenRouter API (chat/completions)

Frontend: HTML + JavaScript (Django template)

Deployment: Docker (Python 3.10 slim image)




📂 Project Structure
faq_chatbot/
├── manage.py
├── faq_chatbot/        # main Django project
├── chatbot/            # chatbot app
│   ├── models.py       # FAQ model
│   ├── serializers.py  # DRF serializers
│   ├── views.py        # API + UI logic
│   ├── urls.py         # routes
│   ├── templates/      # frontend templates
│   └── static/         # CSS/static assets
├── requirements.txt
├── Dockerfile
└── .env




⚡ Setup & Installation
1. Clone Repo
git clone https://github.com/your-username/faq-chatbot-api.git
cd faq-chatbot-api

2. Create Virtual Environment
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

3. Install Dependencies
pip install -r requirements.txt

4. Configure Environment Variables

Create a .env file in the project root:

OPENROUTER_API_KEY=your_openrouter_api_key


Get your API key from 👉 OpenRouter
.

5. Database Setup

Update database settings in faq_chatbot/settings.py if needed, then run:

python manage.py makemigrations
python manage.py migrate

6. Run Server
python manage.py runserver





Visit:

API → http://127.0.0.1:8000/api/faq/

UI → http://127.0.0.1:8000/

🧪 Example Usage
API Request
curl -X POST http://127.0.0.1:8000/api/faq/ \
  -H "Content-Type: application/json" \
  -d '{"question": "What is Django?"}'

Example Response
{
  "question": "What is Django?",
  "answer": "Django is a high-level Python web framework that enables rapid development of secure and maintainable websites.",
  "created_at": "2025-09-17T09:20:10Z"
}



<img width="1881" height="940" alt="Screenshot 2025-09-20 230311" src="https://github.com/user-attachments/assets/026558f9-32d2-4d48-9fde-eb130f5efb83" />


🐳 Run with Docker

Build and run:

docker build -t faq-chatbot .
docker run -p 8000:8000 faq-chatbot




📌 Roadmap

 Add user authentication (JWT).

 Enable multiple AI model selection.

 Improve frontend (React/Vue).

 Deploy on Render/Heroku.

 Add unit tests with pytest.




📜 License

MIT License. Free to use and modify.
