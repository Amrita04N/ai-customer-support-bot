from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI
import os
from dotenv import load_dotenv
from uuid import uuid4

# Load environment variables
load_dotenv()  # Make sure .env has OPENAI_API_KEY=sk-xxxx

# Initialize FastAPI app
app = FastAPI(title="AI Customer Support Bot")

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# In-memory sessions storage
sessions = {}

# ------------------------
# Models
# ------------------------
class StartSessionRequest(BaseModel):
    customer_name: str

class ChatRequest(BaseModel):
    session_id: str
    user_message: str

# ------------------------
# Endpoints
# ------------------------
@app.get("/")
def home():
    return {"message": "AI Customer Support Bot is running!"}

@app.post("/start_session")
def start_session(request: StartSessionRequest):
    customer_name = request.customer_name
    session_id = str(uuid4())
    sessions[session_id] = [{"role": "system", "content": f"Customer {customer_name} started a session."}]
    return {"session_id": session_id}

@app.post("/chat")
def chat(request: ChatRequest):
    session_id = request.session_id
    user_msg = request.user_message

    if session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")

    sessions[session_id].append({"role": "user", "content": user_msg})

    try:
        # Use gpt-3.5-turbo for reliability
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=sessions[session_id]
        )

        ai_reply = response.choices[0].message.content
        sessions[session_id].append({"role": "assistant", "content": ai_reply})
        return {"reply": ai_reply}

    except Exception as e:
        # Catch any OpenAI errors and return a safe message
        print("OpenAI API error:", e)
        ai_reply = "Sorry, I cannot process your request right now. Please try again later."
        sessions[session_id].append({"role": "assistant", "content": ai_reply})
        return {"reply": ai_reply}

@app.get("/session/{session_id}")
def get_session(session_id: str):
    if session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    return {"session_history": sessions[session_id]}
