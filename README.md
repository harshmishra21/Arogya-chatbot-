# 🏥 Arogya Sehat - Medical Assistant Chatbot

**Binary Brains | SIH 2025**

A multilingual Medical Assistant Chatbot powered by Google's Gemini AI and integrated with Telegram. This intelligent chatbot provides medical information and health-related support in both English and Hindi, making healthcare information accessible to a wider audience.

![Python](https://img.shields.io/badge/Python-3.12-blue.svg)
![Gemini AI](https://img.shields.io/badge/Gemini-2.5--flash-orange.svg)
![Telegram](https://img.shields.io/badge/Telegram-Bot-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## 📋 Table of Contents
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [API Keys Setup](#-api-keys-setup)
- [Troubleshooting](#-troubleshooting)
- [Disclaimer](#-disclaimer)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

- **🤖 AI-Powered Responses**: Utilizes Google's Gemini 2.5 Flash model for intelligent, context-aware medical information
- **🌐 Multilingual Support**: Seamlessly switch between English and Hindi
- **💬 Telegram Integration**: Easy-to-use interface through Telegram messenger
- **🧠 Context-Aware Conversations**: Maintains conversation history for coherent interactions
- **⚡ Real-time Responses**: Fast and efficient response generation
- **🔒 Safe & Responsible**: Built-in guardrails to ensure appropriate medical guidance
- **📱 Accessible**: Available 24/7 through Telegram on any device

---

## 🛠️ Tech Stack

- **Language**: Python 3.12
- **AI Model**: Google Gemini 2.5 Flash
- **Bot Framework**: python-telegram-bot
- **Environment Management**: python-dotenv
- **API Integration**: google-generativeai

---

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8 or higher** (Python 3.12 recommended)
- **pip** (Python package manager)
- **Git** (for cloning the repository)
- **Telegram Account** (to create and test the bot)
- **Google Gemini API Key** (free tier available)
- **Telegram Bot Token** (obtained from BotFather)

---

## 🚀 Installation

Follow these steps to set up the project on your local machine:

### 1. Clone the Repository

```bash
git clone https://github.com/harshmishra21/Arogya-Sehat-chatbot.git
cd Arogya-Sehat-chatbot
```

### 2. Create a Virtual Environment

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Required Libraries

**⚠️ IMPORTANT: These libraries are REQUIRED to run the chatbot properly!**

#### Core Dependencies (Must Install):

1. **google-generativeai** - For Gemini AI integration
2. **python-telegram-bot** - For Telegram bot functionality
3. **python-dotenv** - For environment variable management
4. **textbase** - Framework for the chatbot

#### Quick Installation Method:

**Option 1: Install from requirements.txt (Recommended)**
```bash
pip install -r requirements.txt
```

**Option 2: Install individually**
```bash
pip install google-generativeai==0.8.5
pip install python-telegram-bot==22.4
pip install python-dotenv==1.1.1
pip install textbase
```

#### Complete requirements.txt contents:
```
google-generativeai==0.8.5
python-telegram-bot==22.4
python-dotenv==1.1.1
google-ai-generativelanguage==0.6.15
google-api-core==2.25.1
googleapis-common-protos==1.70.0
textbase
```

**✅ Verify Installation:**
```bash
pip list | grep -E "(google|telegram|dotenv|textbase)"
```

---

## ⚙️ Configuration

### 1. Create Environment File

Create a `.env` file in the `textbase/` directory:

```bash
cd textbase
touch .env
```

### 2. Add Your API Keys

Open the `.env` file and add the following:

```env
GEMINI_API_KEY=your_gemini_api_key_here
TELEGRAM_TOKEN=your_telegram_bot_token_here
```

**⚠️ Important**: Never commit your `.env` file to GitHub. It's already included in `.gitignore`.

---

## 🔑 API Keys Setup

### Getting Google Gemini API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click on "Get API Key" or "Create API Key"
4. Copy the generated API key
5. Paste it in your `.env` file as `GEMINI_API_KEY`

### Getting Telegram Bot Token

1. Open Telegram and search for [@BotFather](https://t.me/botfather)
2. Send `/newbot` command
3. Follow the instructions to create your bot
4. Copy the bot token provided by BotFather
5. Paste it in your `.env` file as `TELEGRAM_TOKEN`

---

## 🎯 Usage

### Running the Chatbot

1. Make sure your virtual environment is activated
2. Navigate to the `textbase/` directory:
   ```bash
   cd textbase
   ```

3. Run the bot:
   ```bash
   python main.py
   ```

4. You should see:
   ```
   ✅ Telegram bot connected to Gemini is running...
   ```

### Interacting with the Bot

1. Open Telegram and search for your bot using the username you created
2. Start a conversation with `/start`
3. Use these commands:
   - `/start` - Initialize the bot
   - `/english` - Switch to English language
   - `/hindi` - Switch to Hindi language (हिन्दी में बात करें)
4. Ask any health-related questions!

**Example Queries:**
- "What are the symptoms of flu?"
- "How can I improve my sleep quality?"
- "बुखार के लिए घरेलू उपाय क्या हैं?" (Home remedies for fever in Hindi)

---

## 📁 Project Structure

```
Binary_brains/
│
├── textbase/
│   ├── main.py              # Main bot application
│   ├── .env                 # Environment variables (not in repo)
│   ├── sample.py            # Sample code
│   └── textbase/            # Textbase library modules
│       ├── message.py
│       ├── models.py
│       └── ...
│
├── venv/                    # Virtual environment (not in repo)
├── Members_List.pdf         # Team members information
├── SIH2025-Binary_Brains.pdf # Project documentation
├── README.md                # This file
└── .gitignore              # Git ignore rules
```

---

## 🐛 Troubleshooting

### Common Issues and Solutions

**1. ModuleNotFoundError: No module named 'google.generativeai'**
```bash
pip install google-generativeai
```

**2. Telegram Bot Not Responding**
- Check if your bot token is correct in `.env`
- Ensure the bot is running (`python main.py`)
- Verify your internet connection

**3. Gemini API Error**
- Verify your API key is valid
- Check if you've exceeded the free tier quota
- Ensure the API key has proper permissions

**4. Virtual Environment Issues**
- Deactivate and reactivate: `deactivate` then `source venv/bin/activate`
- Recreate the virtual environment if needed

**5. Import Errors**
- Ensure you're in the correct directory (`textbase/`)
- Verify all packages are installed: `pip list`

---

## ⚠️ Disclaimer

**IMPORTANT MEDICAL DISCLAIMER:**

This Medical Assistant Chatbot is designed to provide **general medical information and educational support only**. 

- ❌ **NOT a substitute** for professional medical advice, diagnosis, or treatment
- ❌ **NOT for medical emergencies** - Call emergency services immediately if needed
- ❌ **NOT a replacement** for consultation with qualified healthcare providers
- ✅ **Always consult** your physician or healthcare provider for personalized medical advice
- ✅ **Use responsibly** and verify information with medical professionals

The chatbot's responses are generated by AI and should not be considered as professional medical guidance.

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/AmazingFeature`
3. **Commit your changes**: `git commit -m 'Add some AmazingFeature'`
4. **Push to the branch**: `git push origin feature/AmazingFeature`
5. **Open a Pull Request**

### Areas for Contribution
- Adding more language support
- Improving response accuracy
- Adding voice message support
- Creating a web interface
- Enhancing error handling
- Writing tests

---

## 📄 License

This project is licensed under the **MIT License** - see the LICENSE file for details.

---

## 👥 Team Binary Brains

**SIH 2025 Hackathon Project**

For more information, refer to `Members_List.pdf` and `SIH2025-Binary_Brains.pdf`.

---

## 📞 Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Contact the team members listed in `Members_List.pdf`

---

## 🙏 Acknowledgments

- Google Gemini AI for providing the powerful language model
- Telegram for the bot platform
- Textbase library for the framework
- All contributors and team members

---

**Made with ❤️ by Team Binary Brains**

