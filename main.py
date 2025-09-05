from flask import Flask, request
import os

app = Flask(__name__)


## ping service for employees
@app.route('/ping', methods=['GET'])
def ping():
   host = request.args.get('host', 'localhost')
   os.system(f'ping -c 1 {host}')
   return f"Ping sent", 200

if __name__ == '__main__':
   app.run(debug=False, port=5001)
