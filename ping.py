import os
from flask import Flask

app = Flask(__name__)

# for uptime robot to ping and keep alive
@app.route('/')
def home():
  return "Hello :)"