from flask import Flask



app = Flask(__name__)



@app.route('/bye')

def goodbye__world():

    return 'Goodbye, World!'



if __name__ == '__main__':

    app.run(debug=True)

