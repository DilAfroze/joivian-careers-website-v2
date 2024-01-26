from sqlalchemy import create_engine, text
import os

# string used to connect to the database
db_connection_string = os.environ['DB_CONNECT_STRING']

# connecting to the database
engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                           "ssl_ca": "/etc/ssl/cert.pem" #ssl security certificate for connection
                       }})

#loading jobs from the database
def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._asdict())

    return jobs

def load_job_from_db(var):
	with engine.connect() as conn:
		# String formating for query
		result = conn.execute(text("SELECT * FROM jobs WHERE id = :var"), {'var': var})
		rows = result.all()
		if len(rows) == 0:
			return None
		else:
			return dict(rows[0])