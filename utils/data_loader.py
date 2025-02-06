import json

class DataLoader:
    @staticmethod
    def load_json(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)