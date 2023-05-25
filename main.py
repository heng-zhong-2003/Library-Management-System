from flask_cors import CORS
from app import create_app
from config import config

environment = config['development']
app = create_app(environment)
cors = CORS(app)
cors.init_app(app, resource={r"/*": {"origins": "*"}})
if __name__ == '__main__':
    app.run()