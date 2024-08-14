from fastapi import FastAPI, File
from app.modules.Common import *
from app.modules.LocalKeyFunc import *
from app.modules.RemoteKeyFunc import KeyMethodClass

tags_metadata = [
    {
        "name": "root",
        "description": "hello world",
    },
    {
        "name": "V1",
        "description": "save keys locally.",
    },
    {
        "name": "V2",
        "description": "save keys in gitee.com",
    },
]

app = FastAPI(
    title="Mobile Push Key",
    description='模拟一个二次因素验证验证码发送器<br><br>Gitee: <a href="https://gitee.com/amadeus666/mobile_push_key.git"  class="link">https://gitee.com/amadeus666/mobile_push_key.git</a>',
    version="1.2.0",
    contact={
        "name": "wei-z",
        "email": "1419864987@qq.com",
    },
    openapi_tags=tags_metadata)


@app.get("/", tags=["root"])
def read_root():
    return {"Hello": "World"}


@app.get("/v1/VerificationCode", tags=["V1"])
@app.get("/v1/VerificationCode/{access_key}", tags=["V1"], description="get key", response_description="res a key")
def getVerificationCode(access_key: str):
    if (check_token(access_key) == True):
        VerificationCode = read_code()
    else:
        VerificationCode = "access_key isn`t correct, please check..."
    return VerificationCode


@app.get("/v2/GetPushKey/{endpoint}/{owner}/{repo}/{path}/{access_token}",
         tags=["V2"],
         response_description="res a key,like '{\"code\":123456, \"remaining sum\":123}' "
         )
def GetPushKey(endpoint: str, owner: str, repo: str, path: str, access_token: str):
    """
    Get a key from gitee, eg. 
        repo url: https://gitee.com/amadeus666/keystore.git
        file path: folder/secret

    - **endpoint**: default is gitee.com
    - **owner**: @xxx, like amadeus666 above.
    - **repo**: repo name, keystore
    - **path**: secrets file path, "folder/secret"
    - **access_token**: api token of your gitee repo
    """
    current_key = KeyMethodClass(
        endpoint, owner,  repo, path, access_token).get_key()
    return current_key


@app.post("/v2/CreateNewKeys",
          tags=["V2"],
          response_description="200"
          )
def CreateNewKey(endpoint: str, owner: str, repo: str, path: str, access_token: str, newkeys: bytes = File(...)):
    """
    Put keys to gitee.com, prepare a secret.txt that contains secret keys.
    Since gitee.com use "HTTP PUT" method to update its files, this operation may override the existed keys.
    eg. 
        repo url: https://gitee.com/amadeus666/keystore.git
        file path: folder/secret-test

    - **endpoint**: default is gitee.com
    - **owner**: @xxx, like amadeus666 above.
    - **repo**: repo name, keystore
    - **path**: secrets file path, "folder/secret"
    - **access_token**: api token of your gitee repo
    - **newkeys**: create your new key_files and upload it

    """
    response = KeyMethodClass(
        endpoint, owner,  repo, path, access_token).create_new_keys(newkeys)
    return response