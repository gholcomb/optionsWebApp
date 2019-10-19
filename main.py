from flask import Flask, render_template
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
import playground
from flask import jsonify
import sys

app = Flask(__name__, template_folder="templates")
app.config['SECRET_KEY'] = "Jyq35Qbpjt"

class NameForm(Form):
    name = StringField('Enter a stock', validators=[Required()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    table = None
    dates = "NONE"
    chain = 'None'
    form = NameForm()
    name = form.name.data
    if name:
        table = playground.fetchStockInfo(name)
        dates = playground.getExpDates(name)
        chain = playground.getOptionChain(name)
        form.name.data = ''
    return render_template('index.html', form=form, name=name, table=table, dates=dates, chain=chain)

@app.route('/background_process')
def background_process():
    try:
        lang = request.args.get('proglang')
        if str(lang).lower() == 'python':
            return jsonify(result='You are wise')
        else:
            return jsonify(result='Try again')
    except Exception as e:
        return str(e)



if __name__ == "__main__":
    app.run(debug=True)
