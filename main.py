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

@app.route('/ping', methods=['GET'])
def ping():
   host = request.args.get('host', 'localhost')
   try:
       sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
       sock.settimeout(2)
       packet = struct.pack('!BBHHH', 8, 0, 0, 1, 1)
       sock.sendto(packet + struct.pack('!H', (~sum(struct.unpack('!4H', packet)) & 0xffff)), (socket.gethostbyname(host), 0))
       sock.recvfrom(1024)
       sock.close()
       return f"Host {host} is reachable", 200
   except:
       return f"Host {host} is unreachable", 200

if __name__ == '__main__':
   app.run(debug=False, port=5001)
