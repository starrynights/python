#encoding:utf-8

import sys
import web
import model

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding("utf-8")
#urlӳ��
urls = (
        '/', 'Index',
        '/view/(\d+)', 'View',
        '/new', 'New',
        '/delete/(\d+)', 'Delete',
        '/edit/(\d+)', 'Edit',
        '/login', 'Login',
        '/logout', 'Logout'
        )
app = web.application(urls, globals())

#ģ�湫������
t_globals = {
        'datestr': web.datestr,
        'cookie': web.cookies,
}

#ָ��ģ��Ŀ¼�����趨����ģ��
render = web.template.render('templates', base = 'base', globals = t_globals)

#������½��
login = web.form.Form(
        web.form.Textbox('username'),
        web.form.Password('password'),
        web.form.Button('login')
        )

#��ҳ��
class Index:
    def GET(self):
        login_form = login
        posts = model.get_all_posts()
        return render.index(posts, login_form)
    def POST(self):
        login_form = login()
        if login_form.validates():
            if login_form.d.username == 'admin' and login_form.d.password == 'admin':
                web.setcookie('username', login_form.d.username)
        raise web.seeother('/')

#�鿴������
class View:
    def GET(self, id):
        post = model.get_post_by_id(int(id))
        if post == None:
            return web.notfound("Sorry, the post you are looking for is not exist")
        return render.view(post)

#�½�������
class New:
    form = web.form.Form(
            web.form.Textbox('title', web.form.notnull, size=30, description = 'Post title: '),
            web.form.Textarea('content', web.form.notnull, rows = 30, cols = 80, description = "Post content: "),
            web.form.Button('Post entry'),
            )
    def GET(self):
        form = self.form
        if not web.cookies().get('username'):
            web.seeother('/')
        return render.new(form)
    def POST(self):
        form = self.form
        if not web.cookies().get('username'):
            web.seeother('/')
        if not form.validates():
            return render.new(form)
        model.new_post(form.d.title, form.d.content)
        raise web.seeother('/')

#ɾ��������
class Delete:
    def POST(self, id):
        model.del_post_by_id(int(id))
        raise web.seeother('/')

#�༭������
class Edit:
    def GET(self, id):
        post = model.get_post_by_id(int(id))
        form = New.form()
        form.fill(post)
        return render.edit(post, form)
    def POST(self, id):
        post = model.get_post_by_id(int(id))
        form = New.form()
        if not form.validates():
            return render.edit(post, form)
        model.update_post(int(id), form.d.title, form.d.content)
        raise web.seeother('/')

#�˳���½
class Logout:
    def GET(self):
        web.setcookie('username', '', expires = -1)
        raise web.seeother('/')

#����404��ʾ����
def notfound():
    return web.notfound("Sorry, the page you are looking for was not found")

#����
if __name__ == '__main__':
    app.run()

