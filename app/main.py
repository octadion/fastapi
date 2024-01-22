from typing import List
from pydantic import BaseModel
from fastapi import FastAPI
from joblib import load

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

class IrisSingleRequest(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width:float

mapping_res = {0:'setosa', 1:'versicolor', 2:'virginica'}
def post_process(pred):
    return  mapping_res[pred]

@app.post("/iris")
def iris(request:IrisSingleRequest):
    formatted_features = [[request.sepal_length,request.sepal_width,request.petal_length,request.petal_width]]
    model =  load("model.sav")
    result = model.predict(formatted_features)
    print({"result": result.tolist()[0]})
    return {"result": post_process(result.tolist()[0])}