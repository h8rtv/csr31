class Crypto:
  def __init__(self, key):
    self.key = key

  # Ceasar cipher
  def encrypt(self, text):
    b = bytes(text, "latin-1")
    encrypted = []
    for byte in b:
      encrypted.append((byte + self.key) % 255)
    
    return bytes(encrypted)

  # Ceasar cipher
  def decrypt(self, b):
    decrypted = []
    for byte in b:
      if (byte - self.key) < 0:
        decrypted.append(byte - self.key + 255)
      else:
        decrypted.append(byte - self.key)
    
    return bytes(decrypted)
