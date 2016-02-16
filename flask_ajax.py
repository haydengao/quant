from flask import (Flask, request, jsonify, render_template)
import datetime
import myapp as ma
                   
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('test.html')
        
        
@app.route('/ajax', methods = ['POST'])
def ajax_request():
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
            
            return jsonify([{'ticker':'a1' 'name':'a2', 'amount':'a3', 'cost':'a4', 'price':'a5', 'value':'a6', 'increase':'a8', 'weight':'a9'},{'ticker':'b1', 'name':'b2', 'amount':'b3', 'cost':'b4', 'price':'b6', 'value':'b7', 'increase':'b8', 'weight':'b9'}])
    else:
        return jsonify({'name':"该日没数据"})


#    return jsonify({'name':formatDate.strftime('%Y-%m-%d')})
    
if __name__ == "__main__":
    app.run(debug = True)