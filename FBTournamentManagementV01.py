from app import app, db
from app.models import User, Log
# app = Flask(__name__)
#
#

@app.shell_context_processor
def make_shell_context():
    return {'db':db, 'User':User, 'Log':Log}

# @app.route('/')
# def hello_world():
#     return 'Hello World!'
#
#

# if __name__ == "__main__":
# 	app.run(host='raspberrypi.local',port=8080, debug=True)
