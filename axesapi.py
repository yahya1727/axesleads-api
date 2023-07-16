from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import AxesFunctions

origins = ["*"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CustomerFeedback(BaseModel):
    uname: Optional[str] = None
    uemail: Optional[str] = None
    usubject: Optional[str] = None
    body: Optional[str] = None

@app.get('/')
def homePage():
    return {"status": "Welcome To AxesLeads-Api"}

@app.post('/customer/feedback')
def storeFeedback(userdata : CustomerFeedback):
    data = userdata.dict()
    result = AxesFunctions.SendMailToCustomer(data)
    return result