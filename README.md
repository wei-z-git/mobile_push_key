
[![release tag](https://img.shields.io/github/v/release/wei-z-git/mobile_push_key?include_prereleases)](https://github.com/wei-z-git/mobile_push_key/releases)
[![build status](https://img.shields.io/github/workflow/status/wei-z-git/mobile_push_key/Docker%20Image%20CI)](https://github.com/wei-z-git/mobile_push_key/actions)

# Quick start
## 1.Use Local storage
(1) use local storage to save keys

`docker run -d --name mobile_push_key_app -e KEYSTORE_PATH="app/keystore/code.key" -e TOKEN="[token]" -v [key_path]:/app/keystore/ -p 66:80 registry.cn-qingdao.aliyuncs.com/wei-z/mobile_push_key`
- [TOKEN] use your own token
- [key_path] where your key saved in host server, such as "/root/keystore/"

eg . 
TOKEN="12345" 
-v /root/keystore/:/app/keystore/

(2) Edit your keys
with file named "keys.key"in your server

(3) Get reqeust:
```bash
curl http://localhost:66/v1/VerificationCode/[token]
```

(4)see api docs
localhost:66/docs
## 2.Use Gitee.com
(1) use gitee.com to save keys

`docker run -d --name mobile_push_key_app   -p 81:80 registry.cn-qingdao.aliyuncs.com/wei-z/mobile_push_key:latest`

(2) put keys in any path of your repo, notices that the format if the file should be like below:

```
123456
123456
123456
```
(3) Get reqeust:
```yaml
http://localhost:81/v2/GetPushKey/gitee.com/[owner]/[repo]/[path]/[access_token]
```
eg.
http://localhost:81/v2/GetPushKey/gitee.com/amadeus666/keystore/secrets-test/123a924

(4)Put new keys(preview):
We could use API "/v2/CreateNewKeys" in swagger page to put new keys(through a file) into gitee.com.
Since gitee.com use "HTTP PUT" method to update its files, this operation may override the existed keys.
```
http://localhost:81/v2/CreateNewKeys
```
swagger doc: localhost/docs
## dependence
    python 3.6+
`pip install fastapi`  
`pip install uvicorn`
`pip install requests`
`pip install python-multipart`
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
`uvicorn app.main:app --reload --port 80`  

