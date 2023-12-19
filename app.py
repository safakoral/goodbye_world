from flask import Flask
app = Flask(__name__)
@app.route('/bye')
def goodbye_world():
    return 'Goodbye World!'

if __name__ == '__main__':

    app.run(debug=True, host="dev.project.com", port="5001")