from flask import Flask

app = Flask('app')

@app.route('/')
def ping():
    return "PONG !, HELLO FROM MTC"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
