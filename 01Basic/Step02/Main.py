from flask import Flask
app = Flask(__name__)

@app.route('/')
def root():
  return 'Hello Flask(Main.py)'

# 실행
'''
set FLASK_APP=Main.py
set FLASK_DEBUG=1
flask run
'''