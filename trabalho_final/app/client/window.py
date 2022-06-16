from PySide6 import QtCore, QtWidgets

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

    self.send_button = QtWidgets.QPushButton('Enviar')
    self.send_button.clicked.connect(self.send_msg)

    flo = QtWidgets.QFormLayout()
    flo.addRow('Mensagem:', self.msg)
    flo.addRow('Mensagem criptografada:', self.encrypted_msg)
    flo.addRow('Mensagem binária:', self.binary_msg)
    flo.addRow(self.send_button)

    self.setLayout(flo)
    self.setWindowTitle('Client')
  
  @QtCore.Slot(str)
  def on_msg_changed(self, msg):
    self.encrypted_msg.setText(handler.get_encrypted_msg(msg))
    self.binary_msg.setText(handler.get_binary_msg(msg))

  @QtCore.Slot()
  def send_msg(self):
    pass
