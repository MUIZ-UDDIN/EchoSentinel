# 📡 EchoSentinel: Autonomous Market Intelligence Platform

**EchoSentinel** is a full-stack, distributed system designed to monitor market sentiment in real-time. It harvests global news, analyzes emotional context using Natural Language Processing (NLP), and provides a persistent dashboard for market trend intelligence.

<img width="3839" height="1976" alt="image" src="https://github.com/user-attachments/assets/b58d6fcc-da2e-44e7-b4fd-658c9b0c0e1e" />

## 🚀 Key Features

*   **Autonomous Ingestion:** A dedicated background worker (`watcher.py`) that monitors high-value keywords (e.g., Bitcoin, AI, Tesla) 24/7.
*   **AI Sentiment Engine:** Powered by the **VADER NLP model** to classify news headlines into Positive, Negative, or Neutral sentiments with high accuracy.
*   **Persistent Data Vault:** Uses **SQLAlchemy ORM** and **SQLite** to maintain a permanent history of market trends, allowing for historical analysis.
*   **Real-time Dashboard:** A modern, responsive interface built with **FastAPI** and **Asynchronous JavaScript** for instant market updates.
*   **Cloud-Ready Architecture:** Fully containerized using **Docker** and **Docker Compose** for seamless deployment to any VPS or Cloud environment.

## 🛠️ Tech Stack

*   **Backend:** Python 3.12, FastAPI
*   **Database:** SQLite, SQLAlchemy (ORM)
*   **AI/NLP:** VADER Sentiment Analysis
*   **Frontend:** Vanilla JavaScript (ES6+), CSS3 (Flexbox/Grid), HTML5
*   **DevOps:** Docker, Docker Compose, `uv` Package Manager
*   **Testing:** Pytest (Unit Testing)

## 🏗️ System Architecture

EchoSentinel uses a **Distributed Worker Pattern**:

1.  **The Engine (Harvester):** The core logic that communicates with External APIs and performs NLP analysis.
2.  **The Scout (Watcher):** An autonomous background process that populates the database while the system is idle.
3.  **The Waiter (FastAPI):** A high-performance web server that bridges the database and the user.
4.  **The Face (UI):** A dynamic frontend that calculates market "Bullish/Bearish" scores on the fly.

## 📦 Installation & Setup

### Prerequisites
*   [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.
*   A [NewsAPI Key](https://newsapi.org/).

### Quick Start
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/YOUR_USERNAME/EchoSentinel.git
    cd EchoSentinel
    ```

2.  **Configure Environment Variables:**
    Create a `.env` file in the root directory:
    ```text
    API_KEY=your_news_api_key_here
    ```

3.  **Launch the Platform:**
    ```bash
    docker-compose up --build
    ```

4.  **Access the Dashboard:**
    Open [http://localhost:8000/index.html](http://localhost:8000/index.html) in your browser.

## 🧪 Testing
EchoSentinel is built with reliability in mind. Run the test suite using:
```bash
uv run pytest