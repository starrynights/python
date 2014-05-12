#!/usr/bin/env python

import web

render = web.template.render('templates/')

urls = ('/(.*)/','redirect',
        "/.*", "hello")
app = web.application(urls, globals())

class hello:
    def GET(self):
        #return 'Hello World'
        #name = "Bob"
        i = web.input(name=None)
        return render.hello(i.name)

class redirect:
    def GET(self, path):
        web.seeother('/' + path)

if __name__ == "__main__":
    app.run()
