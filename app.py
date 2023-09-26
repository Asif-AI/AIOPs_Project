from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def Index():
    return "Hello All"

if __name__ == '__main__':
    app.run(port=8080)
