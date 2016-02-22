#encoding:utf-8
from flask import (Flask, render_template, request, jsonify)
import myapp as ma

app = Flask(__name__)

@app.route('/')
def index():
    sttg_id = 1
    
    survey_ = ma.Survey.query.filter_by(strategy_id=sttg_id).all()
    survey = list(range(len(survey_)))
        
    for i in range(len(survey_)):
        survey[i] = {'date':survey_[i].date.strftime('%s')+'000','daily':survey_[i].daily,'profit':survey_[i].profit,'sharp':survey_[i].sharp,'marketValue':survey_[i].marketValue,'enable':survey_[i].enable,'benchmark':ma.Benchmark.query.filter_by(date=survey_[i].date).first().index,'pullback':survey_[i].pullback,'alpha':survey_[i].alpha,'beta':survey_[i].beta,'information':survey_[i].information,'fluctuation':survey_[i].fluctuation}
    
    return render_template('test.html',survey=survey)
