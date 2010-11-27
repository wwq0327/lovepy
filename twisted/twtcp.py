from twisted.internet.selectreactor import SelectReactor
from twisted.internet.protocol import Protocol, ClientFactory
reactor = SelectReactor()
protocol = Protocol()
class QuickDisconnectedProtocol(Protocol):
    def connectionMade(self):
        print "Connected to %s."%self.transport.getPeer().host
        self.transport.loseConnection()

class BasicClientFactory(ClientFactory):
    protocol = QuickDisconnectedProtocol
    def clientConnectionLost(self, connector, reason):
        print 'Lost connection:%s'%reason.getErrorMessage()
        reactor.stop()
    def clientConnectionFailed(self,connector,reason):
        print 'Connection failed: %s'%reason.getErrorMessage()
        reactor.stop()

reactor.connectTCP('www.google.com',80,BasicClientFactory())
reactor.run()
