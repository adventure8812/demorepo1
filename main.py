from flask import Flask, request
import os
import socket
import struct
import time

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
   return {"status": "healthy", "service": "ping-service"}, 200

@app.route('/health2', methods=['GET'])
def health():
   return {"status": "health2222y", "service": "ping-service"}, 200

if __name__ == '__main__':
   app.run(debug=False, port=5001)
