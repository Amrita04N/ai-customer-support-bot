# AI Customer Support Bot 🤖

A simple AI-powered customer support bot built with **FastAPI** and **OpenAI GPT**.  
It supports session-based conversations, retains chat history, and can simulate escalation when queries are not answered.

---

## 🚀 Features

- **Session-based conversations:** Each user gets a unique session ID.
- **Contextual memory:** The bot remembers previous messages in the same session.
- **AI-powered responses:** Uses OpenAI GPT-4o-mini to generate answers.
- **Escalation simulation:** Handles cases where the bot cannot provide an answer.
- **Frontend chat UI:** Lightweight browser interface to interact with the bot.

---

## 🛠 Tech Stack

- **Backend:** FastAPI  
- **AI:** OpenAI GPT-4o-mini  
- **Database:** In-memory Python dictionary (can be extended to SQL/NoSQL)  
- **Frontend:** HTML, CSS, JavaScript  
- **Environment management:** Python virtual environment (.venv)  

---

## ⚡ Getting Started

### 1️⃣ Clone the repo

```bash
git clone https://github.com/Amrita04N/ai-customer-support-bot.git
cd ai-customer-support-bot
2️⃣ Create and activate virtual environment
bash
Copy code
python -m venv .venv

# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate
3️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Setup environment variables
Create a .env file in the project root:

ini
Copy code
OPENAI_API_KEY=sk-your_openai_key_here
Replace sk-your_openai_key_here with your actual OpenAI API key.

5️⃣ Run the FastAPI backend
bash
Copy code
uvicorn app:app --reload --port 8000
6️⃣ Open the frontend
Open index.html in your browser and start chatting with the bot.

💬 Example Chat Flow
User	Bot
Hi, I need help with my account	Hello! How can I assist you today?
How can I reset my password?	You can reset it by clicking "Forgot Password" on the login page.
I still can't login, please escalate	I’m escalating your issue to a human agent.

📂 Project Structure
bash
Copy code
ai-cs-bot/
│
├── app.py           # FastAPI backend
├── index.html       # Frontend chat UI
├── .env             # Environment variables (not pushed to GitHub)
├── .venv/           # Python virtual environment (ignored in Git)
├── requirements.txt # Python dependencies
└── README.md
✅ Notes
Make sure the backend is running before opening the frontend.

The bot stores chat only in memory, so restarting the server will reset all sessions.

You can extend this project by adding a database for persistent chat history or user authentication.

🎥 Demo
Start backend: uvicorn app:app --reload --port 8000

Open index.html in a browser

Chat interactively with the AI bot

📝 License
This project is for educational purposes.

yaml
Copy code

---

If you want, I can now **give you a small final submission checklist** to make sure your demo and GitHub repo look perfect for evaluation.  

Do you want me to do that?
