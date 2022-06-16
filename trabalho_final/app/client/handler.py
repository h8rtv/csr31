import codecs

from lib.env import get_env
from lib.crypto import Crypto
import lib.manchester_code as manchester_code
import client.client as client

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

def send_msg(msg):
  msg = manchester_code.bitstring_to_bytes(msg)
  client.send_msg(msg)

def manchester_encode(msg):
  return manchester_code.manchester_encode(msg)
