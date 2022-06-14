
import socket

HOST = "localhost"
PORT = 1234

def main():
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello, world!")
    data = s.recv(1024)
    print("Received", repr(data))

if __name__ == '__main__':
  main()