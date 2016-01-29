#encoding:utf-8
import sys
import os
from flask import Flask,render_template
from flask.ext.sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)
#app.debug = True

class Strategy(db.Model):
    __tablename__ = 'strategies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    status = db.Column(db.String(64))
    daily = db.Column(db.Float)
    profit = db.Column(db.Float)
    start = db.Column(db.Date)
    end = db.Column(db.Date)

    def __repr__(self):
        return '<Strategy %r>' % self.name


@app.route('/')
def index():

    strategies_ = Strategy.query.all()
    strategies = list(range(len(strategies_)))

    for i in range(len(strategies_)):
        start = '_'
        end = '_'
        if strategies_[i].start == None:
            start = start
        else:
            start = strategies_[i].start.strftime('%Y-%m-%d')
    
        if strategies_[i].end == None:
            end = end
        else:
            end = strategies_[i].end.strftime('%Y-%m-%d')
    
        strategies[i] = {'name':strategies_[i].name,'status':strategies_[i].status,'daily':strategies_[i].daily,'profit':strategies_[i].profit,'start':start,'end':end}

    return render_template('index.html', strategies = strategies)


@app.route('/strategy/<name>')
def strategy(name):
    strategy_ = Strategy.query.filter_by(name=name).first()

    if strategy_ == None:
        return '<h1>没有这个策略</h1>'
    else:
        start = '_'
        end = '_'
        if strategy_.start == None:
            start = start
        else:
            start = strategy_.start.strftime('%Y-%m-%d')
        
        if strategy_.end == None:
            end = end
        else:
            end = strategy_.end.strftime('%Y-%m-%d')

        strategy = {'name':strategy_.name,'status':strategy_.status,'daily':strategy_.daily,'profit':strategy_.profit,'start':start,'end':end}
        return render_template('strategy.html',strategy = strategy)