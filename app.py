from flask import Flask, render_template

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'Location': 'Bengaluru, India',
  'salary': 'Rs. 10,00,000',
}, {
  'id': 2,
  'title': 'Data Scientist',
  'Location': 'Delhi, India',
  'salary': 'Rs. 15,00,000',
}, {
  'id': 3,
  'title': 'Frontend Engineer',
  'Location': 'Remote',
}, {
  'id': 3,
  'title': 'Backend Engineer',
  'Location': 'San Fransisco, USA',
  'salary': '$150, 000',
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Abhinna')


@app.route("/api/jobs")
def list_jobs():
  return jasonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
