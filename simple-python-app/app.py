from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello I am Sharad Upadhyaya and I created ci/cd with aws successfully!'

if __name__ == '__main__':
    app.run()



