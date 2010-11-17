from xml.sax.handler import ContentHandler
from xml.sax import parse

class TestHandler(ContentHandler):

    in_headline = False

    def __init__(self, headlines):
        ContentHandler.__init__(self)
        self.headlines = headlines
        self.data = []

    def startElement(self, name, attrs):
        #print name, attrs.keys()
        if name == 'h1':
            self.in_headline = True

    def endElement(self, name):
        if name == 'h1':
            text = ''.join(self.data)
            self.data = []
            self.headlines.append(text)
            self.in_headline = False

    def characters(self, string):
        if self.in_headline:
            self.data.append(string)

headlines = []

parse('website.xml', TestHandler(headlines))
print 'The following <h1> elements were found:'
for h in headlines:
    print h
