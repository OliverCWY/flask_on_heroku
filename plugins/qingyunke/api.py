import requests
from urllib.parse import urlencode
def get_response(msg):
    key={
        "key":"free",
        "appid":0,
        "msg":msg
    }
    response=requests.get("http://api.qingyunke.com/api.php?"+urlencode(key)).json()
    return None if response["result"] else response["content"]
