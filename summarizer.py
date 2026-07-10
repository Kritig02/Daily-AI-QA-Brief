import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def summarize_articles(articles):

    prompt = """
        You are an AI QA analyst preparing a daily briefing for a Senior QA Engineer.

        Create a concise Telegram newsletter.

        Use this exact format:

        🤖 *AI QA Brief*
        📅 Today's Update

        🔥 *Top Stories*

        1. *Title*

        📝 *Summary:*
        2 concise sentences.

        💡 *Why QA Engineers should care:*
        1-2 practical sentences.

        📌 *Impact:* High/Medium/Low

        🔗 *Source:*
        URL

        Rules:
        - No introduction
        - No conclusion
        - Maximum 5 stories
        - Keep total response under 2000 characters
        - Focus on AI testing, QA automation, Playwright, Selenium, LLM testing, MCP, and developer tools.
        - Prioritize practical impact for QA engineers.

        Articles:

        """

    for article in articles:
        prompt += f"""
        title: {article['title']}
        Content: {article['content']}
        Source: {article['url']}
        """

    response = client.models.generate_content(model="gemini-3.1-flash-lite", contents = prompt)

    return response.text