import json

class Event:
    def __init__(self, obj):
        self.name = obj["name"]
        self.content = obj["text"]

        if "question" in obj.keys():
            self.has_choice = True
            self.question = obj["question"]
            self.choices = obj["responses"]
        else:
            self.has_choice = False
            self.effect = obj["effect"]

    @staticmethod
    def generate_morning_events():
        with open("src/data/morning_events.json", "r") as f:
            data = json.load(f)

            for ele in data:
                yield Event(ele)

print(list(Event.generate_morning_events()))