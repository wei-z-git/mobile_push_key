import base64
import requests
import json
from threading import Thread


class KeyMethodClass:
    def __init__(self, endpoint="gitee.com", owner="", repo="", path="", access_token=""):
        self.endpoint = endpoint
        self.owner = owner
        self.repo = repo
        self.path = path
        self.access_token = access_token

    def async_wrapper(f):
        def wrapper(*args, **kwargs):
            thr = Thread(target=f, args=args, kwargs=kwargs)
            thr.start()
        return wrapper

    def get_current_key(self):
        # key_file may like "123456\n123456\n123456"
        key_file = self.get_key_file().split('\n')
        # {"code":123456, "remaining sum":123}
        key={"code":key_file[0],"remaining sum":str(len(key_file)-1)}
        return key

    def get_key_file(self):
        respose = requests.get(
            "https://{endpoint}/api/v5/repos/{owner}/{repo}/contents/{path}?access_token={access_token}".format(
                endpoint=self.endpoint, owner=self.owner, repo=self.repo, path=self.path, access_token=self.access_token),
            headers={'Content-Type': 'application/json;charset=UTF-8'},
        )
        # Bytes(base64) --> Byte(str) ---> Str
        key_file_str = str(base64.b64decode(json.loads(respose.text)
                                            ['content'].encode('utf-8')), 'utf-8')
        return key_file_str
   
    @async_wrapper
    def update_key_file(self, key_file_str):
        # get Blob SHA of the file
        sha = json.loads(requests.get(
            "https://{endpoint}/api/v5/repos/{owner}/{repo}/contents/{path}?access_token={access_token}".format(endpoint=self.endpoint, owner=self.owner, repo=self.repo, path=self.path, access_token=self.access_token)).text)['sha']

        key_file = key_file_str.split('\n')
        message = key_file[0]
        del key_file[0]

        # put last key "empty" to avoid the last key redisplay
        key_file[0] = "empty\n" if key_file[0] == "" else key_file[0]

        # 1.transform key_file back to key_file_str  2.str --> Byte(str) --> Byte(base64)
        content = base64.b64encode(bytes('\n'.join(key_file), 'utf-8'))
        payload_dict = {
            'access_token': self.access_token,
            'content': content,
            'sha': sha,
            'message': message
        }
        respose = requests.put(
            "https://{endpoint}/api/v5/repos/{owner}/{repo}/contents/{path}".format(endpoint=self.endpoint, owner=self.owner, repo=self.repo, path=self.path), data=payload_dict).text
        print (respose)
        return respose

    # @classmethod

    def get_key(self):
        """
        get current key & delete used key & update keyfile in gitee.com
        """
        key = self.get_current_key()
        # refresh keyfile
        self.update_key_file(self.get_key_file())
        return key

    def create_new_keys(self,newkeys):
        # get Blob SHA of the file
        newkeys=base64.b64encode(newkeys)
        sha = json.loads(requests.get(
            "https://{endpoint}/api/v5/repos/{owner}/{repo}/contents/{path}?access_token={access_token}".format(endpoint=self.endpoint, owner=self.owner, repo=self.repo, path=self.path, access_token=self.access_token)).text)['sha']

        # key_file = key_file_str.split('\n')
        message = newkeys

        # # 1.transform key_file back to key_file_str  2.str --> Byte(str) --> Byte(base64)
        # content = base64.b64encode(bytes('\n'.join(key_file), 'utf-8'))
        payload_dict = {
            'access_token': self.access_token,
            'content': newkeys,
            'sha': sha,
            'message': message
        }
        respose = requests.put(
            "https://{endpoint}/api/v5/repos/{owner}/{repo}/contents/{path}".format(endpoint=self.endpoint, owner=self.owner, repo=self.repo, path=self.path), data=payload_dict).text
        return respose