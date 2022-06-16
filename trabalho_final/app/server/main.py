from threading import Thread
import codecs
import sys

from PySide6 import QtWidgets

from lib.env import get_env
from lib.crypto import Crypto
from lib.manchester_code import manchester_decode, bitstring_to_bytes
import server.window as window
import server.server as server

# TODO codificação de linha manchester
env = get_env()
crypto = Crypto(env.get("KEY"))

def parse_data(data):
  binary_msg_manchester = ''
  for c in data:
    binary_msg_manchester += '{0:08b}'.format(c)
  
  binary_msg = manchester_decode(binary_msg_manchester)

  decoded_data = bitstring_to_bytes(binary_msg)
  encrypted_msg = codecs.decode(decoded_data, 'latin-1')

  msg = crypto.decrypt(encrypted_msg)
  msg = codecs.decode(msg, "latin-1")

  return {
    "encrypted_msg": encrypted_msg,
    "binary_msg": binary_msg,
    "binary_msg_manchester": binary_msg_manchester,
    "msg": msg,
  }

def main():
  app = QtWidgets.QApplication(sys.argv)

  server_window = window.ServerWindow()
  def handle_data(data):
    server_window.on_data(parse_data(data))

  thread = Thread(target=server.tcp_server, args=(handle_data,))
  thread.setDaemon(True)
  thread.start()

  server_window.show()
  sys.exit(app.exec_())