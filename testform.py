# Answer to a question on Flask mailing list
# http://librelist.com/browser//flask/2012/6/30/using-ajax-with-flask/
# NOTE: *REALLY* don't do the thing with putting the HTML in a global
#       variable like I have, I just wanted to keep everything in one
#       file for the sake of completeness of answer.
#       It's generally a very bad way to do things :)
#
from flask import (Flask, request, jsonify)
from flask_wtf import Form
from wtforms.fields.html5 import DateField
import myapp as ma
                   
app = Flask(__name__)

class ExampleForm(Form):
    dt = DateField('DatePicker', format='%Y-%m-%d')


@app.route('/', methods=['POST','GET'])
def index():
    today = datetime.date(2016,1,29)
    date1 = today
    
    form1 = ExampleForm()
    if form1.validate_on_submit():
        date1 = form.dt.data

    return render_template('test.html',form1 = form1)
        
        
@app.route('/ajax', methods = ['POST'])
def ajax_request():
    username = request.form['username']
    return jsonify(username=username)
    
    
if __name__ == "__main__":
    app.run(debug = True)