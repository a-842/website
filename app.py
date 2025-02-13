from flask import Flask, redirect, request
import requests

app = Flask(__name__)

WEB2_URL = "http://localhost:5001"  # Change to web2's actual address

@app.route('/assassin/<path:subpath>')
def proxy_to_web2(subpath):
    web2_response = requests.get(f"{WEB2_URL}/{subpath}", params=request.args)
    return (web2_response.text, web2_response.status_code, web2_response.headers.items())

if __name__ == '__main__':
    app.run(port=5000, host=0.0.0.0)
