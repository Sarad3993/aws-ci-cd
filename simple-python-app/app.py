from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello I am Sarad and I am learning DevOps with AWS!'

if __name__ == '__main__':
    app.run()

