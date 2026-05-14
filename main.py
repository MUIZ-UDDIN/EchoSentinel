import logging
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from Harvester import News

engine = News()
app = FastAPI()

# news = engine.fetch()
# engine.save_to_db()


@app.get("/search/{topic}")
async def search_news(topic: str):
    result = engine.fetch(topic)
    engine.save_to_db(result, topic)

    logging.info(f"{len(result)} has been loaded")
    return result

@app.get("/history/{limit}")

async def get_vault(limit: int):
    data = engine.data_history(limit)

    return data

app.mount("/", StaticFiles(directory="./FrontEnd", html=True), name="FrontEnd")

