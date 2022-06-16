from PySide6 import QtCore, QtWidgets

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

    flo = QtWidgets.QFormLayout()
    flo.addRow('Mensagem:', self.msg)
    flo.addRow('Mensagem criptografada:', self.encrypted_msg)
    flo.addRow('Mensagem binária:', self.binary_msg)
    flo.addRow('Mensagem binária com codificação Manchester:', self.binary_msg_manchester)

    self.setLayout(flo)
    self.setWindowTitle('Server')
  
  @QtCore.Slot(dict)
  def on_data(self, data):
    self.msg.setText(data['msg'])
    self.encrypted_msg.setText(data['encrypted_msg'])
    self.binary_msg.setText(data['binary_msg'])
    self.binary_msg_manchester.setText(data['binary_msg_manchester'])
