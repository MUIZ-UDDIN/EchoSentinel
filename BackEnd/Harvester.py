import os
from dotenv import load_dotenv
import requests
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, sessionmaker
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer #type:ignore

logging.basicConfig(filename="database/Harvest.log", level=logging.INFO)

load_dotenv()

class base(DeclarativeBase):
    pass

class Artcile_TB(base):
    __tablename__ = "Artic_Table"

    id: Mapped[int] = mapped_column(primary_key=True)
    topic: Mapped[str] = mapped_column()
    title: Mapped[str] = mapped_column()
    sentiment: Mapped[str] = mapped_column()

class News:
    def __init__(self):
        self.api = os.getenv("API_KEY")

        engine = create_engine("sqlite:///database/Harvester.db")
        base.metadata.create_all(engine)
        self.session = sessionmaker(bind=engine)
        self.Sentiment_analyzer = SentimentIntensityAnalyzer()



    def sentiment_analysis(self, sentiments: str) -> str:

        analyzer = self.Sentiment_analyzer.polarity_scores(sentiments)
        compound = analyzer["compound"]

        if compound >= 0.05:
            return "POSITIVE"
        
        elif compound <= -0.05:
            return "NEGATIVE"

        else:
            return "NEUTRAL"


    def fetch(self, topic: str) -> list:
        url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={self.api}"
        artic_lst = []
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                for articles in data["articles"]:
                    article = articles["title"]
                    sentiment = self.sentiment_analysis(article)
                    articles["sentiment"] = sentiment
                    artic_lst.append(articles)
            
            else:
                logging.error(f"Url is not responding{response.status_code}")
                return []

        except Exception as e:
            logging.warning(f"URL request is not responding")
        
        return artic_lst

    def save_to_db(self, article: list, topic: str)-> None:
        DB = self.session()
        for artic in article:
            new_row = Artcile_TB(
                title = artic["title"],
                sentiment = artic["sentiment"],
                topic = topic
            )
            DB.add(new_row)
        DB.commit()
        DB.close()

    def data_history(self, limit: int = 50):
        DH = self.session()
        Query_Data = DH.query(Artcile_TB).order_by(Artcile_TB.id.desc()).limit(limit).all()
        Lst_QD = []
        
        for Query_dt in Query_Data:
            Lst_QD.append({"title": Query_dt.title, "topic": Query_dt.topic, "sentiment": Query_dt.sentiment, })
        
        logging.info(f"{len(Lst_QD)} Query_data has been appended")
        DH.close()

        return Lst_QD
        

engine = News()
        
if __name__ == "__main__":
    
    news = engine.fetch("sad")
    engine.save_to_db(news, "sad")
    for new in news[:3]:
        print(f"{new["title"]} : {new['sentiment']}")