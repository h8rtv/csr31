import sys

from PySide6 import QtWidgets

from lib.env import get_env
from lib.crypto import Crypto
import client.window as window

env = get_env()
crypto = Crypto(env.get("KEY"))

def main():
  app = QtWidgets.QApplication(sys.argv)
  client_window = window.ClientWindow()

  client_window.show()
  sys.exit(app.exec_())