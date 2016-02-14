#encoding:utf-8
import os
from flask import Flask,render_template
from flask.ext.sqlalchemy import SQLAlchemy
import datetime
from flask_wtf import Form
from wtforms.fields.html5 import DateField

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.secret_key = 'SHH!'

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
    fluctuation = db.Column(db.Float) #收益波动率
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




class ExampleForm(Form):
    dt = DateField('DatePicker', format='%Y-%m-%d')




#app.debug = True

@app.route('/')
def index():
    today = datetime.date(2016,1,29)

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

        id = strategies_[i].id
        
        survey = Survey.query.filter_by(strategy_id=id,date=today).first()
    
        strategies[i] = {'name':strategies_[i].name,'status':strategies_[i].status,'daily':survey.daily,'profit':survey.profit,'start':start,'end':end}

    return render_template('index.html', strategies = strategies)


@app.route('/strategy/<name>')
def strategy(name):
    today = datetime.date(2016,1,29)
    date1 = today
    
    form1 = ExampleForm()
    if form1.validate_on_submit():
        date1 = form.dt.data

    
    
    strategy_ = Strategy.query.filter_by(name=name).first()

    if strategy_ == None:
        return '<h1>没有这个策略</h1>'
    else:
        sttg_id = strategy_.id

        survey_ = Survey.query.filter_by(strategy_id=sttg_id,date=today).first()
        
        survey = {'daily':survey_.daily,'profit':survey_.profit,'sharp':survey_.sharp,'marketValue':survey_.marketValue,'enable':survey_.enable,'pullback':survey_.pullback,'alpha':survey_.alpha,'beta':survey_.beta,'information':survey_.information,'fluctuation':survey_.fluctuation}

        transfer_ = Transfer.query.filter_by(strategy_id=sttg_id,date_id=Survey.query.filter_by(date=today).first().id).all()
        transfer = list(range(len(transfer_)))
        
        for i in range(len(transfer_)):
            deal_amount = '--'
            deal_time = '--'
            cost = '--'
            if transfer_[i].dealAmount == None:
                deal_amount = deal_amount
            else:
                deal_amount = transfer_[i].dealAmount

            if transfer_[i].dealTime == None:
                deal_time = deal_time
            else:
                deal_time = transfer_[i].dealTime.strftime('%H:%M:%S')
            
            if transfer_[i].cost == None:
                cost = cost
            else:
                cost = transfer_[i].cost
            
            transfer[i] = {'ticker':transfer_[i].ticker,'name':transfer_[i].name,'direction':transfer_[i].direction,'orderAmount':transfer_[i].orderAmount,'dealAmount':deal_amount,'orderTime':transfer_[i].orderTime,'dealTime':deal_time,'cost':cost,'status':transfer_[i].status}

        positions_ = Position.query.filter_by(strategy_id=sttg_id,date_id=Survey.query.filter_by(date=date1).first().id).all()
        positions = list(range(len(positions_)))

        for i in range(len(positions_)):
            positions[i] = {'ticker':positions_[i].ticker,'name':positions_[i].name,'amount':positions_[i].amount,'cost':positions_[i].cost,'price':positions_[i].price,'value':positions_[i].value,'increase':positions_[i].increase,'weight':positions_[i].weight}

        today = today.strftime('%Y-%m-%d')

        return render_template('strategy.html',name=name,survey = survey,positions = positions,transfer = transfer,date = today,form1 = form1)



@app.route('/test', methods=['POST','GET'])
def testForm():
    datee = '2013-01-03'
    form = ExampleForm()
    if form.validate_on_submit():
        datee = form.dt.data.strftime('%Y-%m-%d')
    return render_template('dp.html', form=form, datee = datee)