import yaml
import os

# This module provides a simple function to read and parse your YAML configuration file, 
# making it easy to access project settings throughout your code.
# It reads the configuration from a specified path (default is "config/config.yaml")
# and returns the configuration as a dictionary.
def load_config(config_path: str = "config/config.yaml") -> dict:
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
        # print(config)
    return config
