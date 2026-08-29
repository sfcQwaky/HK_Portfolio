from flask import Flask, render_template
from content import Record, Base
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///my_protfolio.db"
db = SQLAlchemy(model_class=Base)

db.init_app(app)


@app.route('/')
def index():
    latest_projects=db.session.query(Record).order_by(Record.id)
    tmp_projects = latest_projects.all()
    return render_template('home.html', temp_projects=tmp_projects)

@app.route('/projects')
def projects():
    return render_template('projects_overview.html')

# @app.route('/project/<int:project_id>')
# def single_projects(project_id):
#
#    return render_template('project.html')


if __name__ == "__main__":
    app.run(debug=True, port=5001)