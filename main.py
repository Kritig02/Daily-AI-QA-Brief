import asyncio

from telegram_bot import send_message 
from search import get_latest_news
from summarizer import summarize_articles

print("Main file started")

async def run():
    articles = get_latest_news()
    summary = summarize_articles(articles)
    await send_message(summary)

if __name__ == "__main__":
    asyncio.run(run())