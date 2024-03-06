from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, BooleanField, SelectMultipleField
from wtforms.validators import DataRequired


class DemoForm(FlaskForm):
    first_name = StringField('Имя', validators=[DataRequired()])
    last_name = StringField('Фамилия', validators=[])
    about_me = TextAreaField('Обо мне')
    sex = SelectMultipleField('Пол', choices=(
        ('m', 'муж'),
        ('f', 'жен'),
        ('none', 'не указывать') 
    ), default='f')
    submit = SubmitField('Отправить')


class TaskForm(FlaskForm):
    title = StringField("Заголовок")
    content = TextAreaField("Описание")
    isDone = BooleanField("Выполнено?")
    submit = SubmitField('Отправить')