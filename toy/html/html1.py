import HTMLParser
import urllib

class parseLinks(HTMLParser.HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            for name, value in attrs:
                if name == 'src':
                    print 'value ==>'+value
                    print '<a href>==>'+self.get_starttag_text()
IParser = parseLinks()
IParser.feed(urllib.urlopen('http://www.python.org/').read())
IParser.close()
