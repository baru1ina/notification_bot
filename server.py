import schedule
from fastapi import FastAPI

app = FastAPI()


@app.post('/notify')
async def notify():
    schedule.run_pending()