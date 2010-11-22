from xml.sax.handler import ContentHandler
import xml.sax
import sys
class testHandler(ContentHandler):
    def characters(self, ch):
        sys.stdout.write(ch.encode("Latin-1"))

parser = xml.sax.make_parser()
handler = testHandler()
parser.setContentHandler(handler)
parser.parse("test.xml")
