# -*- coding: utf-8 -*-
# @Author: Landers
# @Github: Landers1037
# @File: flask_config.py
# @Date: 2020-05-14

# flask的配置对象格式
from .read_config import read_config
from .check_config import check_config

# 一个可以实例化解析为配置对象的类
# 这里有一个顺序问题，flask优先加载这里的配置文件，那么init配置步骤就在这里进行


class flask_config:
    check_config()
    raw_config = read_config()
    DEBUG = raw_config.debug
    SQLALCHEMY_DATABASE_URI = raw_config.sqlite
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'This is a Secret Key'
    SERVER_NAME = raw_config.server_name
    MAX_CONTENT_LENGTH = raw_config.image_size