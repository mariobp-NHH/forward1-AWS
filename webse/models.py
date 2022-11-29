from datetime import datetime
from webse import application, db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Database User
class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    chats_gender = db.relationship('ChatGender', backref='author', lazy=True)
    questionnaires_gender = db.relationship('QuestionnaireGender', backref='author', lazy=True)
    chats_gd = db.relationship('ChatGD', backref='author', lazy=True)
    questionnaires_gd = db.relationship('QuestionnaireGD', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

# Database Gender Platform
class ChatGender(db.Model):
    __bind_key__ = 'gender_platform'
    __tablename__ = 'chat_gender'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"ChatGender('{self.title}', '{self.date_posted}')"

class QuestionnaireGender(db.Model):
    __bind_key__ = 'gender_platform'
    __tablename__= 'questionnaire_gender'
    id = db.Column(db.Integer, primary_key=True)
    title_questionnaire = db.Column(db.String(100), nullable=False)
    title_question = db.Column(db.String(100), nullable=False)
    question_num = db.Column(db.Integer)
    question_str = db.Column(db.String(100))
    question_option = db.Column(db.Integer, nullable=True)
    date_question = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"QuestionnaireGender('{self.question_str}', '{self.date_exercise}')"


# Database Green Digitalization Course

class ChatGD(db.Model):
    __bind_key__ = 'gd_course'
    __tablename__ = 'chat_gd'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"ChatGD('{self.title}', '{self.date_posted}')"  

class QuestionnaireGD(db.Model):
    __bind_key__= 'gd_course'
    __tablename__ = 'questionnaire_gd'
    id = db.Column(db.Integer, primary_key=True)
    title_questionnaire = db.Column(db.String(100), nullable=False)
    title_question = db.Column(db.String(100), nullable=False)
    question_num = db.Column(db.Integer)
    question_str = db.Column(db.String(100))
    question_option = db.Column(db.Integer, nullable=True)
    date_question = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"QuestionnaireGD('{self.question_str}', '{self.date_exercise}')"                 
        