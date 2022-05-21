import os

TOKEN_ENV = os.getenv('TOKEN')
def Check_token(token):
    if (token == TOKEN_ENV):
        result = True
    else :
        result = False
    return result