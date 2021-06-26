from flask import Flask, request, send_from_directory
import socket

app = Flask(__name__, static_url_path='')

@app.route('/')
def echo_string():
    host_ip_address = socket.gethostbyname(socket.gethostname())
    return f'IP Address is  - {host_ip_address} , Echoing my_string - {request.args.get("my_string")}'

@app.route('/html/<path:path>')
def send_html(path):
    return send_from_directory('html', path)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
