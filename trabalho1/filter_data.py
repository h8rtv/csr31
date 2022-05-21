import os
import pandas as pd
import re
import json

def get_files(path):
    for _, _, files2 in os.walk('./medidas/' + path):
      for file in files2:
        room = file.split('-')[0]
        pos = file.split('-')[1].split('.')[0]
        yield ('./medidas/' + path + '/' + file, room, pos)


def main():
  d = {
    'UTFPR-VISITANTE': {},
    'UTFPR-ALUNO': {},
    'UTFPR-SERVIDOR':{},
  }

  floor = 'e1'
  for file, room, pos in get_files(floor):
    df = pd.read_csv(file, names=['ssid', 'col2', 'col3', 'freq', 'channel', 'signal', 'col7', 'col8', 'col9'], sep=',', engine='python')

    row_visitante = df.loc[df['ssid'] == 'UTFPR-VISITANTE']
    row_visitante = row_visitante.loc[df['freq'].map(lambda x: x[:1]) == '2'].iloc[0]

    row_aluno = df.loc[df['ssid'] == 'UTFPR-ALUNO']
    row_aluno = row_aluno.loc[df['freq'].map(lambda x: x[:1]) == '2'].iloc[0]

    row_servidor = df.loc[df['ssid'] == 'UTFPR-SERVIDOR']
    row_servidor = row_servidor.loc[df['freq'].map(lambda x: x[:1]) == '2'].iloc[0]

    if not room in d['UTFPR-ALUNO']:
      d['UTFPR-ALUNO'][room] = {}

    if not room in d['UTFPR-SERVIDOR']:
      d['UTFPR-SERVIDOR'][room] = {}

    if not room in d['UTFPR-VISITANTE']:
      d['UTFPR-VISITANTE'][room] = {}

    d['UTFPR-ALUNO'][room][pos] = {
      'signal': row_aluno['signal'],
      'channel': row_aluno['channel'],
    }
    d['UTFPR-VISITANTE'][room][pos] = {
      'signal': row_visitante['signal'],
      'channel': row_visitante['channel'],
    }
    d['UTFPR-SERVIDOR'][room][pos] = {
      'signal': row_servidor['signal'],
      'channel': row_servidor['channel'],
    }
  
  with open(floor + 'xx.json', 'w') as fp:
    json.dump(d, fp)



if __name__ == '__main__':
  main()