# 🤖 Daily AI QA Brief

An autonomous AI agent that discovers, analyzes, and delivers the latest **AI, Machine Learning, and Quality Engineering** news directly to Telegram every morning.

Instead of manually browsing multiple websites, the agent searches trusted sources, summarizes the most relevant articles using Gemini, explains **why each story matters to QA engineers**, and sends a concise daily briefing.

---

## ✨ Features

* 🔍 Searches the web for the latest AI & Quality Engineering news using **Tavily**
* 🧠 Summarizes articles with **Google Gemini**
* 💡 Explains why each article matters to QA Engineers
* 📲 Delivers a clean daily briefing to **Telegram**
* ⏰ Runs automatically every morning using **GitHub Actions**
* 🔐 Secure API key management using GitHub Secrets and environment variables

---

## 🏗️ Architecture

```text
                    ┌────────────────────┐
                    │  GitHub Actions    │
                    │  (Daily @ 8:00 AM) │
                    └─────────┬──────────┘
                              │
                              ▼
                     ┌────────────────┐
                     │    main.py     │
                     │ Orchestrator   │
                     └──────┬─────────┘
                            │
          ┌─────────────────┴─────────────────┐
          ▼                                   ▼
 ┌──────────────────┐                 ┌──────────────────┐
 │    search.py     │                 │  summarizer.py   │
 │     Tavily       │                 │ Google Gemini AI │
 └────────┬─────────┘                 └────────┬─────────┘
          │                                    │
          └─────────────────┬──────────────────┘
                            ▼
                  ┌────────────────────┐
                  │  telegram_bot.py   │
                  └─────────┬──────────┘
                            ▼
                 📲 Telegram Daily Brief
```

---

## 📂 Project Structure

```text
Daily-AI-QA-Brief/
│
├── main.py
├── search.py
├── summarizer.py
├── telegram_bot.py
├── requirements.txt
├── .env
│
└── .github/
    └── workflows/
        └── daily_brief.yml
```

---

## 🛠️ Tech Stack

* Python 3.12
* Google Gemini API
* Tavily Search API
* Telegram Bot API
* GitHub Actions
* python-dotenv

---

## 🚀 How It Works

1. Search the latest AI & QA news using Tavily.
2. Retrieve the most relevant articles.
3. Send the articles to Gemini.
4. Generate:

   * A concise summary
   * Why it matters for QA Engineers
   * Impact level
5. Deliver the briefing to Telegram.
6. Repeat automatically every morning.

---

## 📸 Example Output

```text
🤖 AI QA Brief

🔥 Playwright introduces AI Agents

📝 Summary
Playwright now supports agentic browser automation through MCP,
enabling more intelligent UI testing.

💡 Why it matters
QA teams can build more resilient and self-healing automation
instead of relying solely on brittle scripted tests.

📌 Impact
High

🔗 Source
https://...
```

---

## ⚙️ Local Setup

Clone the repository:

```bash
git clone https://github.com/Kritig02/Daily-AI-QA-Brief.git
cd Daily-AI-QA-Brief
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
CHAT_ID=YOUR_CHAT_ID
TAVILY_API_KEY=YOUR_TAVILY_API_KEY
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

Run the project:

```bash
python3 main.py
```

---

## ☁️ Automation

The project uses **GitHub Actions** to execute automatically every morning.

Workflow:

* Install dependencies
* Load secrets securely
* Search latest news
* Summarize using Gemini
* Send the briefing to Telegram

No local machine is required after deployment.

---

## 🔮 Future Improvements

* Store previous articles to prevent duplicate news.
* Personalized article ranking based on user interests.
* Weekly AI QA newsletter.
* Slack, Microsoft Teams, and Discord integrations.
* Voice summary using text-to-speech.
* AI-generated podcast of the daily briefing.
* Web dashboard with searchable news archive.
* RAG-based knowledge base for historical QA news.
* Multi-language support.

---

## 🎯 Why I Built This

I wanted a faster and more efficient way to stay up to date with the rapidly evolving world of AI and Quality Engineering without spending time browsing multiple websites and newsletters every day.

This project combines autonomous web search, LLM-powered summarization, and workflow automation to build a practical AI agent that discovers relevant news, explains why it matters to QA professionals, and delivers actionable insights directly to Telegram every morning.

---

## 📄 License

This project is licensed under the MIT License.
