from Harvester import News
import logging
import time

engine = News()

watch_lst = ["Bitcoin", "AI", "Tesla"]

while True:
    for each in watch_lst:
        try:
            new = engine.fetch(each)
            engine.save_to_db(new, each)
            logging.info(f"{len(new)} articles has been updated")

        except Exception as e:
            logging.info(f"There is a issue at watch_lst data creation: {e}")


    time.sleep(3600)

