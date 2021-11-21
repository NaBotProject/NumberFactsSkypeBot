from skpy import SkypeEventLoop,SkypeNewMessageEvent
import requests
def checkInt(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

def getFact(num):
    r = requests.get(url = "http://numbersapi.com/"+num,json=False)
    return r.json()["text"]

class MySkype(SkypeEventLoop):
    def onEvent(self, event):            
        for request in self.contacts.requests():
                request.accept()
        if isinstance(event, SkypeNewMessageEvent) \
          and not event.msg.userId == self.userId :
            for request in self.contacts.requests():
                request.accept()
            if(event.msg.content == "about" or checkInt(event.msg.content)):
                msg = "https://github.com/NaBotProject" if event.msg.content == "about" else getFact(event.msg.content)
                event.msg.chat.sendMsg(msg)

if __name__ == "__main__":
    sk = MySkype("email", "pass", autoAck=True)
    print("Ready!")
    sk.loop()
