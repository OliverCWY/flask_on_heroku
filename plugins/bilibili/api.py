import requests
def getSongListInfo(input):
    input=str(input)
    if(input.find("am")!=-1):
        input=input[input.find("am")+2:]
    response=requests.get(f"https://www.bilibili.com/audio/music-service-c/web/menu/info?sid={input}").json()
    return response["data"] if response["msg"]=="success" else None

def getSongList(input):
    input=str(input)
    if(input.find("am")!=-1):
        input=input[input.find("am")+2:]
    response=requests.get(f"https://www.bilibili.com/audio/music-service-c/web/song/of-menu?sid={input}&pn=1&ps=1000000").json()
    return response["data"]["data"] if response["msg"]=="success" else None

def getSongInfo(input):
    input=str(input)
    if(input.find("au")!=-1):
        input=input[input.find("au")+2:]
    response=requests.get(f"https://www.bilibili.com/audio/music-service-c/web/url?sid={input}").json()
    return response["data"] if response["msg"]=="success" else None
