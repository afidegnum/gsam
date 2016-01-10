from flask_wtf import Form


# from flask_wtf import Form
from wtforms import StringField, TextAreaField, IntegerField, FileField, DateField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Required
from project import db
from project.idea.models import Category

def category_list():
        return db.session.query(Category)

class IdeaForm(Form):
    title = StringField("Title", validators=[DataRequired()])
    description = TextAreaField("Description")
    score = IntegerField("score", validators=[DataRequired()])
    category = QuerySelectField(get_label='category', query_factory=category_list)


# from flask_wtf import Form
class CategoryForm(Form):
    name = StringField("category Name", validators=[DataRequired()])
    Icon = FileField(u"Icon")


# from flask_wtf import Form
class CommentForm(Form):
    title = StringField("title", validators=[DataRequired()])
    description = TextAreaField("Description")


# from flask_wtf import Form
class ContestForm(Form):
    title = StringField("title", validators=[DataRequired()])
    end = DateField("Contest Ends", format='%Y-%m-%d')
    description = TextAreaField("Description")


