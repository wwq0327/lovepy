from twisted.internet import reactor
import time

def printTime():
    print "Current time is ", time.strftime("%H:%M:%S")
def stopReactor():
    print "Stopping reactor"
    reactor.stop()

for t in range(1,6):
    reactor.callLater(t, printTime)

reactor.callLater(6,stopReactor)

print 'Runing the reactor...'
reactor.run()
print 'Reactor stopped.'
