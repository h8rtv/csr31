from PySide6 import QtCore, QtWidgets

from matplotlib.backends.backend_qtagg import (
    FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure

import client.handler as handler

class ServerWindow(QtWidgets.QWidget):
  def __init__(self):
    super().__init__()

    self.msg = QtWidgets.QLineEdit()
    self.msg.setReadOnly(True)

    self.encrypted_msg = QtWidgets.QLineEdit()
    self.encrypted_msg.setReadOnly(True)

    self.binary_msg = QtWidgets.QLineEdit()
    self.binary_msg.setReadOnly(True)

    self.binary_msg_manchester = QtWidgets.QLineEdit()
    self.binary_msg_manchester.setReadOnly(True)

    self.canvas = self.build_canvas()

    flo = QtWidgets.QFormLayout()
    flo.addRow('Mensagem:', self.msg)
    flo.addRow('Mensagem criptografada:', self.encrypted_msg)
    flo.addRow('Mensagem binária:', self.binary_msg)
    flo.addRow('Mensagem binária com codificação Manchester:', self.binary_msg_manchester)
    flo.addWidget(NavigationToolbar(self.canvas, self))
    flo.addRow(self.canvas)

    self.setLayout(flo)
    self.setWindowTitle('Server')

  @QtCore.Slot(dict)
  def on_data(self, data):
    self.msg.setText(data['msg'])
    self.encrypted_msg.setText(data['encrypted_msg'])
    self.binary_msg.setText(data['binary_msg'])
    self.binary_msg_manchester.setText(data['binary_msg_manchester'])
    self.update_canvas()

  def build_canvas(self):
    canvas = FigureCanvas(Figure(figsize=(5, 3)))
    self.canvas_subplots = canvas.figure.subplots()
    return canvas

  def update_canvas(self):
    self.canvas_subplots.cla()
    data = self.binary_msg_manchester.text()
    if len(data) > 0:
      y = [int(c) for c in data]
      y.append(y[-1])

      x = [v / 2 for v in range(len(y))]
      self.canvas_subplots.step(x, y, where='post')

    self.canvas_subplots.figure.canvas.draw()
