def manchester_encode(mensagem):
  binario = ""
  for x in mensagem:
    binario += '{0:08b}'.format(ord(x))

  clock = [clock % 2 for clock in range(1, len(binario) * 2 + 1)]
  clockStr = ''.join(str(e) for e in clock)
  manchester = ""
  cont = 0
  for i in binario:
    if (i == '1' and clockStr[cont] == '0') or (i == '0' and clockStr[cont] == '1'):
      manchester += '1'
    else:
      manchester += '0'
    cont = cont + 1
    if (i == '1' and clockStr[cont] == '0') or (i == '0' and clockStr[cont] == '1'):
      manchester += '1'
    else:
      manchester += '0'
    cont = cont + 1

  return manchester

def manchester_decode(manchester):
  decmanchester = ""
  for num in range(1, len(manchester)):
    if(num % 2):
      decmanchester += manchester[num]
  
  return decmanchester
    
def bitstring_to_bytes(s):
  v = int(s, 2)
  b = bytearray()
  while v:
    b.append(v & 0xff)
    v >>= 8
  return bytes(b[::-1])