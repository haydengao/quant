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
    
    pt = ma.Position.query.filter_by(strategy_id=1,date_id=Survey.query.filter_by(date=formatDate).first().id).first()
    if pt == None:
        return jsonify({'name':999})
    else:
        return jsonify({'id':pt.id, 'ticker':pt.ticker, 'name':pt.name, 'amount':pt.amount, 'cost':pt.cost, 'price':pt.price, 'value':pt.value, 'increase':pt.increase, 'weight':pt.weight})


#   return jsonify({'name0':date[0:4],'name1':date[5:7],'name2':date[8:10]})
    
if __name__ == "__main__":
    app.run(debug = True)