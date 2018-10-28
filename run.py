# import os
from app import app

# config_name = os.getenv('APP_SETTINGS')
# this_app = app.create_app()

if __name__ == '__main__':
    app.run(debug=True)