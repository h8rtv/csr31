import socket
from lib.crypto import Crypto
from lib.env import get_env

env = get_env()


def send_msg(msg):
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((env.get("HOST"), env.get("PORT")))
    s.sendall(msg)