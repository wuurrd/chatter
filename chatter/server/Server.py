import logging
import sys
import time
from chatter.server.Stream import Stream

log = logging.getLogger(__name__)

def test():
    for x in xrange(0,20):
        sys.stdout.write('\r [%2i]' % x)
        sys.stdout.flush()
        time.sleep(1)

def start():
    stream = Stream()
    log.debug("Start server")
    print 'start'
    test()
    #run server
