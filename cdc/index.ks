#codint:utf-8
from cdctools import *
print dir()

def _htmhead(title):
    htm = """<html><HEAD>
    <meta http-equiv="Content-Type" content="text/html;charset=utf-8"/>
    <title>%s</title></HEAD>
    <body>"""%title
    return htm
htmfoot="""
<h5>design by:<a href="mailto:wwq0327@gmail.com">Wyatt.Wang</a>
powered by:<a href="http://python.org">Python</a>+<a href="http://karrigell.sourceforge.net">Karrigell 3.1.1</a>
</h5>
</body></html"""

def index(**args):
    print _htmhead("PyCDC Web")
    print htmfoot
