import os

SECRET_KEY = os.urandom(24)
debug = True
port = 8000

USER_ID = 'AAAAAA'

DB_USERNAME = 'root'
DB_PASSWORD = 'root'
DB_HOST = '127.0.0.1'
DB_PORT = '3306'
DB_NAME = 'blogs'

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(DB_USERNAME,DB_PASSWORD,DB_HOST,DB_PORT,DB_NAME)
SQLALCHEMY_TRACK_MODIFICATIONS = False


UEDITOR_UPLOAD_PATH=os.path.join(os.path.dirname(__file__),'images')
print(UEDITOR_UPLOAD_PATH)
UEDITOR_UPLOAD_TO_QINIU = False
UEDITOR_QINIU_ACCESS_KEY = "0t1qIGDKaYukQvf0vTRhd9MuEGiw0NSflm8TLsD5"
UEDITOR_QINIU_SECRET_KEY = "5g-tPtRU7S15PcAweZWaomKt2D1CQBAnwfVWGw49"
UEDITOR_QINIU_BUCKET_NAME = "yuy_space2"
UEDITOR_QINIU_DOMAIN = "http://www.yydgs.top.qiniudns.com/"

PER_PAGE = 10