import socket
from lib.env import get_env

env = get_env()

def tcp_server(callback):
  while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      print("Server started")
      s.bind((env.get("HOST"), env.get("PORT")))
      print("Server binded")
      s.listen()
      conn, addr = s.accept()
      with conn:
        print("Connected by", addr)
        while True:
          data = conn.recv(1024)
          if not data:
            break
          callback(data)
      conn.close()
