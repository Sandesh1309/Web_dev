from flask import Flask, render_template
app = Flask(__name__)
JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'Salary': 'Rs.1200000'
  },
  {
    'id': 2,
    'title': 'Front-End Engineeer',
    'location': 'Bengaluru, India',
    'Salary': 'Rs.1300000'
  },
  {
      'id': 3,
      'title': 'Full-stack Developer',
      'location': 'Bengaluru, India',
      'Salary': 'Rs.1250000'
  },
  {
    'id': 4,
    'title': 'Data scientist',
    'location': 'USA',
    'Salary': '$.15000'
  }
]
@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name="Sandy")

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)