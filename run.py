# /run.py
import os

from src.app import create_app

if __name__ == '__main__':
  env_name = os.getenv('FLASK_ENV')
  port = os.getenv('PORT')
  app = create_app(env_name)
  # run app
  app.run(host='0.0.0.0', port=port)
