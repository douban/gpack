#!/usr/local/bin/python2.7
#coding:utf-8

class Config(object):
    def __init__(self):
        self.http_config= {"upload_pack": True,
                           "receive_pack": True,
                           "git_path": "/Users/xtao/gentoo/usr/bin/git",
                           "project_root": "/Users/xtao/Work/code"}

config = Config()

