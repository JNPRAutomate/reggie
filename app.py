import os
from flask import Flask, render_template
from flask.ext.script import Manager, Shell
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'reggie_magic_key'
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

manager = Manager(app)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    pod_number = db.Column(db.Integer, unique=True)
    username = db.Column(db.String(64))
    addr_wan = db.Column(db.String(16), unique=True)

    def __init__(self):
        self.pod_number = self._next_pod()

    def addr_lo0(self):
        addr = "10.255.255.{0}/32".format(self.pod_number)
        return addr

    def addr_st0(self):
        addr = "10.255.{0}.2/30".format(self.pod_number)
        return addr

    def _next_pod(self):
        MAX_PODS = 255
        new_pod_id = 1
        pods = Student.query.order_by('pod_number').all()
        for pod in pods:
            #print "Pod: {0} / {1}".format(pod.username, pod.pod_number)
            if new_pod_id == pod.pod_number:
                #print "Found ID: {0}".format(pod.pod_number)
                next
            else:
                #print "Unused: {0}".format(new_pod_id)
                return new_pod_id
            new_pod_id = new_pod_id + 1
            if new_pod_id > MAX_PODS:
                return False
        return False

    def __repr__(self):
        return '<Student {0} @ {1}>'.format(self.username, self.addr_wan)

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')

@manager.command
def db_mock():
    '''
    Create some test database entries
    '''
    group =[
        {'username': 'Kurt', 'pod_number': 9},
        {'username': 'Rob', 'pod_number': 10},
        {'username': 'John', 'pod_number': 5},
        {'username': 'Erin', 'pod_number': 21}
    ]

    for i in group:
        s = Student()
        s.username = i['username']
        s.pod_number = i['pod_number'] # Force out of order pods
        db.session.add(s)
        db.session.commit()

    return True


def make_shell_context():
    return dict(app=app, db=db, Student=Student)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', form=form, name=name)


if __name__ == '__main__':
    manager.run()