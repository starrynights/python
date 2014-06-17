#encoding:utf-8

import sys
import web
import datetime

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

#���ݿ�����
db = web.database(dbn = 'mysql', db = 'blog', user = 'root')

#��ȡ��������
def get_all_posts():
    return db.select('entries', order = 'id DESC')

#��ȡ��������
def get_post_by_id(id):
    try:
        return db.select('entries', where = 'id=$id', vars = locals())[0]
    except IndexError:
        return None

#�½�����
def new_post(title, content):
    db.insert('entries', title = title, content = content, posted_on = datetime.datetime.utcnow())

#ɾ������
def del_post_by_id(id):
    db.delete('entries', where = 'id=$id', vars = locals())

#�޸�����
def update_post(id, title, content):
    db.update('entries', where = 'id=$id', title = title, content = content, vars = locals())


