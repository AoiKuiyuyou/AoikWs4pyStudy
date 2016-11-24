[:var_set('', """
# Compile command
aoikdyndocdsl -s README.src.md -n aoikdyndocdsl.ext.all::nto -g README.md
""")
]\
[:HDLR('heading', 'heading')]\
# AoikWs4pyStudy
Python **WebSocket-for-Python (ws4py)** library study.

Tested working with:
- Python 3.5
- ws4py 0.3.5

Trace call using [AoikTraceCall](https://github.com/AoiKuiyuyou/AoikTraceCall):
- [WebSocketClientTraceCall.py](/src/WebSocketClientTraceCall.py)
- [WebSocketClientTraceCallLogPy3.txt](/src/WebSocketClientTraceCallLogPy3.txt?raw=True)
- [WebSocketClientTraceCallNotesPy3.txt](/src/WebSocketClientTraceCallNotesPy3.txt?raw=True)

## Table of Contents
[:toc(beg='next', indent=-1)]

## Set up AoikTraceCall
[:tod()]

### Setup via pip
Run:
```
pip install git+https://github.com/AoiKuiyuyou/AoikTraceCall
```

### Setup via git
Run:
```
git clone https://github.com/AoiKuiyuyou/AoikTraceCall

cd AoikTraceCall

python setup.py install
```

## Usage
[:tod()]

### Start server
Run:
```
python "AoikWs4pyStudy/src/WebSocketServer.py"
```

### Start client
Run:
```
python "AoikWs4pyStudy/src/WebSocketClientTraceCall.py" > Log.txt 2>&1
```
