from flask import Flask, request
import os

app = Flask(__name__)





@app.route('/ping1', methods=['GET'])
def ping():
   host = request.args.get('host1')
   os.system(f'ping -c 1 {host}')
   return f"Ping sent", 200

@app.route('/curl', methods=['GET'])
def curl():
   host = request.args.get('host')
   os.system(f'curl {host}')
   return f"Curl sent", 200

if __name__ == '__main__':
   app.run(debug=False, port=5002)
