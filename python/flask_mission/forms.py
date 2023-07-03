from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class UserSignupForm(FlaskForm):
    userid = StringField('아이디', validators=[DataRequired(), Length(min=3, max=10)])
    password1 = PasswordField('비밀번호', validators=[DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다.')])
    password2 = PasswordField('비밀번호 확인', validators=[DataRequired()])
    email = TextField('이메일', validators=[DataRequired(), Email()])