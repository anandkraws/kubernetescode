from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Get the IP address of the incoming request
    pod_ip = request.remote_addr
    return f'Please run on EKS as well. Connected through pod IP: {pod_ip}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
