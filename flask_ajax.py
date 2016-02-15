from flask import (Flask, request, jsonify, render_template)
import myapp as ma
                   
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('test.html')
        
        
@app.route('/ajax', methods = ['POST'])
def ajax_request():
    date = request.form['date']
    return jsonify(date=date)
    
    
if __name__ == "__main__":
    app.run(debug = True)