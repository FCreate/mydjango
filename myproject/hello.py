from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    global counter 
    counter+=1
    return str(counter)
counter=0
if __name__ == '__main__':
    app.run()
