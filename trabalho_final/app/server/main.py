from threading import Thread
import codecs
import sys

from PySide6 import QtWidgets

from lib.env import get_env
from lib.crypto import Crypto
import server.window as window
import server.server as server

# TODO codificação de linha manchester
env = get_env()
crypto = Crypto(env.get("KEY"))

def parse_data(data):
  binary_msg = ''
  for byte in data:
    binary_msg += '{0:08b}'.format(ord(byte))

  encrypted_msg = codecs.decode(data, "latin-1")

  msg = crypto.decrypt(data)

  return {
    "encrypted_msg": encrypted_msg,
    "binary_msg": binary_msg,
    "msg": msg,
  }

def main():
  app = QtWidgets.QApplication(sys.argv)

  server_window = window.ServerWindow()
  def handle_data(data):
    server_window.on_data(parse_data(data))

  Thread(target=server.tcp_server, args=(handle_data,)).start()

  server_window.show()
  sys.exit(app.exec_())