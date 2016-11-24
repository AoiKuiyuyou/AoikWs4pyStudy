# coding: utf-8
from __future__ import absolute_import

# Standard imports
from wsgiref.simple_server import make_server

# External imports
from ws4py.server.wsgirefserver import WebSocketWSGIRequestHandler
from ws4py.server.wsgirefserver import WSGIServer
from ws4py.server.wsgiutils import WebSocketWSGIApplication
from ws4py.websocket import EchoWebSocket


def main():
    # Create server
    server = make_server(
        host='127.0.0.1',
        port=9000,
        server_class=WSGIServer,
        handler_class=WebSocketWSGIRequestHandler,
        app=WebSocketWSGIApplication(handler_cls=EchoWebSocket)
    )

    # Initialize manager
    server.initialize_websockets_manager()

    # Run server
    server.serve_forever()


# If is run as main module
if __name__ == '__main__':
    # Call main function
    exit(main())
