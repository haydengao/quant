from flask import (Flask, request, jsonify, render_template)
import datetime
import myapp as ma
                   
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('test.html')
        
        
@app.route('/positions', methods = ['POST'])
def positions_ajax_request():
    date = request.form['date']
    formatDate = datetime.date(int(date[0:4]),int(date[5:7]),int(date[8:10]))
    dateID = ma.Survey.query.filter_by(date=formatDate).first()
    if dateID != None:
        pt_ = ma.Position.query.filter_by(strategy_id=1,date_id=dateID.id).all()
        if pt_ == None:
            return jsonify({'name':"该日没数据"})
        else:
            pt = list(range(len(pt_)))
            
            for i in range(len(pt_)):
                pt[i] = {'ticker':pt_[i].ticker, 'name':pt_[i].name, 'amount':pt_[i].amount, 'cost':pt_[i].cost, 'price':pt_[i].price, 'value':pt_[i].value, 'increase':pt_[i].increase, 'weight':pt_[i].weight}
            
            return jsonify(results=pt)
    else:
        return jsonify({'name':"该日没数据"})



@app.route('/transfers', methods = ['POST'])
def transfers_ajax_request():
    date = request.form['date']
    formatDate = datetime.date(int(date[0:4]),int(date[5:7]),int(date[8:10]))
    dateID = ma.Survey.query.filter_by(date=formatDate).first()
    if dateID != None:
        ts_ = ma.Transfer.query.filter_by(strategy_id=1,date_id=dateID.id).all()
        if ts_ == None:
            return jsonify({'name':"该日没数据"})
        else:
            ts = list(range(len(ts_)))
            
            for i in range(len(ts_)):
                deal_amount = '--'
                deal_time = '--'
                cost = '--'
                if ts_[i].dealAmount != None:
                    deal_amount = ts_[i].dealAmount
                
                if ts_[i].dealTime != None:
                    deal_time = ts_[i].dealTime.strftime('%H:%M:%S')
                
                if ts_[i].cost != None:
                    cost = ts_[i].cost
                
                ts[i] = {'ticker':ts_[i].ticker, 'name':ts_[i].name, 'direction':ts_[i].direction, 'orderAmount':ts_[i].orderAmount, 'dealAmount':deal_amount, 'orderTime':ts_[i].orderTime.strftime('%H:%M:%S'), 'dealTime':deal_time, 'cost':cost, 'status':ts_[i].status}
            
            return jsonify(results=ts)
    else:
        return jsonify({'name':"该日没数据"})

    
if __name__ == "__main__":
    app.run(debug = True)