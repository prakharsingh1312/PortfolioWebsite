from flask import Flask ,  render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
#Tables
app.secret_key = 'popatpanda'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://Portfolio:Popat#Panda#1234$@34.67.79.192/Portfolio'
db=SQLAlchemy(app)

class Event(db.Model):
	__tablename__='event'
	id=db.Column('id', db.Integer, primary_key=True)
	type=db.Column('type', db.String(100), db.CheckConstraint("type in ('Education','Experience','Position Of Responsibility')"))
	date=db.Column('date', db.String(100))
	post=db.Column('post', db.String(100))
	employer=db.Column('employer', db.String(100))
	desc=db.Column('description', db.String(1000))

class Achievement(db.Model):
	__tablename__='achievement'
	id=db.Column('id', db.Integer, primary_key=True)
	icon=db.Column('icon', db.String(100), db.CheckConstraint("icon in ('flaticon-trophy','flaticon-quality')"))
	position=db.Column('position', db.String(100))
	organization=db.Column('organization', db.String(100))

class Skills(db.Model):
	__tablename__='skills'
	id=db.Column('id', db.Integer, primary_key=True)
	skill=db.Column('skill', db.String(100), unique=True)
	progress=db.Column('progress', db.Integer)

class Project(db.Model):
	__tablename__='project'
	id=db.Column('id', db.Integer, primary_key=True)
	name=db.Column('name', db.String(100))
	tech_stack=db.Column('tech_stack', db.String(100))
	image=db.Column('image', db.String(1000))
	desc=db.Column('description',db.String(1000))
	github_link=db.Column('github_link',db.String(100))
	web_link=db.Column('web_link',db.String(100))
	size=db.Column('size',db.Integer)

db.create_all()
#db.drop_all()
@app.route("/")
def hello():
	experience=Event.query.filter_by(type='Experience')
	education=Event.query.filter_by(type='Education')
	position=Event.query.filter_by(type='Position Of Responsibility')
	achievement=Achievement.query.all()
	skill=Skills.query.all()
	project=Project.query.all()
	return render_template('index.html',experiences=experience,positions=position,achievements=achievement,skills=skill,projects=project,educations=education)
if __name__ == "__main__":
    app.run()