from flask import Flask, render_template , jsonify

app = Flask(__name__)

Jobs = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Cairo,Egypt',
    'salary': '$1,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Cairo,Egypt',
    'salary': '$1,500'
  },
  {
    'id': 3,
    'title': 'Mechanical Engineer',
    'location': 'Cairo,Egypt',
    'salary': '$2,000'
  },
  {
    'id': 4,
    'title': 'Software Engineer',
    'location': 'Cairo,Egypt',
    'salary': '$2,000'
  }
]

@app.route("/")
def hello():
  return render_template('home.html', jobs=Jobs)

@app.route("/jobs")
def list_jobs():
  return jsonify(Jobs)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
