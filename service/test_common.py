from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
  import demo_common
  return ('demo_common version installed: {}'
          .format(demo_common.__version__))
