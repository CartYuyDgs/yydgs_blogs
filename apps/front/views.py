from flask import Blueprint,render_template,request,abort,redirect,url_for
from exts import db
from .models import Crawl_poem,ContextModel
from .forms import SearchForm
import random,config
from utils import restful
from flask_paginate import Pagination,get_page_parameter

front_bp = Blueprint('front',__name__)

@front_bp.route('/')
def index():
    board_id = request.args.get('db',type=int,default=None)
    poem_title,poem_author,poem_text = get_poem()

    page = request.args.get(get_page_parameter(), type=int, default=1)
    start = (page - 1) * config.PER_PAGE
    end = start + config.PER_PAGE
    query_obj = ContextModel.query.order_by(ContextModel.create_time.desc())
    if board_id:
        query_obj = query_obj.filter(ContextModel.board_id==board_id)
        posts = query_obj.slice(start,end)
        total = query_obj.count()
    else:
        posts = query_obj.slice(start, end)
        total = query_obj.count()

    pagination = Pagination(bs_version=3, page=page, total=total, outer_window=0, inner_window=2)
    # text = ['人生海海', '潮落之后是潮起', '你说那是消磨，笑柄，罪过', '但那是我的英雄主义']
    # author = '麦家'
    # print(text)
    contexts = {
        'poem_title':poem_title,
        'poem_text': poem_text,
        'poem_author': poem_author,
        'posts':posts,
        'pagination':pagination,
        'current_id':board_id
    }
    return render_template('front/index.html', **contexts)

def get_poem():
    num = random.randint(1, 310)
    poem = Crawl_poem.query.get(num)
    poem_text = poem.context[1:-1].split(",")
    poem_author = poem.author
    poem_title = poem.title
    return (poem_title,poem_author,poem_text)

@front_bp.route('/p/<post_id>/')
def pdetail(post_id):
    post = ContextModel.query.get(post_id)
    if not post:
        abort(404)
    return render_template('front/pdetail.html',post=post)

# @front_bp.route('/s/',methods=['POST'])
# def search():
#     form = SearchForm(request.form)
#     text = form.text.data
#     if form.validate():
#         post = ContextModel.query.filter(ContextModel.title==text).first()
#         # return render_template('front/pdetail.html',post=post)
#         return redirect(url_for('front.pdetail',post_id=post.id))
#     else:
#         return restful.paramserror_error(form.get_error())