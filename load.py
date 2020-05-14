import json
from text_func import func

class load():
    def _init_(self, mode="std"):
        head, text, emoji, url = self.load()

        if mode != "random":
            text = func()._init_(text, mode=mode)
        else:
            pass

        return head, text, emoji, url

    def load(self):
        with open("settings.json", "r", encoding="utf8") as set:
            setting = json.load(set)

        head = setting["head"]
        text = setting["text"]
        emoji = setting["emoji"]
        url = setting["url"]

        ch = self.check(head, text, url)

        if ch == 3:
            return head, text, emoji, url
        else:
            return None

    def check(self, head, text, url):

        good = 0

        if head["Authorization"] == None:
            print('Write your AuthToken in "settings.json"')
        elif head["Content-type"] != "application/json":
            print('don`t change other parameters')
        else:
            good += 1

        if text == None:
            print('Write your text in "settings.json"')
        else:
            good += 1

        if url != "https://discordapp.com/api/v6/users/@me/settings":
            print("don`t change link of discord")
        else:
            good += 1

        return good
