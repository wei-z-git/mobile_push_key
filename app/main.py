from app.check_token import Check_token
from fastapi import FastAPI
from app.read_code import Read_code
from app.check_token import Check_token
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/VerificationCode")
@app.get("/VerificationCode/{token}")
def getVerificationCode(token:str):
    if (Check_token(token)==True):
        VerificationCode=Read_code()
    else:
        VerificationCode="token isn`t correct, please check..."
    return VerificationCode
