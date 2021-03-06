#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
配置文件
__author__= 'jiangyixin'
__time__ = 2019/2/22 21:20
"""
import os

from dynaconf import settings


# 项目根目录
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Config:
    GITHUB_TOKEN_ACCESS_URL = 'https://github.com/login/oauth/access_token'
    GITHUB_CLIENT_ID = os.getenv('GITHUB_CLIENT_ID')
    GITHUB_CLIENT_SECRET = os.getenv('GITHUB_CLIENT_SECRET')


class DevelopmentConfig(Config):
    """开发环境配置"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{settings.get("DB_USER")}:{settings.get("DB_PASSWORD")}' \
                              f'@{settings.get("DB_HOST")}:{settings.get("DB_PORT")}/{settings.get("DB_NAME")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(Config):
    """测试环境配置"""
    pass


class ProductionConfig(Config):
    """生成环境配置"""
    pass


config = {
    'default': DevelopmentConfig,
    'development': DevelopmentConfig,
    'test': TestConfig,
    'production': ProductionConfig
}
