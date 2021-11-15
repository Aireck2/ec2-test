from flask import Flask

app = Flask(__name__)
app_settings = 'helpers.config.DevelopmentConfig'
app.config.from_object(app_settings)

@app.get('/')
def index():
  return f'Hola'