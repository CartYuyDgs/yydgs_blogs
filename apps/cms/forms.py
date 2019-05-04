from wtforms import Form,StringField,IntegerField
from wtforms.validators import InputRequired,Regexp
from apps.forms import BaseForm


class APostForm(BaseForm):
    title = StringField(validators=[InputRequired(message='请输入标题！')])
    context = StringField(validators=[InputRequired(message='请输入内容！')])
    board_id = IntegerField(validators=[InputRequired(message='请输入板块ID！')])

class SigninForm(BaseForm):
    telephone = StringField(validators=[Regexp(r"1[345789]\d{9}", message='请输入正确格式的手机号码！')])
    password = StringField(validators=[Regexp(r"[0-9a-zA-Z_\.]{6,20}", message='请输入正确格式的密码！')])
    remeber = StringField()