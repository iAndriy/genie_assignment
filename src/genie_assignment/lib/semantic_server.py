__author__ = 'aivaney'

import tornado.httpserver
import tornado.ioloop
from tornado import web
import os

def start_semantic_ui_server(port=8888):
    settings = {
    "static_path": get_semantic_static_path(),
    }
    ioloop = tornado.ioloop.IOLoop.instance()
    application = get_static_app(settings['static_path'])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(port)
    try:
        ioloop.start()
    except KeyboardInterrupt:
        tornado.ioloop.IOLoop.instance().stop()

def stop_tornado():
    ioloop = tornado.ioloop.IOLoop.instance()
    ioloop.add_callback(lambda x: x.stop(), ioloop)

def get_static_app(path=None):
    if path is None:
        path = get_semantic_static_path()
    return tornado.web.Application(handlers=[(r"/(.*)", web.StaticFileHandler, {"path": path}),], default_host="localhost")

def get_semantic_static_path():
    return os.path.join(os.path.dirname(__file__), "../static/Semantic-UI-gh-pages")