import socket
import codecs
import lib.crypto as crypto

HOST = "localhost"
PORT = 1234
KEY = 42

crypto = crypto.Crypto(KEY)

def main():
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(crypto.encrypt("mensagem linda de ámor e páz"))
    data = s.recv(1024)
    print("Received", codecs.decode(data, "utf-8"))

if __name__ == '__main__':
  main()