from fastapi import FastAPI
import uvicorn
import sys
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from textSummarizer.pipeline.prediction import PredictionPipeline

text:str = 'What is Text Summarization?'

app = FastAPI()

@app.get("/", tags = ['authentication'])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return Response("Training Successful !!!", status_code=200)
    except Exception as e:
        return Response(f"Training Failed!!! [error: {e}]", status_code=400)
    
@app.get("/predict")
async def predict_route():
    try:
        obj = PredictionPipeline()
        summary = obj.predict(text)
        return Response(summary, status_code=200)
    except Exception as e:
        return Response(f"Prediction Failed!!! [error: {e}]", status_code=400)
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)