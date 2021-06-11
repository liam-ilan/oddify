import os
from dotenv import load_dotenv
from flask import Flask
from threading import Thread
load_dotenv()

try:
  port = int(os.environ["PORT"])
except:
  port = 3000

app = Flask('')

@app.route('/')
def home():
  return "Stayin alive :)"

def run():
  app.run(host='0.0.0.0', port=port)

def keep_alive():
  t = Thread(target=run)
  t.start()