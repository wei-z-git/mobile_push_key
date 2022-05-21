from matplotlib.font_manager import json_dump
import requests
import json

def test1(endpoint):
    respose = requests.get(
        "https://gitee.com/api/v5/repos/amadeus666/keystore/contents/secrets?access_token=3338f24654a424bf075836fe19aa274b",
    )
    respose = json.loads(respose.text)['sha']
    return respose


def test2(endpoint):
    x=test1(1)
    payload_dict = {'access_token':'3338f24654a424bf075836fe19aa274b','content':'Mg==','sha':x,'message':'2'}
    respose = requests.put(
        "https://gitee.com/api/v5/repos/amadeus666/keystore/contents/secrets",
        data=payload_dict,
    )
    respose = respose.text
    return respose

test2(1)