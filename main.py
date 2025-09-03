from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
   return {"status": "healthy", "service": "ping-service"}, 200


@app.route('/health2', methods=['GET'])
def health():
   return {"status": "healthy2", "service": "ping-service"}, 200

@app.route('/health3', methods=['GET'])
def health():
   return {"status": "healthy2", "service": "ping-service"}, 200


## ping service for employees
@app.route('/ping', methods=['GET'])
def ping():
   host = request.args.get('host', 'localhost')
   os.system(f'ping -c 1 {host}')
   return f"Ping sent", 200

if __name__ == '__main__':
   app.run(debug=False, port=5001)
