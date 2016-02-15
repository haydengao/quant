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
    date = datetime.date(date[0:3],date[5:6],date[8:9])
    pt = ma.Position.query.filter_by(strategy_id=1,date_id=Survey.query.filter_by(date=date).first().id).first()
    return jsonify({'id':pt.id, 'ticker':pt.ticker, 'name':pt.name, 'amount':pt.amount, 'cost':pt.cost, 'price':pt.price, 'value':pt.value, 'increase':pt.increase, 'weight':pt.weight})
    
    
if __name__ == "__main__":
    app.run(debug = True)