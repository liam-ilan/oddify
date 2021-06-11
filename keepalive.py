import os
from dotenv import load_dotenv
from flask import Flask
from threading import Thread
load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
  return "Stayin alive :)"

app.run(host='0.0.0.0')
