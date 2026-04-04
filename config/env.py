import yaml
import os
class ConfigReader:

    @staticmethod #we dont have to create an object because its a static method
    def read_config():
        config_path=os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "config", #directory name
            "env.yaml" #file name
        )
        with open(config_path) as file:
            return yaml.safe_load(file)