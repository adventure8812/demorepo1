from flask import Flask, request
import subprocess
import re

app = Flask(__name__)





@app.route('/ping1', methods=['GET'])
def ping():
   host = request.args.get('host12')
   if not host:
       return "Missing 'host12' parameter", 400
   # Allow only IPv4 addresses or simple hostnames (letters, digits, hyphens, dots)
   if not re.fullmatch(r"[A-Za-z0-9.-]+", host):
       return "Invalid host", 400
   # Prefer subprocess.run with argument list to avoid shell interpretation
   try:
       subprocess.run(["ping", "-c", "1", host], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
   except subprocess.CalledProcessError:
       return "Ping failed", 502
   return f"Ping sent", 200

@app.route('/curl', methods=['GET'])
def curl():
   host = request.args.get('host')
   os.system(f'curl {host}')
   return f"Curl sent", 200

if __name__ == '__main__':
   app.run(debug=False, port=5002)
