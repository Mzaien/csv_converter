from fastapi import FastAPI, UploadFile, File, HTTPException
from typing import Dict, List
from csv import DictReader
from shutil import copyfileobj
from os import unlink

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Resal 💙"}


# Testing a get enpoint with local csv file
@app.get("/csv")
def csvre():
    with open('../csv_test.csv', "r") as file:
        csv_reader = DictReader(file, delimiter=',')
        table: List[Dict] = []
        for row in csv_reader:
            table.append(row)

        table.sort(key=lambda x: x['customer_average_rating'], reverse=True)
        highest = table[0]
        product_name = highest['product_name']
        product_rating = float(highest['customer_average_rating'])

        return {"top_product": product_name, "product_rating": product_rating}


# The convert endpoint is used to convert the data from the csv file to json
@app.post("/convert")
async def conv(csv_file: UploadFile = File(...)):
    if csv_file.content_type != "text/csv":
        raise HTTPException(status_code=402, detail="Invalid file type")
    else:
        with open("files/destination.csv", "wb") as buffer:
            copyfileobj(csv_file.file, buffer)
        with open('files/destination.csv', "r", encoding="utf8") as file:
            csv_reader = DictReader(file, delimiter=',')
            table: List[Dict] = []
            for row in csv_reader:
                table.append(row)

            table.sort(key=lambda x: x['customer_average_rating'],
                       reverse=True)
            highest = table[0]
            product_name = highest['product_name']
            product_rating = float(highest['customer_average_rating'])

            unlink('files/destination.csv', dir_fd=None)
            return {"top_product": product_name, "product_rating": product_rating}
