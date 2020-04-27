import flask

app = flask.Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def test():
    return "<h1>Wine Closet Test<h1><p>The server is working</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)