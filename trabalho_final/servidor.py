import socket
import codecs
import lib.crypto as crypto

HOST = "localhost"
PORT = 1234
KEY = 42

crypto = crypto.Crypto(KEY)

def main():
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.bind((HOST, PORT))
      s.listen()
      conn, addr = s.accept()
      with conn:
          print("Connected by", addr)
          while True:
              data = conn.recv(1024)
              if not data:
                break
              data = crypto.decrypt(data)
              data = codecs.decode(data, "latin-1")
              print("Received", data)
              conn.sendall(b"Recebido")

if __name__ == '__main__':
  main()