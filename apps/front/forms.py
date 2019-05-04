from wtforms import Form,StringField,IntegerField
from wtforms.validators import InputRequired,Regexp
from apps.forms import BaseForm

class SearchForm(BaseForm):
    text = StringField(validators=[InputRequired(message='请输入名称！')])