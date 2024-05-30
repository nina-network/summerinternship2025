from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.get('/')
def index():

    today = datetime.now().date()
    last_day = datetime(today.year, 12, 31).date()
    
    days_left = (last_day - today).days

    return render_template('index.html', today = today, last_day = last_day, days_left = days_left)
    
if __name__ == '__main__':
    app.run(debug=True)