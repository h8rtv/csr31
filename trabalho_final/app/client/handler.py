import codecs

from lib.env import get_env
from lib.crypto import Crypto

env = get_env()
crypto = Crypto(env.get("KEY"))

def get_encrypted_msg(msg):
  encrypted = crypto.encrypt(msg)
  return codecs.decode(encrypted, "latin-1")

def get_binary_msg(data):
  binary_msg = ''
  for byte in data:
    binary_msg += '{0:08b}'.format(ord(byte))
  return binary_msg
