import socket
from lib.env import get_env

env = get_env()

def tcp_server(callback):
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.bind((env.get("HOST"), env.get("PORT")))
      s.listen()
      conn, addr = s.accept()
      with conn:
          print("Connected by", addr)
          while True:
              data = conn.recv(1024)
              callback(data)
