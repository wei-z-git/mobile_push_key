# Quick start 
## run in docker 
`docker run -d --name mobile_push_key_app -e KEYSTORE_PATH="app/keystore/code.key" -e TOKEN="[token]" -v [key_path]:/app/keystore/ -p 66:80 registry.cn-qingdao.aliyuncs.com/wei-z/mobile_push_key`
- [TOKEN] use your own token
- [key_path] where your key saved in host server, such as "/root/keystore/"

eg . 
TOKEN="12345" 
-v /root/keystore/:/app/keystore/
## Edit your code 
with "code.key" in host server 

# run local
## dependence
    need python 3.6+
`pip install fastapi`  
`pip install uvicorn`
## set environment variable
### windows
    SET KEYSTORE_PATH=app\keystore\code.key
    SET TOKEN=asd
### linux
    KEYSTORE_PATH=app/keystore/code.key
    TOKEN=123
## start uvicorn server
`git clone https://gitee.com/amadeus666/mobile_push_key.git`  
`cd mobile_push_key`  
`uvicorn app.main:app --reload`  
