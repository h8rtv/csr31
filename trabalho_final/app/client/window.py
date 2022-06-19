from PySide6 import QtCore, QtWidgets

from matplotlib.backends.backend_qtagg import (
    FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure

import client.handler as handler

class ClientWindow(QtWidgets.QWidget):
  def __init__(self):
    super().__init__()

    self.msg = QtWidgets.QLineEdit()
    self.msg.textChanged.connect(self.on_msg_changed)

    self.encrypted_msg = QtWidgets.QLineEdit()
    self.encrypted_msg.setReadOnly(True)

    self.binary_msg = QtWidgets.QLineEdit()
    self.binary_msg.setReadOnly(True)

    self.binary_msg_manchester = QtWidgets.QLineEdit()
    self.binary_msg_manchester.setReadOnly(True)

    self.send_button = QtWidgets.QPushButton('Enviar')
    self.send_button.clicked.connect(self.send_msg)

    self.canvas = self.build_canvas()

    flo = QtWidgets.QFormLayout()
    flo.addRow('Mensagem:', self.msg)
    flo.addRow('Mensagem criptografada:', self.encrypted_msg)
    flo.addRow('Mensagem binária:', self.binary_msg)
    flo.addRow('Mensagem binária com codificação Manchester:', self.binary_msg_manchester)
    flo.addWidget(NavigationToolbar(self.canvas, self))
    flo.addRow(self.canvas)
    flo.addRow(self.send_button)

    self.setLayout(flo)
    self.setWindowTitle('Client')

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

  @QtCore.Slot(str)
  def on_msg_changed(self, msg):
    encrypted = handler.get_encrypted_msg(msg)
    self.encrypted_msg.setText(encrypted)
    self.binary_msg.setText(handler.get_binary_msg(encrypted))
    self.binary_msg_manchester.setText(handler.manchester_encode(encrypted))
    self.update_canvas()

  @QtCore.Slot()
  def send_msg(self):
    handler.send_msg(self.binary_msg_manchester.text())
