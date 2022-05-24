import numpy as np
import json
import cv2

def get_data(room):
  with open(room + 'xx.json', 'r') as fp:
    data = json.load(fp)
  
  return data

def get_map():
  with open('map.json', 'r') as fp:
    map = json.load(fp)
  
  return map

def get_color_from_signal(signal):
  hmin = 60
  hmax = 120

  sigmin = -30
  sigmax = -70

  x = (signal - sigmin) / (sigmax - sigmin)
  h = x * (hmax - hmin) + hmin
  b, g, r = cv2.cvtColor(np.uint8([[(h, 255 / 2, 255)]]), cv2.COLOR_HLS2RGB)[0][0]
  return (int(b), int(g), int(r))


def main():
  ssid = 'UTFPR-VISITANTE'
  floor = 'e2'
  room_template = cv2.imread('room_template.png')
  room_sig = np.zeros((room_template.shape[0], room_template.shape[1]), dtype=np.float32)
  signal_count = np.zeros((room_template.shape[0], room_template.shape[1]), dtype=np.float32)

  map = get_map()
  data = get_data(floor)

  texts = []

  for room in map:
    r = floor + room[1:]
    for pos in map[room]:
      if not r in data[ssid]:
        continue

      x, y = map[room][pos]
      pos_data = data[ssid][r][pos]
      texts.append((x, y, pos_data['signal'], pos_data['channel']))
      signal = int(pos_data['signal'].split(' ')[0])
      circle_mask = np.zeros_like(room_template)
      cv2.circle(circle_mask, (x, y), 50, (255, 255, 255), -1)
      #circle_mask = cv2.GaussianBlur(circle_mask, (0, 0), 5)
      signal_count = np.where(circle_mask[:, :, 0], signal_count + 1, signal_count)
      room_sig = np.where(circle_mask[:, :, 0], ((circle_mask[:, :, 0] / 255) * signal) + room_sig, room_sig)
  
  heatmap = np.zeros_like(room_template)
  for i in range(room_sig.shape[0]):
    for j in range(room_sig.shape[1]):
      if signal_count[i, j] != 0:
        heatmap[i, j] = get_color_from_signal(room_sig[i, j] / signal_count[i, j])
      else:
        heatmap[i, j] = room_template[i, j]
  
  final = cv2.addWeighted(room_template, 0.5, heatmap, 0.5, 0)
  for x, y, signal, channel in texts:
    cv2.putText(final, signal, (x - 27, y), cv2.FONT_HERSHEY_SIMPLEX, 0.3, 0, 1)
    cv2.putText(final, channel, (x - 27, 10 + y), cv2.FONT_HERSHEY_SIMPLEX, 0.3, 0, 1)
  
  # cv2.imshow(floor + 'heatmap.png', final)
  # def click(event, x, y, flags, param):
  #   if event == cv2.EVENT_LBUTTONDOWN:
  #     print(room_sig[y, x])
  # cv2.setMouseCallback(floor + 'heatmap.png', click)
  # cv2.waitKey(0)
  cv2.imwrite(floor + 'heatmap.png', final)

if __name__ == '__main__':
  main()