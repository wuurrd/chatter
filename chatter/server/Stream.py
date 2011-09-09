import xmlrpclib

class Stream(object):
    connection = None
    channel = None
    def __init__(self):
        pass

class StreamProxy:
    proxy = None #xmlrpclib.ServerProxy("localhost:8488")
