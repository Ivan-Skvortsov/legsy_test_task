from fastapi import FastAPI

from src.services.parsing import get_product_data

app = FastAPI()


@app.get("/")
async def hello_world():
    print(get_product_data(139760729))
    return {"Hello": "Legsy!"}
