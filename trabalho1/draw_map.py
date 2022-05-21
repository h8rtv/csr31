import cv2
import json

def make_dict(positions):
  positions_dict = {
    'x01': {},
    'x02': {},
    'x03': {},
    'xxx': {},
  }
  x01 = positions[:8]
  x02 = positions[8:14]
  x03 = positions[14:20]
  xxx = positions[20:27]
  
  for i, pos in enumerate(x01):
    positions_dict['x01']['0' + str(i+1)] = pos

  for i, pos in enumerate(x02):
    positions_dict['x02']['0' + str(i+1)] = pos

  for i, pos in enumerate(x03):
    positions_dict['x03']['0' + str(i+1)] = pos

  for i, pos in enumerate(xxx):
    positions_dict['xxx']['0' + str(i+1)] = pos

  return positions_dict

def main():
  room_template = cv2.imread('room_template.png')
  cv2.imshow('room_template', room_template)

  positions = []
  def callback(event, x, y, flags, param):
    if event == 4:
      positions.append((x, y))
      
  cv2.setMouseCallback('room_template', callback)

  key = 0
  while (key != 27):
    if key == 117: # U
      positions.pop()

    if key == 114: # R
      positions = []

    room = room_template.copy()
    for x, y in positions:
      cv2.circle(room, (x, y), 50, (255, 0, 0), 1)

    cv2.imshow("room_template", room)
    key = cv2.waitKey(1)

  dict = make_dict(positions)

  with open('map.json', 'w') as fp:
    json.dump(dict, fp)

  cv2.destroyAllWindows()

if __name__ == '__main__':
  main()
