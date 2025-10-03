import os
from typing import List
import google.generativeai as genai
from textbase.message import Message

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters 
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ------------------ Gemini Setup ------------------
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))  # Replace with your Gemini API key

BASE_PROMPT = """You are chatting with a Medical Assistant.
I can provide information on medical topics and answer health-related questions.
Please remember that I'm not a substitute for professional medical advice.
If you have a medical emergency, please call emergency services immediately.
"""

# ------------------ State ------------------
chat_history: List[Message] = []   # conversation history
state = {"lang": "english"}        # default language


def gemini_chatbot(message_history: List[Message], state: dict):
    """Medical Assistant Chatbot logic with Hindi/English support"""

    # Build language-specific system prompt
    if state.get("lang") == "hindi":
        system_prompt = BASE_PROMPT + "\n\n⚠️ अब से आप हिन्दी में जवाब दें।"
    else:
        system_prompt = BASE_PROMPT + "\n\n⚠️ From now on, respond in English."

    # Prepare messages
    history = []
    for msg in message_history:
        if msg.role == "user":
            history.append({"role": "user", "parts": [msg.content]})
        elif msg.role == "assistant":
            history.append({"role": "model", "parts": [msg.content]})

    # Initialize Gemini model
    model = genai.GenerativeModel("gemini-2.5-flash")

    # Generate response
    chat = model.start_chat(history=history)
    response = chat.send_message(system_prompt + "\n\n" + message_history[-1].content)

    return response.text, state


# ------------------ Telegram Setup ------------------
TOKEN = os.getenv("TELEGRAM_TOKEN")  # Replace with your Telegram bot token

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello! 🤖 I’m your Medical Assistant chatbot.\n\n"
        "Type `/hindi` to chat in Hindi or `/english` to chat in English"
    )


# Change language command
async def set_hindi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    state["lang"] = "hindi"
    await update.message.reply_text("✅ अब से मैं हिन्दी में जवाब दूँगा।")


async def set_english(update: Update, context: ContextTypes.DEFAULT_TYPE):
    state["lang"] = "english"
    await update.message.reply_text("✅ I will now respond in English.")


# Handle user messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global chat_history, state

    user_text = update.message.text
    chat_history.append(Message(role="user", content=user_text))

    try:
        # Run Gemini chatbot
        bot_response, state = gemini_chatbot(chat_history, state)
    except Exception as e:
        print("⚠️ Gemini Error:", e)
        bot_response = "⚠️ Sorry, I couldn’t generate a response right now."

    # Save assistant reply
    chat_history.append(Message(role="assistant", content=bot_response))

    # Send reply back
    await update.message.reply_text(bot_response)


# ------------------ Main Function ------------------
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("hindi", set_hindi))
    app.add_handler(CommandHandler("english", set_english))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("✅ Telegram bot connected to Gemini is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
