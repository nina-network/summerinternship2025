from flask import Flask, render_template
from datetime import datetime
from repositories import internship_data

app = Flask(__name__)

@app.get('/')
def index():

    today = datetime.now().date()
    last_day = datetime(today.year, 12, 31).date()
    
    days_left = (last_day - today).days

    return render_template('index.html', today = today, last_day = last_day, days_left = days_left)

@app.get('/internships')
def internships():

    all_data = internship_data.all_data()

    return render_template('internships.html', all_data=all_data)

@app.get('/internship/<int:id>')
def internship(id):

    data = internship_data.internship(id)

    return render_template('internship.html', data=data)

@app.get('/contact')
def contact():

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)