import os

# it`s no use at present
TOKEN_ENV = os.getenv('TOKEN')
def check_token(token):
    if (token == TOKEN_ENV):
        result = True
    else :
        result = False
    return result