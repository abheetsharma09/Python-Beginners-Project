from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import pickle
from pydantic import BaseModel, Field
import pandas as pd
from typing import Annotated

# import the ML Model
with open("first_model.pkl" , "rb") as ml_binaryData:
    model = pickle.load(ml_binaryData)

# pydantic Data Model
class Model_Input_Data(BaseModel):
    cgpa :Annotated[float , Field(..., gt=0, lt=100 ,description="Enter student CGPA")]
    iq : Annotated[float , Field(..., gt=0 , description="Enter Student IQ")]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict")
def predictData(inputData : Model_Input_Data):
    input_df = pd.DataFrame([{ #Create a Pandas Dataframe for Model Input
        'cgpa' : inputData.cgpa,
        'iq' : inputData.iq
    }])

    prediction = model.predict(input_df)[0]

    return JSONResponse(status_code=200 , content={'output':int(prediction)})