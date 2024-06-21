import os
import yaml
import secrets


class Config:
    def __init__(self, config_path: str):
        self.config = self.load_config(config_path)

    def load_config(self, path: str) -> dict:
        with open(path, 'r') as file:
            return yaml.safe_load(file)

    def get(self, section: str, key: str):
        return self.config.get(section, {}).get(key)


# Initialize the Config object with the path to the YAML file
config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.yaml')
safety_config = Config(config_path)
