#encoding:utf-8
import os
from flask import Flask,render_template
from flask.ext.sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

#策略
class Strategy(db.Model):
    __tablename__ = 'strategies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True) #策略名称
    status = db.Column(db.String(64)) #策略状态
    start = db.Column(db.Date) #策略开始时间
    end = db.Column(db.Date) #策略结束时间
    surveys = db.relationship('Survey', backref='strategy', lazy='dynamic')
    positions = db.relationship('Position', backref='strategy', lazy='dynamic')
    transfers = db.relationship('Position', backref='strategy_', lazy='dynamic')

    def __repr__(self):
        return '<Strategy %r>' % self.name

#每日概况
class Survey(db.Model):
    __tablename__ = 'surveys'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, index=True) #日期
    daily = db.Column(db.Float) #当日收益
    profit = db.Column(db.Float) #累计收益
    sharp = db.Column(db.Float) #夏普比率
    marketValue = db.Column(db.Float) #持仓市值
    enable = db.Column(db.Float) #可用金额
    pullback = db.Column(db.Float) #回撤
    alpha = db.Column(db.Float) #阿尔法
    beta = db.Column(db.Float) #贝塔
    information = db.Column(db.Float) #信息比率
    strategy_id = db.Column(db.Integer, db.ForeignKey('strategies.id')) #所属策略ID
    positions = db.relationship('Position', backref='date', lazy='dynamic')
    transfers = db.relationship('Transfer', backref='date_', lazy='dynamic')

    def __repr__(self):
        return '<Survey %r>' % self.date

#当日持仓
class Position(db.Model):
    __tablename__ = 'positions'
    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String(64), index=True) #证券代码
    name = db.Column(db.String(64)) #证券名称
    amount = db.Column(db.Integer) #持仓数量
    cost = db.Column(db.Float) #持仓成本
    price = db.Column(db.Float) #市价
    value = db.Column(db.Float) #市值
    increase = db.Column(db.Float) #当日涨幅
    weight = db.Column(db.Float) #权重
    strategy_id = db.Column(db.Integer, db.ForeignKey('strategies.id')) #所属策略ID
    date_id = db.Column(db.Integer, db.ForeignKey('surveys.id')) #所属日期ID

    def __repr__(self):
        return '<Position %r>' % self.ticker

#当日调仓
class Transfer(db.Model):
    __tablename__ = 'transfers'
    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String(64), index=True) #证券代码
    name = db.Column(db.String(64)) #证券名称
    direction = db.Column(db.String(64)) #买／卖
    orderAmount = db.Column(db.Integer) #下单数量
    dealAmount = db.Column(db.Integer) #成交数量
    orderTime = db.Column(db.Time) #下单时间
    dealTime = db.Column(db.Time) #成交时间
    cost = db.Column(db.Float) #成交均价
    status = db.Column(db.String(64)) #状态
    strategy_id = db.Column(db.Integer, db.ForeignKey('strategies.id')) #所属策略ID
    date_id = db.Column(db.Integer, db.ForeignKey('surveys.id')) #所属日期ID

    def __repr__(self):
        return '<Transfer %r>' % self.ticker

#基准
class Benchmark(db.Model):
    __tablename__ = 'benchmarks'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, unique=True, index=True) #日期
    index = db.Column(db.Float) #上证指数

    def __repr__(self):
        return '<Benchmark %r>' % self.date

#app.debug = True

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