#!/usr/local/bin/python2.7
#coding:utf-8

try:
    from gevent.monkey import patch_all
    patch_all(subprocess=False, aggressive=False)
    from gevent.pywsgi import WSGIServer
except ImportError:
    print 'You need install gevent manually! System shutdown.'

import config
from ghttp import GHTTPServer


def main():
    server = WSGIServer(('0.0.0.0', '8080'), GHTTPServer(config.http_config))
    server.serve_forever()


if __name__ == '__main__':
    main()

