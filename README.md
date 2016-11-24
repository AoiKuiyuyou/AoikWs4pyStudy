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
- [Set up AoikTraceCall](#set-up-aoiktracecall)
  - [Setup via pip](#setup-via-pip)
  - [Setup via git](#setup-via-git)
- [Usage](#usage)
  - [Start server](#start-server)
  - [Start client](#start-client)

## Set up AoikTraceCall
- [Setup via pip](#setup-via-pip)
- [Setup via git](#setup-via-git)

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
- [Start server](#start-server)
- [Start client](#start-client)

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
