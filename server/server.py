import flask

app = flask.Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def test():
    return "<h1>Wine Closet Test<h1><p>The server is working</p>"

@app.route('/')
def test2():
    return
app.run()