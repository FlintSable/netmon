import json

class ConfigManager:
    @staticmethod
    def load_config(config_file):
        with open(config_file, 'r') as f:
            return json.load(f)
        
    @staticmethod
    def save_config(config_file, config_data):
        with open(config_file, 'w') as f:
            json.dump(config_data, f, indeng=4)

