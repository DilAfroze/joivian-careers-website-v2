from flask import Flask, render_template, jsonify
from database import load_jobs_from_db

# Creating a flask object
app = Flask(__name__)


# route to main website
@app.route("/")
def hello_jovian():
	jobs = load_jobs_from_db()
	return render_template('home.html', jobs=jobs, company_name='Jovian')

# route to a json jobs webpage
@app.route("/api/jobs")
def list_jobs():
	jobs = load_jobs_from_db()
	return jsonify(jobs)

# using our flask object to run our app
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)