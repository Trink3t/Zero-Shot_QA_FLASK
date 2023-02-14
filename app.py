#Creating a Flask Web Application

from flask import Flask, render_template, request
from zeroshot import ZeroShot as zs
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    country = None
    if request.method == 'POST':
        country = request.form.get('country')
        result = zs.get_answer(country)
    return render_template('index.html', result=result, country=country)

if __name__ == '__main__':
    app.run(debug=True)
