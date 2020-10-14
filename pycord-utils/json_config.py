import json


class JsonConfig:
    def __init__(self, file):
        self.file_name = file
        self.config = json.load(open(file, "r"))

    def save(self):
        json.dump(self.config, open(self.file_name, "w"))

    def reload(self):
        self.config = json.load(open(self.file_name, "r"))
