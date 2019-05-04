from flask import Blueprint,render_template,request,views,session,g
from exts import db
from .forms import APostForm,SigninForm
from ..front.models import ContextModel,BoardModel
from .models import AdminModel
from utils import restful
import config
from .decorators import login_required


cms_bp = Blueprint('cms',__name__,url_prefix='/cms')

@cms_bp.route('/',methods=['GET','POST'])
@login_required
def index():
    if request.method == 'GET':
        boards = BoardModel.query.all()
        context = {
            'boards':boards
        }
        return render_template("front/apost.html",**context)
    else:
        form  = APostForm(request.form)
        if form.validate():
            title = form.title.data
            context = form.context.data
            board_id = form.board_id.data
            board = BoardModel.query.get(board_id)
            if not board:
                return restful.paramserror_error('没有这个board ID')
            posts = ContextModel(title=title,context=context)
            posts.board = board
            db.session.add(posts)
            db.session.commit()
            return restful.success()
        else:
            return restful.paramserror_error('验证不通过')

class SigninView(views.MethodView):

    def get(self):
        return render_template('front/signin.html')

    def post(self):
        form = SigninForm(request.form)
        if form.validate():
            telep = form.telephone.data
            passwd = form.password.data
            user = AdminModel.query.filter_by(telephone=telep).first()
            if user and user.check_password(passwd):
                session[config.USER_ID] = user.id
                return restful.success()
            else:
                return restful.paramserror_error(message='用户名或密码错误')
        else:
            return restful.paramserror_error(message=form.get_error())
cms_bp.add_url_rule('/signin/',view_func=SigninView.as_view('signin'))
