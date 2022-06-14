import socket
import codecs

HOST = "localhost"
PORT = 1234

def main():
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(bytes("Olá José!", "utf-8"))
    data = s.recv(1024)
    print("Received", codecs.decode(data, "utf-8"))

if __name__ == '__main__':
  main()