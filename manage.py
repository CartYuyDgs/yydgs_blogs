from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from app import create_app
from apps.front import front_bp
from exts import db
from apps.front.models import ContextModel,BoardModel,Crawl_poem
from apps.cms.models import AdminModel
import requests
from lxml import etree
import time

Article = ContextModel
Post = BoardModel
Poem = Crawl_poem
app = create_app()
manage = Manager(app)
magrate = Migrate(app,db)
manage.add_command('db',MigrateCommand)

@manage.option('-t','--telephone',dest='telephone')
@manage.option('-p','--password',dest='password')
@manage.option('-e','--email',dest='email')
def add_admin(telephone,password,email):
    admin = AdminModel(telephone=telephone,password=password,email=email)
    db.session.add(admin)
    db.session.commit()
    print('管理员添加成功')

@manage.option('-t','--title',dest='title')
@manage.option('-c','--context',dest='context')
@manage.option('-d','--board_id',dest='board_id')
def create_context(title,context,board_id):
    articles = Article(title=title,context=context,board_id=board_id)
    db.session.add(articles)
    db.session.commit()
    print('文章添加成功')

@manage.option('-p','--post',dest='post')
def create_post(post):
    posts = Post(name=post)
    db.session.add(posts)
    db.session.commit()
    print('添加类别成功！')

@manage.command
def add_content():
    for i in range(20):
        title = 'cocos标题'+str(i)
        content = '内容'+str(i)
        create_context(title=title,context=content,board_id=7)

@manage.command
def crowl_get_poem():

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    url = 'https://www.juzimi.com/article/%E7%BA%A2%E6%A5%BC%E6%A2%A6?page='
    for i in range(93):
        urls = url+str(i)
        res = requests.get(url=urls,headers=headers)
        context = res.text
        html = etree.HTML(context)
        divs = html.xpath('.//div[@class="views-field-phpcode"]')
        time.sleep(2)
        print(urls)
        for div in divs:

            author = div.xpath('./div[2]/a/text()')
            if not author:
                author = '曹雪芹'
            title = div.xpath('./div[2]/span/a/text()')
            con = div.xpath('./div[1]/a/text()')
    # url = 'http://www.tw117.com/mingyan-shu/%E7%89%A1%E4%B8%B9%E4%BA%AD/'
    # url = 'http://www.tw117.com/mingyan-shu/%E7%B4%85%E6%A8%93%E5%A4%A2/'
    # for i in range(11):
    #     urls = url + '/' + str(i) + '/'
    #     res = requests.get(url=urls, headers=headers)
    #     context = res.text
    #     html = etree.HTML(context)
    #     time.sleep(2)
    #     lis = html.xpath(".//ul[@class='mingyan-list']/li")
    #     for li in lis:
    #         text = li.xpath('./div[1]//a/text()')
    #         title = text[-1]
    #         author = text[-2]
    #         con = text[:-2]
            poem = Poem(title=title,author = author,context=str(con))
            db.session.add(poem)
            db.session.commit()


if __name__ == '__main__':
    manage.run()
