from flask import Flask
import socket


app = Flask('webapp')

@app.route('/')
def endpoint():
    return "this is the webserver: "+socket.gethostname()+"\n"



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9772)