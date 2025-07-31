# 🤖 Personalized News Analyst Agent

A Python-based agent that fetches real-time news articles on any given topic and leverages a Large Language Model (LLM) to provide a concise, expert-level analysis.

---

## 🚀 Features

-   **Real-time Data:** Fetches the latest articles from around the web using the NewsAPI.
-   **AI-Powered Analysis:** Uses the OpenAI API to analyze the news context and generate insightful summaries.
-   **Expert Persona:** Employs role-prompting to have the LLM act as a professional financial and tech analyst.
-   **Secure & Configurable:** Manages API keys securely using a `.env` file.

---

## 🛠️ How It Works

This project follows a simple but powerful workflow:

1.  **Fetch:** The agent queries the NewsAPI for the top 5 most recent articles related to a specified topic (e.g., "advancements in generative AI").
2.  **Contextualize:** The titles and descriptions of these articles are compiled into a single context block.
3.  **Analyze:** This context is sent to an LLM (GPT-3.5-Turbo) with a carefully crafted prompt, instructing it to act as an analyst and provide a summary, market sentiment, and future implications.
4.  **Report:** The final analysis from the LLM is printed to the console.

---

## ⚙️ Setup and Installation

To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
    cd YOUR_REPOSITORY_NAME
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For Mac/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Create your environment file:**
    -   Create a file named `.env`.
    -   Add your API keys to it in the following format:
        ```env
        NEWS_API_KEY=YOUR_NEWS_API_KEY_HERE
        OPENAI_API_KEY=YOUR_OPENAI_API_KEY_HERE
        ```

---

## ▶️ Usage

Once the setup is complete, simply run the script from your terminal:

```bash
python news_analyst.py
