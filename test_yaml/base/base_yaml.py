import yaml
import os
import sys

sys.path.append(os.getcwd())


def get_yaml_as_file_name(file_name):
    with open("./data/{}.yml".format(file_name), "r", encoding="utf-8")as f:
        return yaml.load(f, Loader=yaml.FullLoader)
