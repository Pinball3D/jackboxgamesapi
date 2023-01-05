import json
import uuid
from enum import Enum
import websocket


class appTags(Enum):
    QUIPLASH = "quiplash"
    QUIPLASH2 = "quiplash2"
    QUIPLASH3 = "quiplash3"
    FIBBAGE = "fibbage"
    FIBBAGE2 = "fibbage2"
    FIBBAGE3 = "fibbage3"
    FIBBAGE4 = "fibbage4"
    WHEELOFENORMOUSPROPORTIONS = "the-wheel"

class host():
    def __init__(self, appTag):
        self.appTag = appTag.value
        import http.client
        conn = http.client.HTTPSConnection("ecast.jackboxgames.com")
        conn.request("POST", "/api/v2/rooms?userId="+str(uuid.uuid4())+"&appTag="+self.appTag)
        res = conn.getresponse()
        data = res.read().decode("utf-8")
        response = json.loads(data)
        self.token = response["body"]["token"]
        self.code = response["body"]["code"]
        print("Game Code: " + self.code)
        self.host = response["body"]["host"]
        self.connectWS()
    def connectWS(self):
        def on_message(wsapp, message):
            print(message)
        wsapp = websocket.WebSocketApp("wss://"+self.host+"/api/v2/rooms/"+self.code+"/play?role=host&format=json&host-token="+self.token, subprotocols=["ecast-v0"], on_message=on_message)
        wsapp.run_forever()


game = host(appTags.QUIPLASH3)
