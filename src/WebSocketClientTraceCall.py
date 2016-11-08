# coding: utf-8
from __future__ import absolute_import

import aoiktracecall.config
import aoiktracecall.trace
import aoiktracecall.wrap


aoiktracecall.config.set_config('FIGLET_WIDTH', 200)


trace_specs = [
    ('aoiktracecall([.].+)?', False),

    ('.+[.]copy', False),

    ('.+[.]__setattr__', True),

    ('socket.IntEnum', False),

    ('socket._intenum_converter', False),

    ('socket[.].+[.]getsockname', False),

    ('socket[.].+[.]getpeername', False),

    ('(socket|SocketServer)[.].+[.]fileno', False),

    ('socket._realsocket', False),

    ('socket[.].+[.]__[^.]+__', False),

    ('socket([.].+)?', {'highlight'}),

    ('__main__[.].+[.]__[^.]+__', False),

    ('__main__([.].+)?', {'highlight'}),

    ('ws4py.streaming.Stream._cleanup', {'highlight'}),

    ('ws4py.framing.Frame._cleanup', {'highlight'}),

    ('ws4py[.].+[.]__init__', {'highlight'}),

    ('ws4py[.].+[.]__[^.]+__', False),

    ('ws4py([.].+)?', True),
]


aoiktracecall.trace.trace_calls_in_specs(specs=trace_specs)


from ws4py.client.threadedclient import WebSocketClient


class CustomClient(WebSocketClient):

    def opened(self):
        self.send('hello')

    def received_message(self, m):
        self.close()


def main():
    try:
        ws = CustomClient(
            'ws://127.0.0.1:9000/',
            protocols=['http-only', 'chat']
        )
        ws.connect()
        ws.run_forever()
    except KeyboardInterrupt:
        ws.close()


aoiktracecall.trace.trace_calls_in_this_module()


if __name__ == '__main__':
    exit(main())
