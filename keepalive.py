import os
from flask import Flask
from threading import Thread
from dotenv import load_dotenv

load_dotenv()

try:
  port = int(os.environ["PORT"])
except:
  port = 3000

app = Flask('')

@app.route('/')
def home():
  return "Staying alive :)"

def run():
  app.run(host='0.0.0.0', port=port)

def keepAlive():
  t = Thread(target=run)
  t.start()