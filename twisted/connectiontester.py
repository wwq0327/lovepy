from twisted.internet.selectreactor import SelectReactor
from twisted.internet.protocol import Protocol,ClientFactory,defer
reactor = SelectReactor()
class CallbackAndDisconnectProtocol(Protocol):
    def connectionMade(self):
        self.factory.deferred.callback("Connected!")
class ConnectionTestFactory(ClientFactory):
    protocol=CallbackAndDisconnectProtocol
    def __init__(self):
        self.deferred=defer.Deferred()
    def clientConnectionFailed(self,connector,reason):
        self.deferred.errback(reason)
def testConnect(host,port):
    testFactory=ConnectionTestFactory()
    reactor.connectTCP(host,port,testFactory)
    return testFactory.deferred
def handleSuccess(result,port):
    print "Connect to port %i"%port
    reactor.stop()
def handleFailure(failure,port):
    print "Error connecting to port %i: %s"%(
        port,failure.getErrorMessage())
    reactor.stop()
if __name__=="__main__":
    import sys
    if not len(sys.argv)==3:
        print "Usage: connectiontest.py host port"
        sys.exit(1)
    host=sys.argv[1]
    port=int(sys.argv[2])
    connecting=testConnect(host,port)
    connecting.addCallback(handleSuccess,port)
    connecting.addErrback(handleFailure,port)
    reactor.run()
