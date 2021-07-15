# -*- coding:utf-8 -*-
import os, sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

global_config = None
global_meta = None


def set_config(config):
    global global_config
    assert global_config is None
    global_config = config


def set_config_path(config_path):
    import json
    with open(config_path, encoding='utf-8') as f:
        config = json.load(f)
        set_config(config)


def new_content():
    global global_config, global_meta
    if global_config is None:
        set_config_path(os.path.join(os.path.dirname(__file__), 'config/hemo_dialysis_data.json'))
    if global_meta is None:
        pass


if __name__ == '__main__':
    import pprint
