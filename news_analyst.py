import os
import requests
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_latest_news(topic):
    news_api_key=os.getenv("MY_NEWS_API")
    url = f"https://newsapi.org/v2/everything?q={topic}&sortBy=publishedAt&pageSize=&apiKey={news_api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # This will raise an error for bad responses (4xx or 5xx)
        articles = response.json().get("articles", [])
        # We only need the title and description for our analysis
        return [{"title": a["title"], "content": a.get("description", "No description available.")} for a in articles]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching news: {e}")
        return []

# --- Part 3: Function to Analyze News with AI ---
def analyze_news(articles):
    """Uses an LLM to analyze a list of articles."""
    # Combine the articles into a single string for the LLM
    news_context = "\n\n".join([f"Title: {a['title']}\nContent: {a['content']}" for a in articles])

    # Assigning a role to the AI for better results
    system_prompt = "You are a world-class financial and tech analyst. Your task is to synthesize information from the provided news articles."
    
    # The specific instruction for the AI
    user_prompt = f"""
    Based on the following news articles, provide a concise summary of the key developments, the overall market sentiment (Positive, Negative, Neutral), and one potential future implication.

    News Articles:
    ---
    {news_context}
    ---
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.5
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error analyzing news: {e}")
        return "Sorry, I was unable to analyze the news."

# --- Part 4: Main Execution ---
if __name__ == "__main__":
    # You can change this topic to anything you're interested in!
    topic_of_interest = input("Enter the topic: ")
    print(f"Fetching and analyzing news for: '{topic_of_interest}'...\n")

    latest_articles = get_latest_news(topic_of_interest)

    if latest_articles:
        analysis = analyze_news(latest_articles)
        print("--- AI Analyst Report ---")
        print(analysis)
        print("-------------------------")
    else:
        print("Could not retrieve articles to analyze. Please check your NewsAPI key or network connection.")
