#coding:utf-8
import web

db = web.database(
        dbn = 'mysql',
        user = 'root',
        pw = '123',
        db = 'webpy'
        )

render = web.template.render("templates/")

urls = (
        '/','index',
        '/add','add'
        )
app = web.application(urls, globals())

class index:
    def GET(self):
        todos = db.select('todo') #选择weypy数据中的todo表。
        return render.index(todos)
class add:
    def POST(self):
        i = web.input()
        n = db.insert('todo',title=i.title)
        raise web.seeother('/')

#web.webapi.internalerror = web.debugerror
if __name__ == "__main__":app.run()
